(function () {
  "use strict";

  const DATA = window.PNWTAP;
  const CFG = DATA.config;
  const S = window.PNWTAP_SCORING;

  const card = document.getElementById("card");
  const cardBody = document.getElementById("card-body");
  const roundPill = document.getElementById("round-pill");
  const puzzleNo = document.getElementById("puzzle-no");
  const helpBtn = document.getElementById("help-btn");
  const setPill = (t) => { roundPill.textContent = t; };

  const esc = (s) => String(s ?? "").replace(/[&<>"']/g, (c) => (
    { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));

  // ---- dates ----
  const iso = (d) => {
    const p = (n) => String(n).padStart(2, "0");
    return `${d.getFullYear()}-${p(d.getMonth() + 1)}-${p(d.getDate())}`;
  };
  const parseISO = (s) => new Date(s + "T00:00:00");
  const addDays = (s, n) => { const d = parseISO(s); d.setDate(d.getDate() + n); return iso(d); };
  const dayNumber = (s) => Math.round((parseISO(s) - parseISO(CFG.epoch)) / 864e5) + 1;
  const prettyDate = (s) => parseISO(s).toLocaleDateString("en-US", { month: "short", day: "numeric" });

  const TODAY = iso(new Date());
  // ?date=YYYY-MM-DD plays a past puzzle (never a future one)
  const requested = new URLSearchParams(location.search).get("date");
  const DATE = requested && requested <= TODAY && DATA.schedule[requested] ? requested : TODAY;
  const IS_ARCHIVE = DATE !== TODAY;
  const todaysIds = DATA.schedule[DATE];

  // ---- storage (localStorage may be unavailable: private mode, blocked site data) ----
  const store = {
    get(k) { try { return JSON.parse(localStorage.getItem(k)); } catch (e) { return null; } },
    set(k, v) { try { localStorage.setItem(k, JSON.stringify(v)); } catch (e) { /* play on */ } },
    keys() { try { return Object.keys(localStorage); } catch (e) { return []; } },
  };
  const KEY = (d) => "pnwtap:" + d;
  function loadGame(d) {
    const g = store.get(KEY(d));
    if (Array.isArray(g)) return { rounds: g, done: true, playedOn: d };   // v1 format
    return g && Array.isArray(g.rounds) ? g : null;
  }

  // ---- map ----
  const MASK = DATA.regionMask || [];
  const bb = CFG.bbox; // [minLat, minLng, maxLat, maxLng]
  let regionBounds = L.latLngBounds([bb[0], bb[1]], [bb[2], bb[3]]);
  if (MASK.length) {
    regionBounds = L.latLngBounds(MASK[0]);
    MASK.forEach((ring) => ring.forEach((pt) => regionBounds.extend(pt)));
  }
  const startBounds = L.latLngBounds(CFG.startBounds);
  const compact = window.matchMedia("(max-width: 640px)").matches;

  const map = L.map("map", {
    minZoom: CFG.minZoom,
    maxZoom: CFG.maxZoom,
    maxBounds: regionBounds.pad(0.35),
    maxBoundsViscosity: 0.25,
    zoomControl: false,
    attributionControl: false,
    zoomSnap: 0.25,
  });
  if (!compact) L.control.zoom({ position: "bottomright" }).addTo(map);
  L.control.attribution({ position: compact ? "topright" : "bottomright", prefix: false })
    .addAttribution(CFG.tileAttribution).addTo(map);

  L.tileLayer(CFG.tileUrl, {
    bounds: regionBounds, noWrap: true, minZoom: CFG.minZoom, maxZoom: CFG.maxZoom,
  }).addTo(map);

  if (CFG.hillshadeUrl) {
    map.createPane("hillshade");
    const pane = map.getPane("hillshade");
    pane.style.zIndex = 250;
    pane.classList.add("hillshade-pane");
    L.tileLayer(CFG.hillshadeUrl, { pane: "hillshade", maxZoom: CFG.maxZoom }).addTo(map);
  }

  // Stencil: the frame colour everywhere except region-shaped holes (WA/OR/BC/AB/YT).
  if (MASK.length) {
    const maskRenderer = L.svg({ padding: 3 });
    const outN = Math.min(85, regionBounds.getNorth() + 25);
    const outS = Math.max(-85, regionBounds.getSouth() - 25);
    const outW = regionBounds.getWest() - 50;
    const outE = regionBounds.getEast() + 50;
    const outer = [[outN, outW], [outN, outE], [outS, outE], [outS, outW]];
    L.polygon([outer].concat(MASK), {
      renderer: maskRenderer, stroke: false,
      fill: true, fillColor: "#2b352e", fillOpacity: 1, interactive: false,
    }).addTo(map);
    L.polygon(MASK, {
      renderer: maskRenderer, fill: false,
      stroke: true, color: "#e2c48b", weight: 1, opacity: 0.5, interactive: false,
    }).addTo(map);
  }

  const roundLayers = L.layerGroup().addTo(map);

  const guessIcon = (label) => L.divIcon({
    className: "guess-marker",
    html: `<span class="guess-dot">${label || ""}</span>`,
    iconSize: [22, 22], iconAnchor: [11, 11],
  });
  const answerIcon = (pulse) => L.divIcon({
    className: "answer-marker",
    html: (pulse ? '<span class="answer-ring"></span>' : "") + '<span class="answer-dot"></span>',
    iconSize: [22, 22], iconAnchor: [11, 11],
  });

  // Keep revealed features clear of the floating card.
  function framePadding() {
    const r = card.getBoundingClientRect();
    const H = window.innerHeight;
    const m = 36;
    if (r.right < window.innerWidth / 2) {           // wide screens: card docked on the left
      return { paddingTopLeft: [r.right + m, m], paddingBottomRight: [m, m] };
    }
    const sheet = r.bottom >= H - 2;                 // phone bottom sheet vs. floating top card
    const covered = Math.min(sheet ? H - r.top : r.bottom, H - 140);   // always leave some map
    return sheet
      ? { paddingTopLeft: [m, m], paddingBottomRight: [m, covered + m] }
      : { paddingTopLeft: [m, covered + m], paddingBottomRight: [m, m] };
  }
  function frame(bounds, opts) {
    map.flyToBounds(bounds, Object.assign(framePadding(), { duration: 0.7, maxZoom: 10 }, opts));
  }
  const resetView = () => map.fitBounds(startBounds, Object.assign(framePadding(), { animate: false }));

  // ---- keyboard: Enter presses the card's primary button ----
  document.addEventListener("keydown", (e) => {
    if (e.key !== "Enter" || !helpEl.hidden || e.target.closest?.("button, a, input")) return;
    const btn = cardBody.querySelector("button.primary:not(:disabled)");
    if (btn) { e.preventDefault(); btn.click(); }
  });

  const CAT_LABEL = { poi: "landmark" };

  // ---- scoring helpers ----
  const total = (rounds) => rounds.reduce((s, r) => s + r.score * r.mult, 0);
  const fmtKm = (km) => (km < 1 ? km.toFixed(1) : km < 10 ? km.toFixed(1).replace(/\.0$/, "") : Math.round(km)) + " km";
  function verdict(score) {
    if (score >= 99) return "Bullseye! 🎯";
    if (score >= 90) return "Nailed it";
    if (score >= 70) return "So close";
    if (score >= 40) return "Right neighbourhood";
    if (score >= 15) return "In the ballpark";
    return "Way off";
  }
  const maxScore = 100 * CFG.multipliers.reduce((a, b) => a + b, 0);

  // ---- help overlay ----
  const helpEl = document.getElementById("help");
  function openHelp() {
    helpEl.hidden = false;
    helpEl.querySelector("button").focus({ preventScroll: true });
  }
  function closeHelp() {
    helpEl.hidden = true;
    store.set("pnwtap-help-seen", 1);
  }
  document.getElementById("help-tiers").textContent =
    CFG.ramp.map((t, i) => `${CFG.emoji[t]} ×${CFG.multipliers[i]}`).join("  ");
  helpEl.querySelector("button").onclick = closeHelp;
  helpEl.onclick = (e) => { if (e.target === helpEl) closeHelp(); };
  helpBtn.onclick = openHelp;
  document.addEventListener("keydown", (e) => { if (e.key === "Escape" && !helpEl.hidden) closeHelp(); });

  // ---- game ----
  if (!todaysIds) {
    resetView();
    cardBody.innerHTML = '<p class="msg">No puzzle scheduled for today — check back another day!</p>';
    return;
  }

  puzzleNo.textContent = `#${dayNumber(DATE)}` + (IS_ARCHIVE ? ` · ${prettyDate(DATE)}` : "");
  const game = loadGame(DATE) || { rounds: [], done: false };
  const save = () => store.set(KEY(DATE), game);

  function startRound() {
    roundLayers.clearLayers();
    const roundIdx = game.rounds.length;
    const loc = DATA.locations[todaysIds[roundIdx]];
    const mult = CFG.multipliers[roundIdx];
    setPill(`${roundIdx + 1} / ${todaysIds.length}`);

    const icon = CFG.categories[loc.category] || "📍";
    const label = `<span class="cat">${icon} ${esc(CAT_LABEL[loc.category] || loc.category)}</span>`;
    const line = loc.geometry.length > 1 ? '<p class="hint">Anywhere along it counts.</p>' : "";
    const ask = loc.image
      ? `<p class="ask">Where is <strong>this place</strong>?</p>${label}` +
        `<img class="prompt-img" src="${esc(loc.image)}" alt="Photo of the mystery location">`
      : `<p class="ask"><strong>${esc(loc.name)}</strong></p>${label}${line}`;
    cardBody.innerHTML =
      `<div class="round-meta"><span>${CFG.emoji[loc.difficulty]} ${esc(loc.difficulty)} · ×${mult}</span>` +
      `<span>${total(game.rounds)} pts so far</span></div>` + ask +
      '<button class="primary" id="lock" disabled>Tap the map</button>';
    const lockBtn = document.getElementById("lock");
    resetView();   // after the card is filled, so the framing knows its size

    let tap = null;
    let marker = null;
    function place(latlng) {
      tap = [latlng.lat, latlng.lng];
      if (!marker) {
        marker = L.marker(latlng, { icon: guessIcon(), draggable: true, autoPan: true }).addTo(roundLayers);
        marker.on("dragend", () => place(marker.getLatLng()));
      } else {
        marker.setLatLng(latlng);
      }
      lockBtn.disabled = false;
      lockBtn.textContent = "Lock in guess";
    }
    const onClick = (e) => place(e.latlng);
    map.on("click", onClick);

    lockBtn.onclick = () => {
      if (!tap) return;
      map.off("click", onClick);
      if (marker.dragging) marker.dragging.disable();
      const near = S.nearest(tap, loc.geometry);
      const score = S.score(near.km, CFG.D_km);
      const r = {
        i: todaysIds[roundIdx], name: loc.name, difficulty: loc.difficulty,
        mult, km: near.km, score, guess: tap, point: near.point,
      };
      game.rounds.push(r);
      if (game.rounds.length === todaysIds.length) { game.done = true; game.playedOn = TODAY; }
      save();
      animateReveal(r, loc);
      renderResult(r, loc);
    };
  }

  // ---- reveal: a line that draws from the guess to the truth ----
  function drawAnswer(loc, point, pulse) {
    if (loc.geometry.length > 1) {
      L.polyline(loc.geometry, { color: "#c0392b", weight: 4, opacity: 0.9, interactive: false }).addTo(roundLayers);
    }
    L.marker(point, { icon: answerIcon(pulse), interactive: false, zIndexOffset: 1000 }).addTo(roundLayers);
  }
  function animateReveal(r, loc) {
    drawAnswer(loc, r.point, true);
    const from = r.guess, to = r.point;
    const line = L.polyline([from, from], {
      color: "#f4c542", weight: 4, opacity: 0.95, lineCap: "round", interactive: false,
    }).addTo(roundLayers);

    const bounds = L.latLngBounds([from, to]);
    if (loc.geometry.length > 1) loc.geometry.forEach((p) => bounds.extend(p));
    frame(bounds);

    setTimeout(() => {
      const t0 = performance.now();
      (function step(now) {
        const t = Math.min(1, (now - t0) / 700);
        const e = 1 - Math.pow(1 - t, 3);
        line.setLatLngs([from, [from[0] + (to[0] - from[0]) * e, from[1] + (to[1] - from[1]) * e]]);
        if (t < 1) requestAnimationFrame(step);
      })(t0);
    }, 720);
  }

  function renderResult(r, loc) {
    setPill(`${game.rounds.length} / ${todaysIds.length}`);
    const last = game.done;
    cardBody.innerHTML =
      `<p class="verdict">${verdict(r.score)}</p>` +
      `<p class="result-name">${esc(loc.name)} <span class="tier">${CFG.emoji[loc.difficulty] || ""}</span></p>` +
      `<p class="result-score"><b>${fmtKm(r.km)}</b> off · <b>${r.score}</b> × ${r.mult} = ` +
        `<span class="pts">${r.score * r.mult}</span></p>` +
      (loc.image ? `<img class="reveal-img" src="${esc(loc.image)}" alt="">` : "") +
      (loc.blurb ? `<p class="reveal-blurb">${esc(loc.blurb)}</p>` : "") +
      `<button class="primary" id="next">${last ? "See results" : "Next round"}</button>`;
    document.getElementById("next").onclick = () => (last ? renderFinal(true) : startRound());
    document.getElementById("next").focus({ preventScroll: true });
  }

  // ---- finish: summary map, breakdown, stats, share ----
  function shareText() {
    const parts = game.rounds.map((r) => `${r.score}${CFG.emoji[r.difficulty]}`).join(" ");
    return `pnwtap #${dayNumber(DATE)} · ${prettyDate(DATE)}\n${parts}\nFinal ${total(game.rounds)}/${maxScore}\n` +
      location.origin + location.pathname;
  }

  function stats() {
    const games = store.keys()
      .filter((k) => /^pnwtap:\d{4}-\d{2}-\d{2}$/.test(k))
      .map((k) => [k.slice(7), loadGame(k.slice(7))])
      .filter(([, g]) => g && g.done);
    const scores = games.map(([, g]) => total(g.rounds));
    const onTime = new Set(games.filter(([d, g]) => (g.playedOn || d) === d).map(([d]) => d));
    let streak = 0;
    for (let d = onTime.has(TODAY) ? TODAY : addDays(TODAY, -1); onTime.has(d); d = addDays(d, -1)) streak++;
    let best = 0, run = 0;
    [...onTime].sort().forEach((d, i, a) => { run = i && addDays(a[i - 1], 1) === d ? run + 1 : 1; best = Math.max(best, run); });
    return {
      played: games.length,
      avg: scores.length ? Math.round(scores.reduce((a, b) => a + b, 0) / scores.length) : 0,
      top: scores.length ? Math.max(...scores) : 0,
      streak, best,
    };
  }

  function drawSummary() {
    roundLayers.clearLayers();
    const bounds = L.latLngBounds([]);
    game.rounds.forEach((r, n) => {
      const loc = DATA.locations[r.i] || { geometry: [r.point] };
      drawAnswer(loc, r.point, false);
      L.polyline([r.guess, r.point], { color: "#f4c542", weight: 3, opacity: 0.9, dashArray: "6 6", interactive: false })
        .addTo(roundLayers);
      L.marker(r.guess, { icon: guessIcon(n + 1), interactive: false }).addTo(roundLayers);
      bounds.extend(r.guess).extend(r.point);
    });
    return bounds;
  }

  function countUp(el, to) {
    const t0 = performance.now();
    (function step(now) {
      const t = Math.min(1, (now - t0) / 900);
      el.textContent = Math.round(to * (1 - Math.pow(1 - t, 3)));
      if (t < 1) requestAnimationFrame(step);
    })(t0);
  }

  let tick = null;
  function renderFinal(fresh) {
    setPill("");
    const bounds = drawSummary();
    if (bounds.isValid()) setTimeout(() => frame(bounds, { maxZoom: 9 }), 50);

    const score = total(game.rounds);
    const st = stats();
    const rows = game.rounds.map((r, n) =>
      `<li data-n="${n}"><span class="rn">${n + 1}</span><span class="rname">${CFG.emoji[r.difficulty]} ${esc(r.name)}</span>` +
      `<span class="rkm">${fmtKm(r.km)}</span><span class="rpts">${r.score * r.mult}</span></li>`).join("");
    const yesterday = addDays(DATE, -1);
    const missed = !IS_ARCHIVE && DATA.schedule[yesterday] && !(loadGame(yesterday) || {}).done
      ? `<a class="archive-link" href="?date=${yesterday}">Missed yesterday? Play #${dayNumber(yesterday)} →</a>` : "";
    const back = IS_ARCHIVE ? '<a class="archive-link" href="./">Back to today’s puzzle →</a>' : "";

    cardBody.innerHTML =
      `<div class="final-head"><div><p class="final">Final score</p>` +
      `<div class="final-score"><span id="final-n">${fresh ? 0 : score}</span><small> / ${maxScore}</small></div></div>` +
      `<div class="next-in"><p class="final">Next puzzle</p><div id="countdown">–</div></div></div>` +
      `<ol class="breakdown">${rows}</ol>` +
      '<button class="primary" id="share">Share result</button>' +
      '<div class="stats">' +
        `<div><b>${st.played}</b><span>played</span></div>` +
        `<div><b>${st.avg}</b><span>average</span></div>` +
        `<div><b>${st.top}</b><span>best</span></div>` +
        `<div><b>${st.streak}</b><span>streak</span></div>` +
      "</div>" + missed + back;
    if (fresh) countUp(document.getElementById("final-n"), score);

    // tap a row to fly to that round
    cardBody.querySelectorAll(".breakdown li").forEach((li) => {
      li.onclick = () => {
        const r = game.rounds[+li.dataset.n];
        const loc = DATA.locations[r.i] || { geometry: [r.point] };
        const b = L.latLngBounds([r.guess, r.point]);
        loc.geometry.forEach((p) => b.extend(p));
        frame(b, { maxZoom: 11 });
      };
    });

    const shareBtn = document.getElementById("share");
    shareBtn.onclick = async () => {
      const text = shareText();
      const touch = window.matchMedia("(pointer: coarse)").matches;
      try {
        if (touch && navigator.share) { await navigator.share({ text }); return; }
        await navigator.clipboard.writeText(text);
        shareBtn.textContent = "Copied to clipboard!";
      } catch (e) {
        if (e && e.name === "AbortError") return;   // user closed the share sheet
        const box = document.createElement("textarea");
        box.className = "share-box";
        box.readOnly = true;
        box.value = text;
        box.rows = text.split("\n").length;
        shareBtn.replaceWith(box);
        box.focus();
        box.select();
      }
    };

    const cd = document.getElementById("countdown");
    clearInterval(tick);
    const upd = () => {
      const now = new Date();
      const mid = new Date(now); mid.setHours(24, 0, 0, 0);
      const s = Math.max(0, Math.floor((mid - now) / 1000));
      if (s === 0 && !IS_ARCHIVE) { location.reload(); return; }
      cd.textContent = [Math.floor(s / 3600), Math.floor(s / 60) % 60, s % 60]
        .map((n) => String(n).padStart(2, "0")).join(":");
    };
    upd();
    tick = setInterval(upd, 1000);
  }

  // ---- go: finished → summary; otherwise the next unplayed round (locked guesses stay locked) ----
  resetView();
  if (game.done) renderFinal(false);
  else startRound();
  if (!store.get("pnwtap-help-seen") && !game.rounds.length) openHelp();
})();
