(function () {
  "use strict";

  const DATA = window.PNWTAP;
  const CFG = DATA.config;
  const S = window.PNWTAP_SCORING;
  // geometry arrives polyline-encoded; decode it once, up front, so every consumer
  // (scoring, reveal, playtest, results) sees plain [lat, lng] arrays
  DATA.locations.forEach((l) => {
    if (typeof l.geometry === "string") l.geometry = S.decode(l.geometry);
    (l.members || []).forEach((m) => { if (typeof m.geometry === "string") m.geometry = S.decode(m.geometry); });
  });
  DATA.regionMask = (DATA.regionMask || []).map((r) => (typeof r === "string" ? S.decode(r) : r));

  const card = document.getElementById("card");
  const cardBody = document.getElementById("card-body");
  const roundPill = document.getElementById("round-pill");
  const puzzleNo = document.getElementById("puzzle-no");
  const helpBtn = document.getElementById("help-btn");
  const setPill = (t) => { roundPill.textContent = t; };
  const reducedMotion = () => window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  // ---- phones: the card is a bottom sheet. Drag its header down to tuck it away (up to
  // bring it back; a tap toggles). While tucked away the header carries the card's main
  // button, so a whole round can be played with the full map in view. New content
  // (a reveal, the next round, the results) brings the sheet back up.
  const head = document.getElementById("card-head");
  const headAction = document.getElementById("head-action");
  const PHONE = window.matchMedia("(max-width: 640px)");
  const isPhone = () => PHONE.matches;
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
  function dragEnd(e) {
    if (dragY === null) return;
    dragY = null;
    const collapsed = card.classList.contains("collapsed");
    let next = collapsed;
    if (e.type !== "pointercancel") {                       // a system gesture resets without toggling
      if (!dragMoved) next = !collapsed;                     // a tap
      else if (!collapsed && dragDy > 40) next = true;       // swiped down
      else if (collapsed && dragDy < -20) next = false;      // swiped up
    }
    if (next === collapsed) {                                // no change: ease back into place
      card.classList.remove("dragging");
      card.style.transform = "";
      return;
    }
    card.style.transform = "";                               // change: land in one frame, no transition
    setCollapsed(next);
    void card.offsetHeight;
    card.classList.remove("dragging");
    // Android sends the tap's click to whatever is under the finger *after* the sheet moved
    // (the map, or the main button): swallow it
    const eat = (ev) => { ev.preventDefault(); ev.stopImmediatePropagation(); };
    window.addEventListener("click", eat, { capture: true, once: true });
    setTimeout(() => window.removeEventListener("click", eat, true), 400);
  }
  head.addEventListener("pointerup", dragEnd);
  head.addEventListener("pointercancel", dragEnd);
  // backstop for any content swap that doesn't go through setBody()
  new MutationObserver(() => setCollapsed(false)).observe(cardBody, { childList: true });
  new MutationObserver(syncHeadAction).observe(cardBody, { subtree: true, childList: true, attributes: true, characterData: true });

  // Replace the card's content. Expand the sheet first, so anything measured afterwards
  // (map framing) sees the real sheet and focus() lands on a visible element.
  let armedAt = 0;
  function setBody(html) {
    setCollapsed(false);
    cardBody.innerHTML = html;
    cardBody.scrollTop = 0;
    armedAt = performance.now() + 350;
    moreBelow();
  }
  // .more while there's content below the fold (behind the sticky main button): it fades
  // out above the button, so the card reads as scrollable
  const moreBelow = () => cardBody.classList.toggle("more",
    cardBody.scrollHeight - cardBody.scrollTop - cardBody.clientHeight > 2);
  cardBody.addEventListener("scroll", moreBelow, { passive: true });
  window.addEventListener("resize", moreBelow);
  // the second tap of a quick double tap would hit the main button that just replaced
  // the first one (Lock in → Next round): swallow those for a moment after a swap
  card.addEventListener("click", (e) => {
    if (performance.now() < armedAt && e.isTrusted && e.target.closest("button.primary, #head-action")) {
      e.preventDefault();
      e.stopImmediatePropagation();
    }
  }, true);
  document.addEventListener("touchstart", () => {}, { passive: true });   // lets iOS show :active

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

  // One puzzle day for everyone: the game's clock (Pacific), whatever the device's zone.
  const TZ = CFG.timeZone || "America/Los_Angeles";
  const today = () => { try { return S.dayIn(Date.now(), TZ); } catch (e) { return iso(new Date()); } };
  const dayBegins = (d) => { try { return S.dayStart(d, TZ); } catch (e) { return parseISO(d).getTime(); } };
  const TODAY = today();
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
  const MASK = DATA.regionMask;
  const bb = CFG.bbox; // [minLat, minLng, maxLat, maxLng]
  let regionBounds = L.latLngBounds([bb[0], bb[1]], [bb[2], bb[3]]);
  if (MASK.length) {
    regionBounds = L.latLngBounds(MASK[0]);
    MASK.forEach((ring) => ring.forEach((pt) => regionBounds.extend(pt)));
  }
  const startBounds = L.latLngBounds(CFG.startBounds);

  // How far the view may roam: the region plus a margin. On phones the bottom sheet hides
  // the bottom of the map, so a southern answer needs room below the region to be lifted
  // above it (otherwise Leaflet pans back once a flight lands) — as much room as the sheet
  // covers right now, in screen pixels at the zoom in use. No more: extra room lets a pinch
  // or a fling park the view south of the region, over nothing but the dark frame.
  const baseRoam = regionBounds.pad(0.35);
  let sheetCover = 0;
  const measureSheet = () => {
    sheetCover = isPhone() ? Math.min(card.offsetHeight, window.innerHeight - 140) + 40 : 0;
  };
  measureSheet();
  function roamFor(zoom, cover = sheetCover) {
    if (!cover) return baseRoam;
    const crs = L.CRS.EPSG3857;
    const p = crs.latLngToPoint(L.latLng(regionBounds.getSouth(), baseRoam.getWest()), zoom);
    p.y += cover;
    return L.latLngBounds([Math.min(baseRoam.getSouth(), crs.pointToLatLng(p, zoom).lat), baseRoam.getWest()],
      baseRoam.getNorthEast());
  }

  const map = L.map("map", {
    minZoom: CFG.minZoom,
    maxZoom: CFG.maxZoom,
    maxBounds: roamFor(CFG.minZoom),
    maxBoundsViscosity: 0.25,
    zoomControl: false,
    attributionControl: false,
    zoomSnap: 0.25,
    fadeAnimation: false,   // cached tiles appear at once (a new round no longer fades in from dark)
    tapHold: false,         // iOS: a long, careful press still places the pin
    bounceAtZoomLimits: false,   // pinching past the widest view just stops (no dark speck-and-snap)
  });
  const setRoam = (zoom) => { map.options.maxBounds = roamFor(zoom); };   // read at drag start and moveend
  map.on("zoom", () => setRoam(map.getZoom()));
  // the sheet grows, shrinks, tucks away: the room below the region follows
  if (window.ResizeObserver) new ResizeObserver(() => { measureSheet(); if (map._loaded) setRoam(map.getZoom()); }).observe(card);
  // zoom buttons on larger screens (phones pinch); the attribution clear of the card
  const zoomCtl = L.control.zoom({ position: "bottomright" });
  const attrCtl = L.control.attribution({ prefix: false }).addAttribution(CFG.tileAttribution).addTo(map);
  const placeControls = () => {
    attrCtl.setPosition(isPhone() ? "topright" : "bottomright");
    if (isPhone()) zoomCtl.remove(); else if (!zoomCtl._map) zoomCtl.addTo(map);
  };
  placeControls();

  const tiles = L.tileLayer(CFG.tileUrl, {
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
    const maskRenderer = L.svg({ padding: 1 });
    const outN = Math.min(85, regionBounds.getNorth() + 25);
    const tallest = Math.max(window.innerHeight, window.screen.height || 0);   // any sheet, either orientation
    const outS = Math.max(-85, Math.min(regionBounds.getSouth() - 25, roamFor(CFG.minZoom, tallest).getSouth() - 5));
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
    // Leaflet redraws an SVG layer only at moveend; mid-flight, mid-pinch and mid-fling it
    // just transforms the old drawing, which a modestly padded layer would run out of.
    // Redraw it whenever the view drifts a zoom level or half a screen from where it was
    // drawn. (_reset/_center/_zoom are Leaflet 1.9.4 internals; Leaflet is pinned.)
    map.on("zoom move", () => {
      const r = maskRenderer;
      if (!r._map || r._zoom === undefined || map._animatingZoom) return;
      const z = map.getZoom(), size = map.getSize();
      const drift = map.project(r._center, z).distanceTo(map.project(map.getCenter(), z));
      if (Math.abs(z - r._zoom) > 0.9 || drift > 0.5 * Math.min(size.x, size.y)) r._reset();
    });
  }

  const roundLayers = L.layerGroup().addTo(map);
  let revealSeq = 0;              // bumped whenever the round's layers are replaced
  const cancelReveal = () => { revealSeq++; };

  const guessIcon = (label) => L.divIcon({
    className: "guess-marker",
    html: `<span class="guess-dot">${label || ""}</span>`,
    iconSize: [22, 22], iconAnchor: [11, 11],
  });
  const answerIcon = (pulse, minor) => L.divIcon({
    className: "answer-marker" + (minor ? " minor" : ""),
    html: (pulse ? '<span class="answer-ring"></span>' : "") + '<span class="answer-dot"></span>',
    iconSize: [22, 22], iconAnchor: [11, 11],
  });

  // Keep revealed features clear of the card. Measures the layout box (offset*), not the
  // painted rect, so an entrance animation or a drag in progress can't skew it.
  function framePadding() {
    const H = window.innerHeight, W = window.innerWidth, m = 36;
    const controls = isPhone() ? [m, m] : [m + 40, m + 24];  // keep clear of zoom buttons + attribution
    if (isPhone()) {                                        // bottom sheet; attribution sits top-right
      const covered = Math.min(card.offsetHeight, H - 140); // always leave some map
      return { paddingTopLeft: [m, m + 12], paddingBottomRight: [m, covered + m] };
    }
    const right = card.offsetLeft + card.offsetWidth;
    if (right < W / 2) return { paddingTopLeft: [right + m, m], paddingBottomRight: controls };   // docked
    const covered = Math.min(card.offsetTop + card.offsetHeight, H - 140);                        // floating top card
    return { paddingTopLeft: [m, covered + m], paddingBottomRight: controls };
  }
  // a page opened in a background tab can have a 0×0 map, where fitting bounds yields NaN
  const sized = () => map.getSize().x > 0 && map.getSize().y > 0;
  // Leaflet ignores a new view while a zoom animation (a quick hop, a double-tap or pinch
  // snap) is still running: finish it first. (Leaflet 1.9.4 internals.)
  const settle = () => { if (map._animatingZoom) map._onZoomTransitionEnd(); };
  let lastFrame = null;           // what moveTo last framed (null: the start view), for re-framing
  const resetView = () => {
    settle();
    lastFrame = null;
    if (sized()) map.fitBounds(startBounds, Object.assign(framePadding(), { animate: false }));
    else map.setView(startBounds.getCenter(), 5, { animate: false });
  };

  // Ask for the tiles of a view before the camera gets there, so it lands on sharp imagery.
  // Same URLs and (no-)CORS mode as the tile layer, so its own requests hit the cache.
  const prefetched = new Set();
  function prefetchTiles(center, zoom) {
    try {
      const tz = Math.max(CFG.minZoom, Math.min(CFG.maxZoom, Math.round(zoom)));
      const c = map.project(center, tz).floor();
      const half = map.getSize().divideBy(2 * map.getZoomScale(zoom, tz));
      const lo = c.subtract(half), hi = c.add(half), T = 256;
      for (let x = Math.floor(lo.x / T); x <= Math.ceil(hi.x / T) - 1; x++) {
        for (let y = Math.floor(lo.y / T); y <= Math.ceil(hi.y / T) - 1; y++) {
          const box = L.latLngBounds(map.unproject([x * T, y * T], tz), map.unproject([(x + 1) * T, (y + 1) * T], tz));
          if (!regionBounds.intersects(box)) continue;      // the tile layer never asks for these
          const im = new Image();
          im.fetchPriority = "high";
          im.onload = im.onerror = () => prefetched.delete(im);   // hold a reference until done
          prefetched.add(im);
          im.src = L.Util.template(CFG.tileUrl, { x, y, z: tz, s: "", r: "" });
        }
      }
    } catch (e) { /* only an optimisation */ }
  }

  // On phones, a zoom-in flight would otherwise request (and then cancel) a whole tile
  // level at every zoom it passes through. When the destination is already on screen,
  // skip the in-between levels: the start tiles scale up and the prefetched ones land.
  // Returns the undo, which runs at moveend or when moveTo gives up waiting for one (a
  // gesture can stop a flight without a moveend).
  function levelHopping(targetZoom, bounds) {
    const dz = Math.round(targetZoom) - Math.round(map.getZoom());
    const skip = L.Browser.mobile && dz >= 2 && dz <= 5 && map.getBounds().contains(bounds);
    tiles.options.updateWhenZooming = !skip;
    if (!skip) return null;
    const restore = () => {
      map.off("moveend", restore);
      if (tiles.options.updateWhenZooming) return;
      tiles.options.updateWhenZooming = true;
      const want = Math.max(CFG.minZoom, Math.min(CFG.maxZoom, Math.round(map.getZoom())));
      if (tiles._tileZoom !== want) tiles._resetView();     // Leaflet 1.9.4 internal: re-sync the level
    };
    map.on("moveend", restore);
    return restore;
  }

  // Move the camera to show `bounds`, then call onArrive once. Already framed: no move.
  // A short hop: Leaflet's quick (~250 ms) zoom/pan. Otherwise a flight scaled to the
  // distance (≤ 0.6 s). { animate: false } cuts straight there.
  function moveTo(bounds, opts, onArrive) {
    let arrived = false, timer = null, restore = null;
    const done = () => {
      if (arrived) return;
      arrived = true;
      clearTimeout(timer);
      map.off("moveend", done);
      if (restore) restore();
      if (onArrive) onArrive();
    };
    settle();
    lastFrame = { bounds, opts };
    if (!sized()) { map.setView(bounds.getCenter(), 6, { animate: false }); return done(); }
    const o = Object.assign(framePadding(), { maxZoom: 10 }, opts);
    const t = map._getBoundsCenterZoom(bounds, o);           // Leaflet 1.9.4 internal: flyToBounds' target
    measureSheet();                                          // the sheet as it is now (just refilled)
    setRoam(Math.min(t.zoom, map.getZoom() || t.zoom));      // the looser of the two, until the zoom lands
    if (!map._loaded || o.animate === false || reducedMotion()) {
      map.setView(t.center, t.zoom, { animate: false });
      return done();
    }
    prefetchTiles(t.center, t.zoom);
    const z0 = map.getZoom(), size = map.getSize();
    const offset = map.project(t.center, z0).distanceTo(map.project(map.getCenter(), z0));
    const dz = Math.abs(t.zoom - z0);
    if (dz < 0.25 && offset < 2) return done();
    let ms;
    if (dz <= 2 && offset < Math.max(size.x, size.y)) {
      ms = 300;
      map.setView(t.center, t.zoom, { animate: true });
    } else {
      const secs = Math.min(0.6, 0.3 + 0.06 * dz);
      ms = secs * 1000;
      restore = levelHopping(t.zoom, bounds);
      map.flyTo(t.center, t.zoom, { duration: secs });
    }
    map.on("moveend", done);
    timer = setTimeout(done, ms + 300);   // a touch mid-flight cancels it without a moveend
  }

  // Rotation or a resize that switches layout (bottom sheet / docked card / top card):
  // move the controls, and re-frame a revealed answer so it isn't left under the card.
  // (The ask phase keeps the player's own pan and zoom.)
  function onLayout() {
    if (!isPhone()) setCollapsed(false);    // the tucked-away state only exists on phones
    measureSheet();
    placeControls();
    requestAnimationFrame(() => {
      map.invalidateSize(false);
      if (lastFrame) moveTo(lastFrame.bounds, Object.assign({}, lastFrame.opts, { animate: false }));
    });
  }
  ["(max-width: 640px)", "(min-width: 641px) and (max-width: 999px) and (max-height: 500px)", "(min-width: 1000px)"]
    .forEach((q) => {
      const mq = window.matchMedia(q);
      if (mq.addEventListener) mq.addEventListener("change", onLayout); else mq.addListener(onLayout);
    });

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
  // Every place as a list of targets: one for most, several for an "any of" place (any
  // growing glacier...), where a tap scores by the nearest.
  const targets = (loc) => loc.members || [{ name: null, geometry: loc.geometry, kind: loc.kind }];
  const targetOf = (loc, mi) => targets(loc)[mi] || targets(loc)[0];
  // which member a saved round hit: by name (a member list can be reordered after the
  // day is played), else by index, else whichever the stored answer point lies on
  const miOf = (loc, r) => {
    if (!loc.members) return 0;
    const k = loc.members.findIndex((m) => m.name === r.member);
    return k >= 0 ? k : loc.members[r.mi] ? r.mi : nearestTo(loc, r.point).mi;
  };
  function nearestTo(loc, tap) {
    const ts = targets(loc);
    const n = S.nearestAny(tap, ts.map((t) => ({ geometry: t.geometry, area: t.kind === "area" })));
    return { km: n.km, point: n.point, mi: n.index, member: ts[n.index].name };
  }
  // "Nearest of 2: Crater Glacier · also Hubbard Glacier" under an "any of" result (a big
  // set: "· and 36 others")
  const memberLine = (loc, mi) => {
    if (!loc.members) return "";
    const others = loc.members.filter((m, k) => k !== mi).map((m) => esc(m.name));
    const rest = others.length > 4 ? ` · and ${others.length} others` : others.length ? ` · also ${others.join(", ")}` : "";
    return `<p class="result-member">Nearest of ${loc.members.length}: <b>${esc(targetOf(loc, mi).name)}</b>${rest}</p>`;
  };

  // ---- scoring helpers ----
  const total = (rounds) => rounds.reduce((s, r) => s + r.score * r.mult, 0);
  const fmtKm = (km) => (km == null ? "–"
    : (km < 1 ? km.toFixed(1) : km < 10 ? km.toFixed(1).replace(/\.0$/, "") : Math.round(km)) + " km");
  // the miss, worded so it can't be confused with a fact like a route's length
  const offBy = (km) => (km === 0 ? "Your tap was <b>inside it</b>" : `Your tap was <b>${fmtKm(km)}</b> off`);
  // bands on the score curve: ≥99 ≈ within 9 km, ≥90 ≈ 29 km, ≥75 ≈ 66 km, ≥55 ≈ 160 km,
  // ≥35 ≈ 360 km, ≥15 ≈ 830 km
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

  // ---- reveal: the answer, then a line drawn from the guess to it once the camera arrives ----
  function drawAnswer(loc, point, pulse, mi = 0) {
    targets(loc).forEach((t, k) => {
      const main = k === mi || !loc.members;               // an "any of" place: the nearest stands out
      if (t.kind === "area") {
        L.polygon(t.geometry, { color: "#c0392b", weight: 2, opacity: main ? 1 : 0.6, fillOpacity: main ? 0.25 : 0.12, interactive: false }).addTo(roundLayers);
      } else if (t.geometry.length > 1) {
        L.polyline(t.geometry, { color: "#c0392b", weight: main ? 4 : 3, opacity: main ? 0.9 : 0.5, interactive: false }).addTo(roundLayers);
      } else if (!main) {
        L.marker(t.geometry[0], { icon: answerIcon(false, true), interactive: false }).addTo(roundLayers);
      }
    });
    L.marker(point, { icon: answerIcon(pulse), interactive: false, zIndexOffset: 1000 }).addTo(roundLayers);
  }
  function animateReveal(r, loc) {
    const seq = ++revealSeq;
    drawAnswer(loc, r.point, true, r.mi);
    const from = r.guess, to = r.point;
    const line = L.polyline([from, from], {
      color: "#f4c542", weight: 4, opacity: 0.95, lineCap: "round", interactive: false,
    }).addTo(roundLayers);
    const live = () => seq === revealSeq && roundLayers.hasLayer(line);

    const bounds = L.latLngBounds([from, to]);
    const shape = targetOf(loc, r.mi).geometry;             // frame the nearest target, not all of them
    if (shape.length > 1) shape.forEach((p) => bounds.extend(p));
    moveTo(bounds, {}, () => {
      if (!live()) return;
      const px = map.latLngToContainerPoint(from).distanceTo(map.latLngToContainerPoint(to));
      const dur = reducedMotion() ? 0 : Math.max(250, Math.min(450, 1.2 * px));
      const t0 = performance.now();
      (function step(now) {
        if (!live()) return;
        const t = dur ? Math.min(1, (now - t0) / dur) : 1;
        const e = 1 - Math.pow(1 - t, 3);
        line.setLatLngs([from, [from[0] + (to[0] - from[0]) * e, from[1] + (to[1] - from[1]) * e]]);
        if (t < 1) requestAnimationFrame(step);
      })(t0);
    });
  }

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
  let fbKind = "place", fbContext = {}, fbOpener = null, fbTimer = null, fbSeq = 0;
  function openFeedback(kind, context) {
    clearTimeout(fbTimer);
    fbSeq++;
    fbKind = kind;
    fbContext = context;
    fbOpener = document.activeElement;
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
    // with a mouse, start typing straight away; on touch, don't throw the keyboard up
    // over the form — land on the dialog and let the player pick a field
    const first = kind === "bug" ? fbForm.elements.what : fbForm.elements.place;
    const fine = window.matchMedia("(hover: hover) and (pointer: fine)").matches;
    (fine ? first : document.getElementById("fb-title")).focus({ preventScroll: true });
  }
  function closeFeedback() {
    clearTimeout(fbTimer);
    fbSeq++;                 // a reply still in flight no longer touches the form
    if (fbEl.contains(document.activeElement)) document.activeElement.blur();
    fbEl.hidden = true;
    window.scrollTo(0, 0);   // iOS can leave the page offset after its keyboard closes
    if (fbOpener && document.contains(fbOpener) && fbOpener.focus) fbOpener.focus({ preventScroll: true });
    fbOpener = null;
    if (onWake) onWake();
  }
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
    const kind = fbKind;
    const subject = fbKind === "bug" ? `pnwtap bug (${fbContext.puzzle})` : `pnwtap place idea: ${f.place.value}`;
    const seq = fbSeq;
    fbSend.disabled = true;
    fbStatus.classList.remove("error");
    fbStatus.textContent = "Sending…";
    try {
      const res = await fetch(fb.endpoint, {
        method: "POST",
        headers: { "Content-Type": "application/json", Accept: "application/json" },
        body: JSON.stringify({
          access_key: fb.key, subject, from_name: "pnwtap",
          // like a real unticked checkbox, the honeypot is only sent when a bot ticks it
          ...(f.botcheck.checked ? { botcheck: true } : {}),
          message: lines.join("\n"), replyto: /@/.test(f.contact.value) ? f.contact.value : undefined,
        }),
      });
      const out = await res.json().catch(() => ({}));
      if (!res.ok || out.success === false) throw new Error(out.message || res.status);
      hit(`/feedback/${kind}`, kind === "bug" ? "Sent a bug report" : "Suggested a place", true);
      if (seq !== fbSeq) return;
      fbStatus.textContent = "Thanks — sent!";
      fbForm.reset();
      fbTimer = setTimeout(closeFeedback, 1400);
    } catch (err) {
      if (seq !== fbSeq) return;
      fbStatus.classList.add("error");
      fbStatus.textContent = "Couldn’t send that — please try again in a bit.";
      fbSend.disabled = false;
    }
  };

  // ---- the new day. Results on screen at midnight make way for the next puzzle, and a
  // tab left on an unstarted puzzle moves on to the new one. Both are checked against the
  // wall clock whenever the page comes back into view, since a sleeping phone's timers
  // freeze; never while offline or mid-feedback. ----
  let tick = null, onWake = null;
  document.addEventListener("visibilitychange", () => { if (!document.hidden && onWake) onWake(); });
  window.addEventListener("pageshow", (e) => { if (e.persisted && onWake) onWake(); });
  window.addEventListener("online", () => { if (onWake) onWake(); });

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
      targets(loc).forEach((t) => {
        const shape = t.geometry.length === 1
          ? L.circleMarker(t.geometry[0], { radius: 5, color: "#fff", weight: 1.5, fillColor: "#c0392b", fillOpacity: 1 })
          : t.kind === "area" ? L.polygon(t.geometry, opts) : L.polyline(t.geometry, opts);
        shape.bindTooltip(`${loc.name}${t.name ? ": " + t.name : ""} · ${loc.difficulty}`).on("click", (e) => {
          L.DomEvent.stopPropagation(e);
          pos = n;
          show();
        }).addTo(allLayer);
      });
    });
    puzzleNo.textContent = "playtest";
    helpBtn.hidden = true;
    let offTap = null;

    function show() {
      if (offTap) offTap();
      cancelReveal();
      roundLayers.clearLayers();
      const { loc } = all[pos];
      setPill(`${pos + 1} / ${all.length}`);
      const opts = all.map(({ loc: l }, n) =>
        `<option value="${n}"${n === pos ? " selected" : ""}>${CFG.emoji[l.difficulty]} ${esc(l.name)}</option>`).join("");
      setBody(
        `<div class="pt-bar"><button class="pt-btn" id="pt-prev" aria-label="Previous">◀</button>` +
        `<select id="pt-pick">${opts}</select>` +
        `<button class="pt-btn" id="pt-next" aria-label="Next">▶</button>` +
        `<button class="pt-btn" id="pt-rand" aria-label="Random">🎲</button></div>` +
        `<label class="pt-all"><input type="checkbox" id="pt-all"${map.hasLayer(allLayer) ? " checked" : ""}> show all answers</label>` +
        `<p class="ask"><strong>${esc(loc.name)}</strong></p>` +
        catChip(loc) + `<span class="pt-meta"> · ${loc.members ? "any of " + loc.members.length : loc.kind} · ${esc(loc.difficulty)}</span>` + clueLine(loc) +
        '<div id="pt-out"></div><button class="primary" id="lock" disabled>Tap the map</button>');
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
        const near = nearestTo(loc, tap);
        const sc = scoreFor(near.km);
        setCollapsed(false);
        armedAt = performance.now() + 350;
        // fill the card first, so the reveal is framed for the sheet that will be on screen
        document.getElementById("pt-out").innerHTML =
          `<p class="verdict">${verdict(sc)}</p>` +
          `<p class="result-score">${offBy(near.km)} · <b>${sc}</b> / 100</p>` +
          memberLine(loc, near.mi) + factCard(loc) +
          (loc.blurb ? `<p class="reveal-blurb">${esc(loc.blurb)}</p>` : "");
        lockBtn.textContent = "Next location";
        lockBtn.onclick = () => go(pos + 1);
        moreBelow();
        lockBtn.focus({ preventScroll: true });
        animateReveal({ guess: tap, point: near.point, mi: near.mi }, loc);
      };
    }
    show();
    resetView();
  }

  // ---- game ----
  if (!todaysIds) {
    setBody('<p class="msg">No puzzle scheduled for today — check back another day!</p>');
    resetView();
    return;
  }

  puzzleNo.textContent = dayLabel(DATE) + (IS_ARCHIVE ? ` · ${prettyDate(DATE)}` : "");
  const game = loadGame(DATE) || { rounds: [], done: false };
  // saved rounds keep the location's name; look it up by name, since row indices shift
  // whenever the sheet gains rows (fall back to the index for very old saves)
  const byName = new Map(DATA.locations.map((l) => [l.name, l]));
  const locOf = (r) => byName.get(r.name) || DATA.locations[r.i] || { geometry: [r.point] };
  const save = () => store.set(KEY(DATE), game);
  if (!IS_ARCHIVE) onWake = () => {
    if (!game.rounds.length && today() !== TODAY && fbEl.hidden && navigator.onLine !== false) {
      location.replace(location.pathname);
    }
  };

  function startRound() {
    cancelReveal();
    roundLayers.clearLayers();
    const roundIdx = game.rounds.length;
    const loc = DATA.locations[todaysIds[roundIdx]];
    const mult = CFG.multipliers[roundIdx];
    setPill(`${roundIdx + 1} / ${todaysIds.length}`);

    const hint = loc.members ? '<p class="hint">Whichever is nearest your tap counts.</p>'   // how many: revealed after
      : loc.kind === "area" ? '<p class="hint">Anywhere inside it counts.</p>'
      : loc.kind === "line" ? '<p class="hint">Anywhere along it counts.</p>' : "";
    const ask = loc.image
      ? `<p class="ask">Where is <strong>this place</strong>?</p>${catChip(loc)}${clueLine(loc)}` +
        `<img class="prompt-img" src="${esc(loc.image)}" alt="Photo of the mystery location">`
      : `<p class="ask"><strong>${esc(loc.name)}</strong></p>${catChip(loc)}${clueLine(loc)}${hint}`;
    setBody(
      `<div class="round-meta"><span>${CFG.emoji[loc.difficulty]} ${esc(loc.difficulty)} · ×${mult}</span>` +
      `<span>${total(game.rounds)} pts so far</span></div>` + ask +
      '<button class="primary" id="lock" disabled>Tap the map</button>');
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
      const near = nearestTo(loc, tap);
      const score = scoreFor(near.km);
      const r = {
        i: todaysIds[roundIdx], name: loc.name, difficulty: loc.difficulty,
        mult, km: near.km, score, guess: tap, point: near.point,
        ...(loc.members ? { mi: near.mi, member: near.member } : {}),
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
      renderResult(r, loc);     // the result card first, so the reveal is framed above it
      animateReveal(r, loc);
    };
  }

  function renderResult(r, loc) {
    setPill(`${game.rounds.length} / ${todaysIds.length}`);
    const last = game.done;
    setBody(
      `<p class="verdict">${verdict(r.score)}</p>` +
      `<p class="result-name">${esc(loc.name)} <span class="tier">${CFG.emoji[loc.difficulty] || ""}</span></p>` +
      `<p class="result-score">${offBy(r.km)} · <b>${r.score}</b> × ${r.mult} = ` +
        `<span class="pts">${r.score * r.mult}</span></p>` + memberLine(loc, r.mi) +
      (loc.image ? `<img class="reveal-img" src="${esc(loc.image)}" alt="">` : "") +
      factCard(loc) +
      (loc.blurb ? `<p class="reveal-blurb">${esc(loc.blurb)}</p>` : "") +
      `<button class="primary" id="next">${last ? "See results" : "Next round"}</button>`);
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
    cancelReveal();
    roundLayers.clearLayers();
    const bounds = L.latLngBounds([]);
    game.rounds.forEach((r, n) => {
      if (!r.guess || !r.point) return;                 // saved by the first version: score only
      const loc = locOf(r);
      drawAnswer(loc, r.point, false, miOf(loc, r));
      L.polyline([r.guess, r.point], { color: "#f4c542", weight: 3, opacity: 0.9, dashArray: "6 6", interactive: false })
        .addTo(roundLayers);
      L.marker(r.guess, { icon: guessIcon(n + 1), interactive: false }).addTo(roundLayers);
      bounds.extend(r.guess).extend(r.point);
    });
    return bounds;
  }

  function countUp(el, to) {
    if (reducedMotion()) { el.textContent = to; return; }
    const t0 = performance.now();
    (function step(now) {
      const t = Math.min(1, (now - t0) / 700);
      el.textContent = Math.round(to * (1 - Math.pow(1 - t, 3)));
      if (t < 1) requestAnimationFrame(step);
    })(t0);
  }

  function renderFinal(fresh) {
    setPill("");
    const bounds = drawSummary();

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

    setBody(
      `<div class="final-head"><div><p class="final">Final score</p>` +
      `<div class="final-score"><span id="final-n">${fresh ? 0 : score}</span><small> / ${maxScore}</small></div></div>` +
      `<div class="next-in"><p class="final">Next puzzle</p><div id="countdown" aria-live="off">–</div></div></div>` +
      `<ol class="breakdown">${rows}</ol>` +
      '<button class="primary" id="share">Share result</button>' +
      '<div class="stats">' +
        `<div><b>${st.played}</b><span>played</span></div>` +
        `<div><b>${st.avg}</b><span>average</span></div>` +
        `<div><b>${st.top}</b><span>best</span></div>` +
        `<div><b>${st.streak}</b><span>streak</span></div>` +
      "</div>" + missed + back + feedback);
    if (fresh) countUp(document.getElementById("final-n"), score);
    // frame the summary straight away (no flight): the count-up is the motion
    if (bounds.isValid()) moveTo(bounds, { maxZoom: 9, animate: false });
    else resetView();                                   // very old saves: score only

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
        targetOf(loc, miOf(loc, r)).geometry.forEach((p) => b.extend(p));
        moveTo(b, { maxZoom: 11 });
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
        setCollapsed(false);                        // (shared from the tucked-away header)
        box.focus();
        box.select();
      }
    };

    const cd = document.getElementById("countdown");
    const midnight = dayBegins(addDays(TODAY, 1));     // when this page's day ends (midnight Pacific)
    const lateFinish = Date.now() >= midnight;         // a game that ran past midnight
    const nextIsOut = () => {
      clearInterval(tick);
      onWake = null;
      cd.previousElementSibling.textContent = "New puzzle out";
      cd.innerHTML = '<a href="./">Play it →</a>';
    };
    const upd = () => {
      const ms = midnight - Date.now();
      if (ms < -1500) {
        // results that were already up at midnight make way for the new puzzle; results
        // just earned after it (or an archive day) stay, with a link instead
        if (IS_ARCHIVE || lateFinish) return nextIsOut();
        if (document.hidden || navigator.onLine === false || !fbEl.hidden) return;   // retried on return
        clearInterval(tick);
        onWake = null;
        location.replace(location.pathname);          // today's page, without any ?date=
        return;
      }
      const s = Math.max(0, Math.floor(ms / 1000));
      cd.textContent = [Math.floor(s / 3600), Math.floor(s / 60) % 60, s % 60]
        .map((n) => String(n).padStart(2, "0")).join(":");
    };
    clearInterval(tick);
    onWake = upd;
    upd();
    if (onWake === upd) tick = setInterval(upd, 1000);
  }

  // ---- go: finished → summary; otherwise the next unplayed round (locked guesses stay locked) ----
  try {
    if (game.done) renderFinal(false);
    else startRound();
  } finally {
    if (!map._loaded) resetView();                    // every path must leave the map with a view
  }
  hit(IS_ARCHIVE ? "/archive" : "/", `pnwtap ${dayLabel(DATE)}`);
})();
