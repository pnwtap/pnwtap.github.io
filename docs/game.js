(function () {
  "use strict";

  const DATA = window.PNWTAP;
  const CFG = DATA.config;

  const statusEl = document.getElementById("status");
  const promptEl = document.getElementById("prompt");
  const controlsEl = document.getElementById("controls");
  const revealEl = document.getElementById("reveal");

  // ---- today's puzzle ----
  function todayISO() {
    const d = new Date();
    const p = (n) => String(n).padStart(2, "0");
    return `${d.getFullYear()}-${p(d.getMonth() + 1)}-${p(d.getDate())}`;
  }
  const DATE = todayISO();
  const todaysIds = DATA.schedule[DATE];

  if (!todaysIds) {
    statusEl.textContent = "No puzzle scheduled for today — check back another day!";
    return;
  }

  // ---- scoring math (mirrors pnwtap/geometry.py) ----
  const R = 6371.0088;
  const rad = (x) => (x * Math.PI) / 180;

  function haversine(a, b) {
    const dphi = rad(b[0] - a[0]);
    const dlmb = rad(b[1] - a[1]);
    const h = Math.sin(dphi / 2) ** 2 +
      Math.cos(rad(a[0])) * Math.cos(rad(b[0])) * Math.sin(dlmb / 2) ** 2;
    return 2 * R * Math.asin(Math.min(1, Math.sqrt(h)));
  }
  function project(origin, pt) {
    return [
      rad(pt[1] - origin[1]) * Math.cos(rad(origin[0])) * R,
      rad(pt[0] - origin[0]) * R,
    ];
  }
  function segDist(tap, a, b) {
    const [ax, ay] = project(tap, a);
    const [bx, by] = project(tap, b);
    const dx = bx - ax, dy = by - ay;
    if (dx === 0 && dy === 0) return Math.hypot(ax, ay);
    let t = -(ax * dx + ay * dy) / (dx * dx + dy * dy);
    t = Math.max(0, Math.min(1, t));
    return Math.hypot(ax + t * dx, ay + t * dy);
  }
  function nearestKm(tap, path) {
    if (path.length === 1) return haversine(tap, path[0]);
    let best = Infinity;
    for (let i = 0; i < path.length - 1; i++) {
      best = Math.min(best, segDist(tap, path[i], path[i + 1]));
    }
    return best;
  }
  function unproject(origin, x, y) {
    const lat = origin[0] + (y / R) * 180 / Math.PI;
    const lng = origin[1] + (x / (R * Math.cos(rad(origin[0])))) * 180 / Math.PI;
    return [lat, lng];
  }
  function nearestPointOnPath(tap, path) {
    if (path.length === 1) return path[0];
    let best = Infinity;
    let bestPt = path[0];
    for (let i = 0; i < path.length - 1; i++) {
      const [ax, ay] = project(tap, path[i]);
      const [bx, by] = project(tap, path[i + 1]);
      const dx = bx - ax, dy = by - ay;
      let cx, cy;
      if (dx === 0 && dy === 0) {
        cx = ax; cy = ay;
      } else {
        let t = -(ax * dx + ay * dy) / (dx * dx + dy * dy);
        t = Math.max(0, Math.min(1, t));
        cx = ax + t * dx; cy = ay + t * dy;
      }
      const d = Math.hypot(cx, cy);
      if (d < best) { best = d; bestPt = unproject(tap, cx, cy); }
    }
    return bestPt;
  }
  const scoreFor = (distKm) => Math.round(100 * Math.exp(-distKm / CFG.D_km));

  // ---- map ----
  const map = L.map("map", { minZoom: 4, maxZoom: 12 }).setView(CFG.center, CFG.zoom);
  L.tileLayer(CFG.tileUrl, { attribution: CFG.tileAttribution }).addTo(map);
  const roundLayers = L.layerGroup().addTo(map);

  // ---- state ----
  const results = [];       // {score, mult, difficulty, name}
  let roundIdx = 0;
  let tapMarker = null;
  let tapLatLng = null;

  function resetRoundLayers() {
    roundLayers.clearLayers();
    tapMarker = null;
    tapLatLng = null;
  }

  function showPrompt(loc) {
    const head = `<div class="round-no">Round ${roundIdx + 1} of ${todaysIds.length}</div>`;
    const body = loc.image
      ? `<img class="prompt-img" src="${loc.image}" alt="Where is this?">`
      : `<div class="prompt-name">${loc.name}</div>`;
    promptEl.innerHTML = `${head}${body}<div class="prompt-cap">Tap the map where you think this is.</div>`;
  }

  function startRound() {
    resetRoundLayers();
    revealEl.hidden = true;
    revealEl.innerHTML = "";
    const loc = DATA.locations[todaysIds[roundIdx]];
    showPrompt(loc);
    controlsEl.innerHTML = `<button id="lock" disabled>Lock in guess</button>`;
    const lockBtn = document.getElementById("lock");

    function onClick(e) {
      tapLatLng = [e.latlng.lat, e.latlng.lng];
      if (!tapMarker) {
        tapMarker = L.marker(e.latlng, { draggable: true }).addTo(roundLayers);
        tapMarker.on("dragend", () => {
          const p = tapMarker.getLatLng();
          tapLatLng = [p.lat, p.lng];
        });
      } else {
        tapMarker.setLatLng(e.latlng);
      }
      lockBtn.disabled = false;
    }
    map.on("click", onClick);

    lockBtn.onclick = () => {
      if (!tapLatLng) return;
      map.off("click", onClick);
      if (tapMarker && tapMarker.dragging) tapMarker.dragging.disable();
      lockRound(loc);
    };
  }

  function lockRound(loc) {
    const dist = nearestKm(tapLatLng, loc.geometry);
    const score = scoreFor(dist);
    const mult = CFG.multipliers[roundIdx];
    results.push({ score, mult, difficulty: loc.difficulty, name: loc.name });

    if (loc.geometry.length === 1) {
      L.circleMarker(loc.geometry[0], { radius: 8, color: "#c0392b", fillColor: "#c0392b", fillOpacity: 0.9 }).addTo(roundLayers);
    } else {
      L.polyline(loc.geometry, { color: "#c0392b", weight: 4 }).addTo(roundLayers);
    }
    const nearPt = nearestPointOnPath(tapLatLng, loc.geometry);
    L.polyline([tapLatLng, nearPt], { color: "#333", weight: 2, dashArray: "4 6" }).addTo(roundLayers);

    const last = roundIdx === todaysIds.length - 1;
    revealEl.hidden = false;
    revealEl.innerHTML =
      `<div class="reveal-name">${loc.name}</div>` +
      `<div class="reveal-score">${Math.round(dist)} km off · <strong>${score}</strong> × ${mult} = ${score * mult}</div>` +
      (loc.image ? `<img class="reveal-img" src="${loc.image}" alt="">` : "") +
      (loc.blurb ? `<p class="reveal-blurb">${loc.blurb}</p>` : "") +
      `<button id="next">${last ? "See results" : "Next round"}</button>`;
    document.getElementById("next").onclick = () => {
      roundIdx += 1;
      if (roundIdx < todaysIds.length) startRound();
      else finish();
    };
  }

  function prettyDate() {
    const months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"];
    const d = new Date(DATE + "T00:00:00");
    return `${months[d.getMonth()]} ${d.getDate()}`;
  }
  function shareString() {
    const parts = results.map((r) => `${r.score}${CFG.emoji[r.difficulty]}`);
    const total = results.reduce((s, r) => s + r.score * r.mult, 0);
    return `pnwtap ${prettyDate()} · ${parts.join(" ")} · Final ${total}`;
  }

  function finish() {
    localStorage.setItem("pnwtap:" + DATE, JSON.stringify(results));
    renderResults();
  }

  function renderResults() {
    resetRoundLayers();
    revealEl.hidden = true;
    const total = results.reduce((s, r) => s + r.score * r.mult, 0);
    promptEl.innerHTML = `<div class="prompt-name">Final score: ${total} / 1000</div>`;
    const share = shareString();
    controlsEl.innerHTML = `<pre id="share">${share}</pre><button id="copy">Copy result</button>`;
    document.getElementById("copy").onclick = () => {
      navigator.clipboard.writeText(share);
      document.getElementById("copy").textContent = "Copied!";
    };
  }

  // ---- resume if already played today ----
  const saved = localStorage.getItem("pnwtap:" + DATE);
  if (saved) {
    results.push(...JSON.parse(saved));
    renderResults();
  } else {
    startRound();
  }
})();
