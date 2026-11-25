// Numeric sorting for the combat tables.
// The upstream tablesort.number plugin (dist/sorts/tablesort.number.min.js)
// does not ship in the 5.3.0 npm bundle root and, more importantly, strips
// decimal commas ("21,5" -> 215) and cannot handle dice notation or
// thresholds. We therefore register our own comparator with Tablesort.extend.
const parseSortValue = (text) => {
  const raw = String(text === null || text === undefined ? "" : text).trim();
  if (raw === "") return Number.NaN;
  // Placeholder for "not applicable".
  if (raw === "-" || raw === "\u2013" || raw === "\u2014") return Number.NEGATIVE_INFINITY;

  // Dice notation, sorted by average damage: 3d4+15 -> 22.5
  const dice = raw.match(/^(\d+)\s*d\s*(\d+)\s*(?:([+\u2212-])\s*(\d+))?$/i);
  if (dice) {
    const count = Number(dice[1]);
    const faces = Number(dice[2]);
    const bonus = dice[4] ? Number((dice[3] === "+" ? "" : "-") + dice[4]) : 0;
    return (count * (faces + 1)) / 2 + bonus;
  }

  // Numbers with sign, decimal comma/dot, thousands spaces, percent sign
  // and short unit suffixes (HP, PV, lbs, ...).
  const compact = raw.replace(/\u2212/g, "-").replace(/\s+/g, "");
  if (!/^[<>]?[+-]?\d+(?:[.,]\d+)?%?[A-Za-z]{0,3}$/.test(compact)) return Number.NaN;

  const value = compact.match(/[+-]?\d+(?:[.,]\d+)?/);
  return Number.parseFloat(value[0].replace(",", "."));
};

if (typeof Tablesort !== "undefined") {
  Tablesort.extend(
    "eressea-number",
    (item) => !Number.isNaN(parseSortValue(item)),
    // tablesort's comparators are called before it reverses the array,
    // so b - a yields ascending order (as advertised by aria-sort).
    (a, b) => parseSortValue(b) - parseSortValue(a),
  );
}

document$.subscribe(() => {
  document.querySelectorAll("article .sortable table").forEach((table) => {
    new Tablesort(table);
  });
});
