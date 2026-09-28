(function () {
  "use strict";

  const DATA = window.PNWTAP;
  const CFG = DATA.config;

  const cardBody = document.getElementById("card-body");
  const roundPill = document.getElementById("round-pill");
  const setPill = (t) => { roundPill.textContent = t; };

  // ---- today's puzzle ----
  function todayISO() {
    const d = new Date();
    const p = (n) => String(n).padStart(2, "0");
    return `${d.getFullYear()}-${p(d.getMonth() + 1)}-${p(d.getDate())}`;
  }
  const DATE = todayISO();
  const todaysIds = DATA.schedule[DATE];

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

  // ---- map: coloured terrain + shaded-relief overlay, locked to the region ----
  const bb = CFG.bbox; // [minLat, minLng, maxLat, maxLng]
  const MASK = DATA.regionMask || [];       // region-shaped stencil rings ([lat,lng])

  // Bounds of the play region: the mask's extent if present, else the bbox.
  let regionBounds = L.latLngBounds([bb[0], bb[1]], [bb[2], bb[3]]);
  if (MASK.length) {
    regionBounds = L.latLngBounds(MASK[0]);
    MASK.forEach((ring) => ring.forEach((pt) => regionBounds.extend(pt)));
  }

  const map = L.map("map", {
    minZoom: CFG.minZoom,
    maxZoom: CFG.maxZoom,
    maxBounds: regionBounds.pad(0.35),   // roomy to roam, but not infinitely
    maxBoundsViscosity: 0.25,            // soft edge
    zoomControl: false,
  }).setView(CFG.center, CFG.zoom);
  L.control.zoom({ position: "bottomleft" }).addTo(map);

  // `bounds` clips tile loading to the region box — the stencil below hides
  // the rectangular corners, and anywhere with no tiles shows #map's colour.
  L.tileLayer(CFG.tileUrl, {
    attribution: CFG.tileAttribution,
    bounds: regionBounds,
    noWrap: true,                        // don't repeat the imagery east–west
    minZoom: CFG.minZoom,
    maxZoom: CFG.maxZoom,
  }).addTo(map);

  if (CFG.hillshadeUrl) {
    map.createPane("hillshade");
    const pane = map.getPane("hillshade");
    pane.style.zIndex = 250;                 // above base tiles, below markers
    pane.classList.add("hillshade-pane");    // blends via CSS
    L.tileLayer(CFG.hillshadeUrl, { pane: "hillshade", maxZoom: CFG.maxZoom }).addTo(map);
  }

  // Stencil: fill a region-sized rectangle with the frame colour, punching
  // region-shaped holes so only WA / OR / BC / AB / YT show through in imagery.
  // Outside the rectangle, #map's background is the same colour, so it's seamless.
  // The mask lives in the default overlay pane (added before roundLayers, so the
  // reveal line/markers draw over it) and uses a padded renderer so it stays
  // rendered — and animates in lockstep with the tiles — during zoom.
  if (MASK.length) {
    const maskRenderer = L.svg({ padding: 3 });
    // a wide outer ring (well past any viewport) with clamped latitude; the
    // renderer clips rasterisation to near the view, so this stays cheap
    const outN = Math.min(85, regionBounds.getNorth() + 25);
    const outS = Math.max(-85, regionBounds.getSouth() - 25);
    const outW = regionBounds.getWest() - 50;
    const outE = regionBounds.getEast() + 50;
    const outer = [[outN, outW], [outN, outE], [outS, outE], [outS, outW]];
    // frame fill with region-shaped holes (no stroke, so the rectangle is invisible)
    L.polygon([outer].concat(MASK), {
      renderer: maskRenderer, stroke: false,
      fill: true, fillColor: "#2b352e", fillOpacity: 1, interactive: false,
    }).addTo(map);
    // trace just the region outline in a soft tan
    L.polygon(MASK, {
      renderer: maskRenderer, fill: false,
      stroke: true, color: "#e2c48b", weight: 1, opacity: 0.5, interactive: false,
    }).addTo(map);
  }

  const roundLayers = L.layerGroup().addTo(map);

  const guessIcon = L.divIcon({
    className: "guess-marker",
    html: '<span class="guess-dot"></span>',
    iconSize: [22, 22], iconAnchor: [11, 11],
  });
  const answerIcon = () => L.divIcon({
    className: "answer-marker",
    html: '<span class="answer-ring"></span><span class="answer-dot"></span>',
    iconSize: [22, 22], iconAnchor: [11, 11],
  });

  // ---- state ----
  const results = [];       // {score, mult, difficulty, name}
  let roundIdx = 0;
  let tapMarker = null;
  let tapLatLng = null;

  if (!todaysIds) {
    setPill("");
    cardBody.innerHTML = '<p class="msg">No puzzle scheduled for today — check back another day!</p>';
    return;
  }

  function resetRoundLayers() {
    roundLayers.clearLayers();
    tapMarker = null;
    tapLatLng = null;
  }

  // ---- guess view ----
  function renderGuess(loc) {
    setPill(`${roundIdx + 1} / ${todaysIds.length}`);
    const ask = loc.image
      ? '<p class="ask">Tap as close as you can to <strong>this place</strong>.</p>' +
        `<img class="prompt-img" src="${loc.image}" alt="Where is this?">`
      : `<p class="ask">Tap as close as you can to <strong>${loc.name}</strong>.</p>`;
    cardBody.innerHTML = ask + '<button id="lock" disabled>Lock in guess</button>';
    const lockBtn = document.getElementById("lock");

    function onClick(e) {
      tapLatLng = [e.latlng.lat, e.latlng.lng];
      if (!tapMarker) {
        tapMarker = L.marker(e.latlng, { icon: guessIcon, draggable: true }).addTo(roundLayers);
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

  function startRound() {
    resetRoundLayers();
    map.setView(CFG.center, CFG.zoom, { animate: false });
    renderGuess(DATA.locations[todaysIds[roundIdx]]);
  }

  // ---- reveal: MapTap-style line that draws from the guess to the truth ----
  function animateReveal(from, loc, nearPt) {
    // outline linear features (rivers/roads/traverses); mark the true point
    if (loc.geometry.length > 1) {
      L.polyline(loc.geometry, { color: "#c0392b", weight: 4, opacity: 0.9 }).addTo(roundLayers);
    }
    L.marker(nearPt, { icon: answerIcon(), interactive: false, zIndexOffset: 1000 }).addTo(roundLayers);

    // the connector, starting as a zero-length line at the guess
    const line = L.polyline([from, from], {
      color: "#2f523e", weight: 4, opacity: 0.95, lineCap: "round",
    }).addTo(roundLayers);

    // frame both points, THEN grow the line once the map has settled
    const bounds = L.latLngBounds([from, nearPt]);
    if (loc.geometry.length > 1) loc.geometry.forEach((p) => bounds.extend(p));
    map.flyToBounds(bounds.pad(0.45), { duration: 0.7, maxZoom: 10 });

    setTimeout(function grow() {
      const startT = performance.now();
      const DUR = 700;
      (function frame(now) {
        const t = Math.min(1, (now - startT) / DUR);
        const e = 1 - Math.pow(1 - t, 3);   // easeOutCubic
        line.setLatLngs([from, [
          from[0] + (nearPt[0] - from[0]) * e,
          from[1] + (nearPt[1] - from[1]) * e,
        ]]);
        if (t < 1) requestAnimationFrame(frame);
      })(performance.now());
    }, 720);
  }

  // ---- result view (replaces the guess view in the same card) ----
  function renderResult(loc, dist, score, mult, last) {
    setPill(`${roundIdx + 1} / ${todaysIds.length}`);
    const tier = CFG.emoji[loc.difficulty] || "";
    cardBody.innerHTML =
      `<p class="result-name">${loc.name} <span class="tier">${tier}</span></p>` +
      `<p class="result-score"><b>${Math.round(dist)} km</b> off · ` +
        `<b>${score}</b> × ${mult} = <span class="pts">${score * mult}</span></p>` +
      (loc.image ? `<img class="reveal-img" src="${loc.image}" alt="">` : "") +
      (loc.blurb ? `<p class="reveal-blurb">${loc.blurb}</p>` : "") +
      `<button id="next">${last ? "See results" : "Next round"}</button>`;
    document.getElementById("next").onclick = () => {
      roundIdx += 1;
      if (roundIdx < todaysIds.length) startRound();
      else finish();
    };
  }

  function lockRound(loc) {
    const dist = nearestKm(tapLatLng, loc.geometry);
    const score = scoreFor(dist);
    const mult = CFG.multipliers[roundIdx];
    results.push({ score, mult, difficulty: loc.difficulty, name: loc.name });

    const nearPt = nearestPointOnPath(tapLatLng, loc.geometry);
    animateReveal(tapLatLng, loc, nearPt);
    renderResult(loc, dist, score, mult, roundIdx === todaysIds.length - 1);
  }

  // ---- finish / share ----
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
    renderFinal();
  }

  function renderFinal() {
    resetRoundLayers();
    setPill("");
    map.flyTo(CFG.center, CFG.zoom, { duration: 0.6 });
    const total = results.reduce((s, r) => s + r.score * r.mult, 0);
    const share = shareString();
    cardBody.innerHTML =
      '<p class="final">Final score</p>' +
      `<div class="final-score">${total} <span>/ 1000</span></div>` +
      `<pre id="share">${share}</pre>` +
      '<button id="copy">Copy result</button>';
    const copyBtn = document.getElementById("copy");
    copyBtn.onclick = () => {
      navigator.clipboard.writeText(share)
        .then(() => { copyBtn.textContent = "Copied!"; })
        .catch(() => { copyBtn.textContent = "Select the text above to copy"; });
    };
  }

  // ---- resume if already played today ----
  const saved = localStorage.getItem("pnwtap:" + DATE);
  if (saved) {
    results.push(...JSON.parse(saved));
    renderFinal();
  } else {
    startRound();
  }
})();
