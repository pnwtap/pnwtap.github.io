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

  // ---- phones: the card is a bottom sheet. Drag its header down to tuck it away (up to
  // bring it back; a tap toggles). While tucked away the header carries the card's main
  // button, so a whole round can be played with the full map in view. New content
  // (a reveal, the next round, the results) brings the sheet back up.
  const head = document.getElementById("card-head");
  const headAction = document.getElementById("head-action");
  const isPhone = () => window.matchMedia("(max-width: 640px)").matches;
  function syncHeadAction() {
    const btn = cardBody.querySelector("button.primary");
    const show = card.classList.contains("collapsed") && btn && !btn.disabled;
    headAction.hidden = !show;
    if (show) headAction.textContent = btn.textContent;
  }
  const setCollapsed = (on) => { card.classList.toggle("collapsed", on); syncHeadAction(); };
  headAction.onclick = () => { const b = cardBody.querySelector("button.primary:not(:disabled)"); if (b) b.click(); };
  let dragY = null, dragDy = 0, dragMoved = false;
  head.addEventListener("pointerdown", (e) => {
    if (!isPhone() || e.target.closest("button")) return;
    dragY = e.clientY; dragDy = 0; dragMoved = false;
    head.setPointerCapture(e.pointerId);
    card.classList.add("dragging");
  });
  head.addEventListener("pointermove", (e) => {
    if (dragY === null) return;
    dragDy = e.clientY - dragY;
    if (Math.abs(dragDy) > 6) dragMoved = true;
    if (!card.classList.contains("collapsed")) card.style.transform = `translateY(${Math.max(0, dragDy)}px)`;
  });
  const dragEnd = () => {
    if (dragY === null) return;
    const collapsed = card.classList.contains("collapsed");
    card.classList.remove("dragging");
    card.style.transform = "";
    if (!dragMoved) setCollapsed(!collapsed);                 // a tap
    else if (!collapsed && dragDy > 40) setCollapsed(true);   // swiped down
    else if (collapsed && dragDy < -20) setCollapsed(false);  // swiped up
    dragY = null;
  };
  head.addEventListener("pointerup", dragEnd);
  head.addEventListener("pointercancel", dragEnd);
  new MutationObserver(() => setCollapsed(false)).observe(cardBody, { childList: true });
  new MutationObserver(syncHeadAction).observe(cardBody, { subtree: true, childList: true, attributes: true, characterData: true });

  // ---- hit counting (GoatCounter, when configured): page views plus a few game events ----
  function hit(path, title, event) {
    const send = () => window.goatcounter.count({ path, title: title || path, event: !!event });
    if (window.goatcounter && window.goatcounter.count) return send();
    const tag = document.querySelector("script[data-goatcounter]");
    if (tag) tag.addEventListener("load", () => window.goatcounter && window.goatcounter.count && send(), { once: true });
  }

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
  const dayLabel = (s) => (dayNumber(s) >= 1 ? `#${dayNumber(s)}` : "practice");
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
    let g = store.get(KEY(d));
    if (Array.isArray(g)) g = { rounds: g, done: true, playedOn: d };      // v1 format
    if (!g || !Array.isArray(g.rounds)) return null;
    // only a save for the puzzle scheduled for that day now counts — a day can be
    // re-curated, and a stale save shouldn't pose as today's result
    const names = (DATA.schedule[d] || []).map((i) => DATA.locations[i].name);
    return names.length && g.rounds.every((r, k) => r.name === names[k]) ? g : null;
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
    const controls = compact ? [m, m] : [m + 40, m + 24];   // keep clear of zoom buttons + attribution
    if (r.right < window.innerWidth / 2) {           // wide screens: card docked on the left
      return { paddingTopLeft: [r.right + m, m], paddingBottomRight: controls };
    }
    const sheet = r.bottom >= H - 2;                 // phone bottom sheet vs. floating top card
    const covered = Math.min(sheet ? H - r.top : r.bottom, H - 140);   // always leave some map
    return sheet
      ? { paddingTopLeft: [m, m + 12], paddingBottomRight: [m, covered + m] }   // attribution sits top-right
      : { paddingTopLeft: [m, covered + m], paddingBottomRight: controls };
  }
  // a page opened in a background tab can have a 0×0 map, where fitting bounds yields NaN
  const sized = () => map.getSize().x > 0 && map.getSize().y > 0;
  function frame(bounds, opts) {
    if (!sized()) return map.setView(bounds.getCenter(), 6, { animate: false });
    map.flyToBounds(bounds, Object.assign(framePadding(), { duration: 0.7, maxZoom: 10 }, opts));
  }
  const resetView = () => (sized()
    ? map.fitBounds(startBounds, Object.assign(framePadding(), { animate: false }))
    : map.setView(startBounds.getCenter(), 5, { animate: false }));

  // ---- keyboard: Enter presses the card's primary button ----
  document.addEventListener("keydown", (e) => {
    if (e.key !== "Enter" || !helpEl.hidden || !fbEl.hidden ||
        e.target.closest?.("button, a, input, select, textarea")) return;
    const btn = cardBody.querySelector("button.primary:not(:disabled)");
    if (btn) { e.preventDefault(); btn.click(); }
  });

  // ---- location presentation: category chip, prompt clues, reveal fact card ----
  const catOf = (loc) => CFG.categories[loc.category] || { icon: "📍", label: loc.category };
  const catChip = (loc) => `<span class="cat">${catOf(loc).icon} ${esc(catOf(loc).label)}</span>`;
  function clueLine(loc) {
    const f = loc.facts || {};
    return (f.clues && f.clues.length ? `<p class="clues">${f.clues.map(esc).join(" · ")}</p>` : "") +
      (f.tagline ? `<p class="tagline">${esc(f.tagline)}</p>` : "");
  }
  function factCard(loc) {
    const f = loc.facts || {};
    if (!f.rows || !f.rows.length) return f.tagline ? `<p class="tagline">${esc(f.tagline)}</p>` : "";
    return '<div class="fact-card">' +
      `<div class="fact-head">${catOf(loc).icon} ${esc(catOf(loc).label)}` +
        (f.tagline ? ` <span class="fact-tag">${esc(f.tagline)}</span>` : "") + "</div>" +
      '<dl class="facts">' +
        f.rows.map(([k, v]) => `<dt>${esc(k)}</dt><dd>${esc(v)}</dd>`).join("") +
      "</dl></div>";
  }
  const scoreFor = (km) => S.score(km, CFG.scoreNearKm, CFG.scoreZeroKm, CFG.scoreShape);

  // ---- scoring helpers ----
  const total = (rounds) => rounds.reduce((s, r) => s + r.score * r.mult, 0);
  const fmtKm = (km) => (km == null ? "–"
    : (km < 1 ? km.toFixed(1) : km < 10 ? km.toFixed(1).replace(/\.0$/, "") : Math.round(km)) + " km");
  const offBy = (km) => (km === 0 ? "<b>Inside it</b>" : `<b>${fmtKm(km)}</b> off`);
  // bands on the score curve: ≥99 ≈ within 3 km, ≥90 ≈ 13 km, ≥75 ≈ 34 km, ≥55 ≈ 95 km,
  // ≥35 ≈ 260 km, ≥15 ≈ 700 km
  function verdict(score) {
    if (score >= 99) return "Bullseye! 🎯";
    if (score >= 90) return "Nailed it";
    if (score >= 75) return "So close";
    if (score >= 55) return "Right neighbourhood";
    if (score >= 35) return "Right region";
    if (score >= 15) return "Right corner of the map";
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
  }
  document.getElementById("help-tiers").textContent =
    CFG.ramp.map((t, i) => `${CFG.emoji[t]} ×${CFG.multipliers[i]}`).join("  ");
  helpEl.querySelector("button").onclick = closeHelp;
  helpEl.onclick = (e) => { if (e.target === helpEl) closeHelp(); };
  helpBtn.onclick = openHelp;
  document.addEventListener("keydown", (e) => { if (e.key === "Escape" && !helpEl.hidden) closeHelp(); });

  // ---- feedback dialog: an in-page form delivered by e-mail (Web3Forms), no login ----
  const fbEl = document.getElementById("feedback");
  const fbForm = document.getElementById("fb-form");
  const fbStatus = fbForm.querySelector(".fb-status");
  const fbSend = document.getElementById("fb-send");
  let fbKind = "place", fbContext = {};
  function openFeedback(kind, context) {
    fbKind = kind;
    fbContext = context;
    document.getElementById("fb-title").textContent = kind === "bug" ? "Report a bug" : "Suggest a place";
    fbForm.querySelectorAll("fieldset").forEach((fs) => {
      const on = fs.dataset.kind === kind;
      fs.hidden = !on;
      fs.disabled = !on;                // hidden fields are neither validated nor sent
    });
    fbForm.elements.about.innerHTML = ['<option value="">—</option>']
      .concat(context.places.map((n) => `<option>${esc(n)}</option>`), ["<option>Something else</option>"]).join("");
    fbStatus.textContent = "";
    fbStatus.classList.remove("error");
    fbSend.disabled = false;
    fbEl.hidden = false;
    (kind === "bug" ? fbForm.elements.what : fbForm.elements.place).focus({ preventScroll: true });
  }
  const closeFeedback = () => { fbEl.hidden = true; };
  document.getElementById("fb-cancel").onclick = closeFeedback;
  fbEl.onclick = (e) => { if (e.target === fbEl) closeFeedback(); };
  document.addEventListener("keydown", (e) => { if (e.key === "Escape" && !fbEl.hidden) closeFeedback(); });
  fbForm.onsubmit = async (e) => {
    e.preventDefault();
    if (!fbForm.reportValidity()) return;
    const f = fbForm.elements;
    const fb = CFG.feedback;
    const lines = fbKind === "bug"
      ? [`What went wrong: ${f.what.value}`, `About: ${f.about.value || "—"}`]
      : [`Place: ${f.place.value}`, `Where: ${f.where.value || "—"}`, `Why: ${f.why.value || "—"}`];
    lines.push(`From: ${f.contact.value || "(anonymous)"}`, "",
      `Puzzle: ${fbContext.puzzle}`, `Places that day: ${fbContext.places.join(" · ")}`,
      `Page: ${location.href}`, `Device: ${navigator.userAgent}`);
    const subject = fbKind === "bug" ? `pnwtap bug (${fbContext.puzzle})` : `pnwtap place idea: ${f.place.value}`;
    fbSend.disabled = true;
    fbStatus.classList.remove("error");
    fbStatus.textContent = "Sending…";
    try {
      const res = await fetch(fb.endpoint, {
        method: "POST",
        headers: { "Content-Type": "application/json", Accept: "application/json" },
        body: JSON.stringify({
          access_key: fb.key, subject, from_name: "pnwtap", botcheck: f.botcheck.checked,
          message: lines.join("\n"), replyto: /@/.test(f.contact.value) ? f.contact.value : undefined,
        }),
      });
      const out = await res.json().catch(() => ({}));
      if (!res.ok || out.success === false) throw new Error(out.message || res.status);
      fbStatus.textContent = "Thanks — sent!";
      hit(`/feedback/${fbKind}`, fbKind === "bug" ? "Sent a bug report" : "Suggested a place", true);
      fbForm.reset();
      setTimeout(closeFeedback, 1400);
    } catch (err) {
      fbStatus.classList.add("error");
      fbStatus.textContent = "Couldn’t send that — please try again in a bit.";
      fbSend.disabled = false;
    }
  };

  // ---- playtest: ?playtest — play any location, check its card, eyeball every answer ----
  const params = new URLSearchParams(location.search);
  if (params.has("playtest")) {
    playtest(params.get("loc"));
    return;
  }

  function playtest(startName) {
    const order = { easy: 0, medium: 1, hard: 2 };
    const all = DATA.locations.map((loc, i) => ({ loc, i }))
      .sort((a, b) => order[a.loc.difficulty] - order[b.loc.difficulty] || a.loc.name.localeCompare(b.loc.name));
    let pos = Math.max(0, all.findIndex((x) => x.loc.name === startName));
    const allLayer = L.layerGroup();
    all.forEach(({ loc }, n) => {
      const opts = { color: "#f4c542", weight: 2, fillOpacity: 0.15 };
      const shape = loc.geometry.length === 1
        ? L.circleMarker(loc.geometry[0], { radius: 5, color: "#fff", weight: 1.5, fillColor: "#c0392b", fillOpacity: 1 })
        : loc.kind === "area" ? L.polygon(loc.geometry, opts) : L.polyline(loc.geometry, opts);
      shape.bindTooltip(`${loc.name} · ${loc.difficulty}`).on("click", (e) => {
        L.DomEvent.stopPropagation(e);
        pos = n;
        show();
      }).addTo(allLayer);
    });
    puzzleNo.textContent = "playtest";
    helpBtn.hidden = true;
    let offTap = null;

    function show() {
      if (offTap) offTap();
      roundLayers.clearLayers();
      const { loc } = all[pos];
      setPill(`${pos + 1} / ${all.length}`);
      const opts = all.map(({ loc: l }, n) =>
        `<option value="${n}"${n === pos ? " selected" : ""}>${CFG.emoji[l.difficulty]} ${esc(l.name)}</option>`).join("");
      cardBody.innerHTML =
        `<div class="pt-bar"><button class="pt-btn" id="pt-prev" aria-label="Previous">◀</button>` +
        `<select id="pt-pick">${opts}</select>` +
        `<button class="pt-btn" id="pt-next" aria-label="Next">▶</button>` +
        `<button class="pt-btn" id="pt-rand" aria-label="Random">🎲</button></div>` +
        `<label class="pt-all"><input type="checkbox" id="pt-all"${map.hasLayer(allLayer) ? " checked" : ""}> show all answers</label>` +
        `<p class="ask"><strong>${esc(loc.name)}</strong></p>` +
        catChip(loc) + `<span class="pt-meta"> · ${loc.kind} · ${esc(loc.difficulty)}</span>` + clueLine(loc) +
        '<div id="pt-out"></div><button class="primary" id="lock" disabled>Tap the map</button>';
      const go = (n) => { pos = (n + all.length) % all.length; show(); };
      document.getElementById("pt-prev").onclick = () => go(pos - 1);
      document.getElementById("pt-next").onclick = () => go(pos + 1);
      document.getElementById("pt-rand").onclick = () => go(Math.floor(Math.random() * all.length));
      document.getElementById("pt-pick").onchange = (e) => go(+e.target.value);
      document.getElementById("pt-all").onchange = (e) => {
        if (e.target.checked) allLayer.addTo(map); else map.removeLayer(allLayer);
      };
      history.replaceState(null, "", `?playtest&loc=${encodeURIComponent(loc.name)}`);

      const lockBtn = document.getElementById("lock");
      let tap = null, marker = null;
      const onClick = (e) => {
        tap = [e.latlng.lat, e.latlng.lng];
        if (!marker) marker = L.marker(e.latlng, { icon: guessIcon() }).addTo(roundLayers);
        else marker.setLatLng(e.latlng);
        lockBtn.disabled = false;
        lockBtn.textContent = "Lock in guess";
      };
      map.on("click", onClick);
      offTap = () => map.off("click", onClick);
      lockBtn.onclick = () => {
        offTap();
        const near = S.nearest(tap, loc.geometry, loc.kind === "area");
        const sc = scoreFor(near.km);
        animateReveal({ guess: tap, point: near.point }, loc);
        document.getElementById("pt-out").innerHTML =
          `<p class="verdict">${verdict(sc)}</p>` +
          `<p class="result-score">${offBy(near.km)} · <b>${sc}</b> / 100</p>` +
          factCard(loc) +
          (loc.blurb ? `<p class="reveal-blurb">${esc(loc.blurb)}</p>` : "");
        lockBtn.textContent = "Next location";
        lockBtn.onclick = () => go(pos + 1);
        lockBtn.focus({ preventScroll: true });
      };
    }
    resetView();
    show();
  }

  // ---- game ----
  if (!todaysIds) {
    resetView();
    cardBody.innerHTML = '<p class="msg">No puzzle scheduled for today — check back another day!</p>';
    return;
  }

  puzzleNo.textContent = dayLabel(DATE) + (IS_ARCHIVE ? ` · ${prettyDate(DATE)}` : "");
  const game = loadGame(DATE) || { rounds: [], done: false };
  // saved rounds keep the location's name; look it up by name, since row indices shift
  // whenever the sheet gains rows (fall back to the index for very old saves)
  const byName = new Map(DATA.locations.map((l) => [l.name, l]));
  const locOf = (r) => byName.get(r.name) || DATA.locations[r.i] || { geometry: [r.point] };
  const save = () => store.set(KEY(DATE), game);

  function startRound() {
    roundLayers.clearLayers();
    const roundIdx = game.rounds.length;
    const loc = DATA.locations[todaysIds[roundIdx]];
    const mult = CFG.multipliers[roundIdx];
    setPill(`${roundIdx + 1} / ${todaysIds.length}`);

    const hint = loc.kind === "area" ? '<p class="hint">Anywhere inside it counts.</p>'
      : loc.kind === "line" ? '<p class="hint">Anywhere along it counts.</p>' : "";
    const ask = loc.image
      ? `<p class="ask">Where is <strong>this place</strong>?</p>${catChip(loc)}${clueLine(loc)}` +
        `<img class="prompt-img" src="${esc(loc.image)}" alt="Photo of the mystery location">`
      : `<p class="ask"><strong>${esc(loc.name)}</strong></p>${catChip(loc)}${clueLine(loc)}${hint}`;
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
      const near = S.nearest(tap, loc.geometry, loc.kind === "area");
      const score = scoreFor(near.km);
      const r = {
        i: todaysIds[roundIdx], name: loc.name, difficulty: loc.difficulty,
        mult, km: near.km, score, guess: tap, point: near.point,
      };
      game.rounds.push(r);
      const day = dayNumber(DATE) >= 1 ? dayNumber(DATE) : "practice";
      if (game.rounds.length === 1) hit(`/start/${day}`, `Started ${dayLabel(DATE)}`, true);
      if (game.rounds.length === todaysIds.length) {
        game.done = true;
        game.playedOn = TODAY;
        // 50-point bands per day: enough to draw a score histogram later
        const band = Math.min(950, Math.floor(total(game.rounds) / 50) * 50);
        hit(`/finish/${day}`, `Finished ${dayLabel(DATE)}`, true);
        hit(`/score/${day}/${band}`, `${dayLabel(DATE)}: final score ${band}–${band + 49}`, true);
      }
      save();
      animateReveal(r, loc);
      renderResult(r, loc);
    };
  }

  // ---- reveal: a line that draws from the guess to the truth ----
  function drawAnswer(loc, point, pulse) {
    if (loc.kind === "area") {
      L.polygon(loc.geometry, { color: "#c0392b", weight: 2, fillOpacity: 0.25, interactive: false }).addTo(roundLayers);
    } else if (loc.geometry.length > 1) {
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
      `<p class="result-score">${offBy(r.km)} · <b>${r.score}</b> × ${r.mult} = ` +
        `<span class="pts">${r.score * r.mult}</span></p>` +
      (loc.image ? `<img class="reveal-img" src="${esc(loc.image)}" alt="">` : "") +
      factCard(loc) +
      (loc.blurb ? `<p class="reveal-blurb">${esc(loc.blurb)}</p>` : "") +
      `<button class="primary" id="next">${last ? "See results" : "Next round"}</button>`;
    document.getElementById("next").onclick = () => (last ? renderFinal(true) : startRound());
    document.getElementById("next").focus({ preventScroll: true });
  }

  // ---- finish: summary map, breakdown, stats, share ----
  function shareText() {
    const parts = game.rounds.map((r) => `${r.score}${CFG.emoji[r.difficulty]}`).join(" ");
    return `pnwtap ${dayLabel(DATE)} · ${prettyDate(DATE)}\n${parts}\nFinal ${total(game.rounds)}/${maxScore}\n` +
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
    return {
      played: games.length,
      avg: scores.length ? Math.round(scores.reduce((a, b) => a + b, 0) / scores.length) : 0,
      top: scores.length ? Math.max(...scores) : 0,
      streak,
    };
  }

  function drawSummary() {
    roundLayers.clearLayers();
    const bounds = L.latLngBounds([]);
    game.rounds.forEach((r, n) => {
      if (!r.guess || !r.point) return;                 // saved by the first version: score only
      const loc = locOf(r);
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
  let reloadAt = null;   // today's puzzle page flips to the new puzzle just after midnight
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
    const missed = !IS_ARCHIVE && DATA.schedule[yesterday] && dayNumber(yesterday) >= 1 && !(loadGame(yesterday) || {}).done
      ? `<a class="archive-link" href="?date=${yesterday}">Missed yesterday? Play #${dayNumber(yesterday)} →</a>` : "";
    const back = IS_ARCHIVE ? '<a class="archive-link" href="./">Back to today’s puzzle →</a>' : "";
    const fill = (url) => url
      .replace("{puzzle}", encodeURIComponent(`${dayLabel(DATE)} · ${DATE}`))
      .replace("{places}", encodeURIComponent(todaysIds.map((i) => DATA.locations[i].name).join(" · ")))
      .replace("{device}", encodeURIComponent(navigator.userAgent));
    const fb = CFG.feedback || {};
    const link = (kind, label) => (fb.key
      ? `<a href="#" data-feedback="${kind}">${label}</a>`
      : fb[kind] && `<a href="${esc(fill(fb[kind]))}" target="_blank" rel="noopener">${label}</a>`);
    const fbLinks = [link("place", "Suggest a place"), link("bug", "Report a bug")].filter(Boolean);
    const feedback = fbLinks.length ? `<p class="feedback">${fbLinks.join(" · ")}</p>` : "";

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
      "</div>" + missed + back + feedback;
    if (fresh) countUp(document.getElementById("final-n"), score);

    cardBody.querySelectorAll("[data-feedback]").forEach((a) => {
      a.onclick = (e) => {
        e.preventDefault();
        openFeedback(a.dataset.feedback, {
          puzzle: `${dayLabel(DATE)} · ${DATE}`,
          places: todaysIds.map((i) => DATA.locations[i].name),
        });
      };
    });

    // tap a row to fly to that round
    cardBody.querySelectorAll(".breakdown li").forEach((li) => {
      li.onclick = () => {
        const r = game.rounds[+li.dataset.n];
        if (!r.guess || !r.point) return;
        const loc = locOf(r);
        const b = L.latLngBounds([r.guess, r.point]);
        loc.geometry.forEach((p) => b.extend(p));
        frame(b, { maxZoom: 11 });
      };
    });

    const shareBtn = document.getElementById("share");
    shareBtn.onclick = async () => {
      const text = shareText();
      hit(`/share/${dayNumber(DATE) >= 1 ? dayNumber(DATE) : "practice"}`, `Shared ${dayLabel(DATE)}`, true);
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
    const midnight = new Date(); midnight.setHours(24, 0, 0, 0);
    clearInterval(tick);
    const upd = () => {
      const s = Math.max(0, Math.floor((midnight - new Date()) / 1000));
      cd.textContent = [Math.floor(s / 3600), Math.floor(s / 60) % 60, s % 60]
        .map((n) => String(n).padStart(2, "0")).join(":");
    };
    upd();
    tick = setInterval(upd, 1000);
    if (!IS_ARCHIVE && !reloadAt) reloadAt = setTimeout(() => location.reload(), midnight - new Date() + 1500);
  }

  // ---- go: finished → summary; otherwise the next unplayed round (locked guesses stay locked) ----
  resetView();
  if (game.done) renderFinal(false);
  else startRound();
  hit(IS_ARCHIVE ? "/archive" : "/", `pnwtap ${dayLabel(DATE)}`);
})();
