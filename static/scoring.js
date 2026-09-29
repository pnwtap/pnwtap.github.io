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

  /** {km, point, index}: the nearest of several targets [{geometry, area}] — an "any of" place. */
  function nearestAny(tap, targets) {
    let best = null;
    targets.forEach((t, index) => {
      const n = nearest(tap, t.geometry, t.area);
      if (!best || n.km < best.km) best = { km: n.km, point: n.point, index };
    });
    return best;
  }

  // 100 at 0 km, nearly flat out to ~nearKm, then log-scaled (each halving of the miss is
  // worth the same points), 0 at zeroKm
  const score = (km, nearKm, zeroKm, shape = 1) =>
    Math.round(100 * Math.max(0, 1 - Math.log1p((km / nearKm) ** shape) / Math.log1p((zeroKm / nearKm) ** shape)));

  // [[lat, lng], ...] from an encoded polyline (Google's algorithm at 1e4 precision) —
  // mirrors decode_polyline in pnwtap/geometry.py; the build encodes every path this way
  function decode(str, precision = 1e4) {
    const out = [], acc = [0, 0];
    let i = 0;
    while (i < str.length) {
      for (let k = 0; k < 2; k++) {
        let shift = 0, result = 0, b;
        do {
          b = str.charCodeAt(i++) - 63;
          result += (b & 0x1f) * 2 ** shift;   // multiply, not <<: stays exact past 31 bits
          shift += 5;
        } while (b >= 0x20);
        acc[k] += result % 2 ? -(result + 1) / 2 : result / 2;
      }
      out.push([acc[0] / precision, acc[1] / precision]);
    }
    return out;
  }

  // ---- the puzzle calendar: one day for everyone, on the game's own clock (a time zone
  // such as America/Los_Angeles), whatever the device's zone ----
  const clocks = {};
  function wallClock(t, tz) {           // {year, month, day, hour, minute, second} at instant t in tz
    const f = clocks[tz] || (clocks[tz] = new Intl.DateTimeFormat("en-US", {
      timeZone: tz, hourCycle: "h23", year: "numeric", month: "numeric", day: "numeric",
      hour: "numeric", minute: "numeric", second: "numeric",
    }));
    const p = {};
    f.formatToParts(t).forEach((x) => { if (x.type !== "literal") p[x.type] = +x.value; });
    p.hour %= 24;                       // some engines say 24:00 for midnight
    return p;
  }
  /** The calendar date (YYYY-MM-DD) at instant t (ms) in time zone tz. */
  function dayIn(t, tz) {
    const p = wallClock(t, tz), z = (n) => String(n).padStart(2, "0");
    return `${p.year}-${z(p.month)}-${z(p.day)}`;
  }
  /** The instant (ms) the calendar day YYYY-MM-DD begins in time zone tz. */
  function dayStart(day, tz) {
    const [y, m, d] = day.split("-").map(Number);
    const midnightUTC = Date.UTC(y, m - 1, d);
    const offset = (t) => {             // tz's wall clock minus UTC, at instant t
      const p = wallClock(t, tz);
      return Date.UTC(p.year, p.month - 1, p.day, p.hour, p.minute, p.second) - Math.floor(t / 1000) * 1000;
    };
    const t = midnightUTC - offset(midnightUTC);
    return midnightUTC - offset(t);     // again at the answer, in case a DST change lies between
  }

  const api = { haversine, nearest, nearestAny, score, decode, dayIn, dayStart };
  if (typeof module !== "undefined" && module.exports) module.exports = api;
  else root.PNWTAP_SCORING = api;
})(this);
