// Distance & scoring math — a mirror of pnwtap/geometry.py. Change both in lockstep;
// tests/test_scoring_parity.py runs this file under node and compares with Python.
(function (root) {
  "use strict";

  const R = 6371.0088;
  const rad = (x) => (x * Math.PI) / 180;

  function haversine(a, b) {
    const dphi = rad(b[0] - a[0]);
    const dlmb = rad(b[1] - a[1]);
    const h = Math.sin(dphi / 2) ** 2 +
      Math.cos(rad(a[0])) * Math.cos(rad(b[0])) * Math.sin(dlmb / 2) ** 2;
    return 2 * R * Math.asin(Math.min(1, Math.sqrt(h)));
  }

  // local equirectangular projection to km offsets relative to `origin`
  function project(origin, pt) {
    return [
      rad(pt[1] - origin[1]) * Math.cos(rad(origin[0])) * R,
      rad(pt[0] - origin[0]) * R,
    ];
  }
  function unproject(origin, x, y) {
    const lat = origin[0] + (y / R) * 180 / Math.PI;
    const lng = origin[1] + (x / (R * Math.cos(rad(origin[0])))) * 180 / Math.PI;
    return [lat, lng];
  }

  // nearest point on segment a–b to the origin (the tap), in projected km
  function closestOnSegment(tap, a, b) {
    const [ax, ay] = project(tap, a);
    const [bx, by] = project(tap, b);
    const dx = bx - ax, dy = by - ay;
    if (dx === 0 && dy === 0) return [ax, ay];
    const t = Math.max(0, Math.min(1, -(ax * dx + ay * dy) / (dx * dx + dy * dy)));
    return [ax + t * dx, ay + t * dy];
  }

  function inside(pt, ring) {
    let hit = false;
    for (let i = 0, j = ring.length - 1; i < ring.length; j = i++) {
      const [yi, xi] = ring[i], [yj, xj] = ring[j];
      if ((yi > pt[0]) !== (yj > pt[0]) && pt[1] < (xj - xi) * (pt[0] - yi) / (yj - yi) + xi) hit = !hit;
    }
    return hit;
  }

  /** {km, point}: distance from `tap` to `path` (a point or polyline); for an `area`, 0 inside the ring. */
  function nearest(tap, path, area) {
    if (path.length === 1) return { km: haversine(tap, path[0]), point: path[0] };
    if (area && inside(tap, path)) return { km: 0, point: tap };
    let best = { km: Infinity, point: path[0] };
    for (let i = 0; i < path.length - 1; i++) {
      const [cx, cy] = closestOnSegment(tap, path[i], path[i + 1]);
      const km = Math.hypot(cx, cy);
      if (km < best.km) best = { km, point: unproject(tap, cx, cy) };
    }
    return best;
  }

  // 100 at 0 km, log-scaled (each halving of the miss is worth the same points), 0 at zeroKm
  const score = (km, nearKm, zeroKm) =>
    Math.round(100 * Math.max(0, 1 - Math.log1p(km / nearKm) / Math.log1p(zeroKm / nearKm)));

  const api = { haversine, nearest, score };
  if (typeof module !== "undefined" && module.exports) module.exports = api;
  else root.PNWTAP_SCORING = api;
})(this);
