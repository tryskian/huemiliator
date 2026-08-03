import {execFileSync} from "node:child_process";
import fs from "node:fs";
import path from "node:path";

import * as d3 from "d3";
import * as Plot from "@observablehq/plot";
import {JSDOM} from "jsdom";

const repoRoot = process.cwd();
const parkedDir = path.join(repoRoot, ".local", "parked");
const evalDb = path.join(repoRoot, ".local", "evals.sqlite");
const swatchDataPath = path.join(repoRoot, "data", "margaret2_swatches.json");
const familyRangePaletteOutputPath = path.join(
  repoRoot,
  "docs",
  "research",
  "family-range-palette.svg",
);
const pulseStackOutputPath = path.join(
  repoRoot,
  "docs",
  "research",
  "eval-pulse-stack.svg",
);
const residueBarsOutputPath = path.join(
  repoRoot,
  "docs",
  "research",
  "eval-residue-family-bars.svg",
);
const familyCountBarsOutputPath = path.join(
  repoRoot,
  "docs",
  "research",
  "family-count-bars.svg",
);
const edgeDensityHeatmapOutputPath = path.join(
  repoRoot,
  "docs",
  "research",
  "edge-density-heatmap.svg",
);
const activeFailSurfaceSplitOutputPath = path.join(
  repoRoot,
  "docs",
  "research",
  "active-fail-surface-split.svg",
);
const archiveIntegrityOutputPath = path.join(
  repoRoot,
  "docs",
  "research",
  "archive-integrity-check.svg",
);

const segmentOrder = ["anchor", "counted_seam", "excluded_noise"];
const segmentLabels = new Map([
  ["anchor", "anchor"],
  ["counted_seam", "counted seam"],
  ["excluded_noise", "excluded noise"],
]);
const segmentColours = new Map([
  ["anchor", "#287a68"],
  ["counted_seam", "#c34f4d"],
  ["excluded_noise", "#8e8378"],
]);
const familyOrder = [
  "neutral",
  "brown",
  "red",
  "orange",
  "yellow",
  "green",
  "blue",
  "purple",
  "pink",
];
const familyColours = new Map([
  ["neutral", "#9a9286"],
  ["brown", "#76513c"],
  ["red", "#b83b45"],
  ["orange", "#d8793e"],
  ["yellow", "#c89f2d"],
  ["green", "#5e8c49"],
  ["blue", "#3e76a8"],
  ["purple", "#7b5ea7"],
  ["pink", "#c96b8d"],
]);
const splitPhaseOrder = ["source seams", "closed anchors"];
const splitPhaseColours = new Map([
  ["source seams", "#c34f4d"],
  ["closed anchors", "#287a68"],
]);
const neutralSplitGroups = [
  {
    group: "lilac / mauve",
    sourceIds: [20082, 20083, 20094],
    proofIds: [20097, 20098, 20099],
  },
  {
    group: "blue / jade",
    sourceIds: [20085, 20090, 20091],
    proofIds: [20100, 20101, 20102],
  },
  {
    group: "mint / green",
    sourceIds: [20086, 20087, 20095],
    proofIds: [20103, 20104, 20105],
  },
  {
    group: "warm peach / pearl",
    sourceIds: [20084, 20088, 20107],
    proofIds: [20151, 20152, 20153],
  },
];
let familySummaryCache = null;
let familyRowsCache = null;

function pythonEnv() {
  const srcPath = path.join(repoRoot, "src");
  return {
    ...process.env,
    PYTHONPATH: process.env.PYTHONPATH
      ? `${srcPath}${path.delimiter}${process.env.PYTHONPATH}`
      : srcPath,
  };
}

function pythonBin() {
  const venvPython = path.join(repoRoot, ".venv", "bin", "python");
  return fs.existsSync(venvPython) ? venvPython : "python3";
}

function readJsonl(filePath) {
  return fs
    .readFileSync(filePath, "utf8")
    .split("\n")
    .filter(Boolean)
    .map((line) => JSON.parse(line));
}

function readMetaLabel(filePath) {
  const metaPath = filePath.replace(/\.jsonl$/, ".meta.txt");
  const text = fs.readFileSync(metaPath, "utf8");
  return text.match(/^label: (.+)$/m)?.[1] ?? path.basename(filePath);
}

function majorityFamily(rows) {
  const counts = d3.rollups(
    rows,
    (items) => items.length,
    (row) => row.family,
  );
  counts.sort((left, right) => d3.descending(left[1], right[1]));
  return counts[0]?.[0] ?? "unknown";
}

function countSegments(rows) {
  const counts = new Map(segmentOrder.map((segment) => [segment, 0]));
  for (const row of rows) {
    const segment = row.pulse_label;
    if (counts.has(segment)) {
      counts.set(segment, counts.get(segment) + 1);
    }
  }
  return counts;
}

function pulseFromRows({rows, source, label, sequence}) {
  const family = majorityFamily(rows);
  const counts = countSegments(rows);
  const firstId = d3.min(rows, (row) => row.id);
  const lastId = d3.max(rows, (row) => row.id);

  return {
    sequence,
    family,
    label: `P${String(sequence).padStart(2, "0")} ${family}${
      source === "live" ? " latest" : ""
    }`,
    archiveLabel: label,
    source,
    firstId,
    lastId,
    counts,
    rows,
  };
}

function readParkedPulses() {
  if (!fs.existsSync(parkedDir)) {
    throw new Error(`Missing parked eval directory: ${parkedDir}`);
  }

  return fs
    .readdirSync(parkedDir)
    .filter((file) => /^eval-surface-.*\.jsonl$/.test(file))
    .sort()
    .map((file) => path.join(parkedDir, file))
    .map((filePath) => {
      const rows = readJsonl(filePath);
      const label = readMetaLabel(filePath);
      const firstId = d3.min(rows, (row) => row.id);
      return {rows, label, source: "parked", firstId};
    })
    .filter(({rows}) => rows.some((row) => row.pulse_label))
    .sort((left, right) => d3.ascending(left.firstId, right.firstId))
    .map((pulse, index) => ({...pulse, sequence: index + 1}))
    .map(pulseFromRows)
    .sort((left, right) => d3.ascending(left.sequence, right.sequence));
}

function familyFromArchiveLabel(label) {
  const tokens = label.toLowerCase().split(/[^a-z]+/).filter(Boolean);
  return tokens.find((token) => familyOrder.includes(token)) ?? "unknown";
}

function readParkedArchives() {
  if (!fs.existsSync(parkedDir)) {
    throw new Error(`Missing parked eval directory: ${parkedDir}`);
  }

  return fs
    .readdirSync(parkedDir)
    .filter((file) => /^eval-surface-.*\.jsonl$/.test(file))
    .sort()
    .map((file) => {
      const filePath = path.join(parkedDir, file);
      const rows = readJsonl(filePath);
      const label = readMetaLabel(filePath);
      return {
        file,
        rows,
        label,
        archiveFamily: familyFromArchiveLabel(label),
      };
    });
}

function readLiveRows() {
  if (!fs.existsSync(evalDb)) {
    throw new Error(`Missing live eval DB: ${evalDb}`);
  }

  const output = execFileSync(
    "sqlite3",
    [
      "-json",
      evalDb,
      "select * from eval_outputs order by id;",
    ],
    {encoding: "utf8"},
  );
  return JSON.parse(output);
}

function readFamilySummaries() {
  if (familySummaryCache !== null) {
    return familySummaryCache;
  }
  if (!fs.existsSync(swatchDataPath)) {
    throw new Error(`Missing swatch snapshot: ${swatchDataPath}`);
  }

  // Reuse the Python runtime classifier so the chart cannot drift from app logic.
  const code = String.raw`
import json
from pathlib import Path

from huemiliator.families import FAMILY_NAMES, build_family_rank_index
from huemiliator.swatches import load_swatch_snapshot

dataset = load_swatch_snapshot(Path("data/margaret2_swatches.json"))
ranked = build_family_rank_index(dataset)
members = {family: [] for family in FAMILY_NAMES}
for item in ranked.values():
    members[item.family].append(item)


def sample_members(group):
    group = sorted(group, key=lambda item: item.family_rank)
    if not group:
        return []
    if len(group) <= 6:
        indexes = range(len(group))
    else:
        indexes = [round(index * (len(group) - 1) / 5) for index in range(6)]
    return [
        {
            "name": group[index].swatch.name,
            "hex": group[index].swatch.hex,
            "rank": group[index].family_rank,
            "source_order": group[index].swatch.source_order,
        }
        for index in indexes
    ]


payload = []
for family in FAMILY_NAMES:
    group = members[family]
    payload.append(
        {
            "family": family,
            "count": len(group),
            "samples": sample_members(group),
        }
    )
print(json.dumps(payload))
`;

  const output = execFileSync(pythonBin(), ["-c", code], {
    cwd: repoRoot,
    encoding: "utf8",
    env: pythonEnv(),
  });
  familySummaryCache = JSON.parse(output);
  return familySummaryCache;
}

function readFamilyCounts() {
  return readFamilySummaries().map(({family, count}) => ({family, count}));
}

function readFamilyRows() {
  if (familyRowsCache !== null) {
    return familyRowsCache;
  }
  if (!fs.existsSync(swatchDataPath)) {
    throw new Error(`Missing swatch snapshot: ${swatchDataPath}`);
  }

  const code = String.raw`
import json
from pathlib import Path

from huemiliator.families import build_family_rank_index
from huemiliator.swatches import load_swatch_snapshot

dataset = load_swatch_snapshot(Path("data/margaret2_swatches.json"))
ranked = build_family_rank_index(dataset)
payload = [
    {
        "name": item.swatch.name,
        "hex": item.swatch.hex,
        "family": item.family,
        "family_rank": item.family_rank,
        "source_order": item.swatch.source_order,
    }
    for item in ranked.values()
]
print(json.dumps(payload))
`;

  const output = execFileSync(pythonBin(), ["-c", code], {
    cwd: repoRoot,
    encoding: "utf8",
    env: pythonEnv(),
  });
  familyRowsCache = JSON.parse(output);
  return familyRowsCache;
}

function buildPulseData() {
  const parkedPulses = readParkedPulses();
  const liveRows = readLiveRows().filter((row) => row.pulse_label);
  const maxPulse = d3.max(parkedPulses, (pulse) => pulse.sequence) ?? 0;
  const pulses = [...parkedPulses];

  if (liveRows.length) {
    const liveFamily = majorityFamily(liveRows);
    pulses.push(
      pulseFromRows({
        rows: liveRows,
        source: "live",
        label: `latest ${liveFamily} proof surface ${d3.min(
          liveRows,
          (row) => row.id,
        )}..${d3.max(liveRows, (row) => row.id)}`,
        sequence: maxPulse + 1,
      }),
    );
  }

  return pulses.sort((left, right) => d3.ascending(left.sequence, right.sequence));
}

function rowsById(pulses) {
  return new Map(pulses.flatMap((pulse) => pulse.rows.map((row) => [row.id, row])));
}

function readRowsForIds(rowIndex, ids, context) {
  return ids.map((id) => {
    const row = rowIndex.get(id);
    if (!row) {
      throw new Error(`Missing row ${id} for ${context}`);
    }
    return row;
  });
}

function toSegments(pulses) {
  return pulses.flatMap((pulse) => {
    let x0 = 0;
    return segmentOrder.map((segment) => {
      const count = pulse.counts.get(segment) ?? 0;
      const item = {
        pulse: pulse.label,
        sequence: pulse.sequence,
        family: pulse.family,
        source: pulse.source,
        segment: segmentLabels.get(segment),
        x0,
        x1: x0 + count,
        count,
        title: `${pulse.label}\n${segmentLabels.get(segment)}: ${count}\nrows ${pulse.firstId}..${pulse.lastId}\narchive: ${pulse.archiveLabel}`,
      };
      x0 += count;
      return item;
    });
  });
}

function renderEvalPulseStack() {
  const pulses = buildPulseData();
  const segments = toSegments(pulses);
  const yDomain = pulses.map((pulse) => pulse.label);
  const height = 96 + yDomain.length * 22;
  const {window} = new JSDOM("<!DOCTYPE html>");

  const svg = Plot.plot({
    document: window.document,
    className: "huey-eval-pulse-stack",
    width: 980,
    height,
    marginTop: 44,
    marginRight: 32,
    marginBottom: 44,
    marginLeft: 118,
    style: {
      background: "#f6f5f2",
      color: "#26231f",
      fontFamily: "Inter, Arial, sans-serif",
      fontSize: 12,
    },
    x: {
      domain: [0, 15],
      label: "rows in pulse",
      ticks: [0, 5, 10, 15],
      grid: true,
    },
    y: {
      domain: yDomain,
      label: null,
    },
    color: {
      domain: [...segmentLabels.values()],
      range: segmentOrder.map((segment) => segmentColours.get(segment)),
    },
    marks: [
      Plot.ruleX([0]),
      Plot.rectX(segments, {
        x1: "x0",
        x2: "x1",
        y: "pulse",
        fill: "segment",
        title: "title",
        insetTop: 3,
        insetBottom: 3,
        rx: 2,
      }),
      Plot.text(
        segments.filter((segment) => segment.count >= 4),
        {
          x: (segment) => (segment.x0 + segment.x1) / 2,
          y: "pulse",
          text: (segment) => segment.count,
          fill: "white",
          fontSize: 10,
          fontWeight: 700,
        },
      ),
    ],
  });

  svg.setAttribute("xmlns", "http://www.w3.org/2000/svg");
  svg.setAttribute("role", "img");
  svg.setAttribute("aria-labelledby", "title desc");

  const title = window.document.createElementNS("http://www.w3.org/2000/svg", "title");
  title.setAttribute("id", "title");
  title.textContent = "Huemiliator eval pulse stacked bars";

  const desc = window.document.createElementNS("http://www.w3.org/2000/svg", "desc");
  desc.setAttribute("id", "desc");
  desc.textContent =
    "Stacked horizontal bars for each Beta 1.0 eval pulse, with anchor, counted seam, and excluded noise row counts.";

  svg.prepend(desc);
  svg.prepend(title);
  svg.append(buildLegend(window.document));

  fs.writeFileSync(pulseStackOutputPath, `${svg.outerHTML}\n`);
  console.log(`wrote ${path.relative(repoRoot, pulseStackOutputPath)}`);
}

function createSvgElement(document, name, attributes = {}, text = null) {
  const element = document.createElementNS("http://www.w3.org/2000/svg", name);
  for (const [key, value] of Object.entries(attributes)) {
    element.setAttribute(key, String(value));
  }
  if (text !== null) {
    element.textContent = text;
  }
  return element;
}

function appendSvg(parent, name, attributes = {}, text = null) {
  const element = createSvgElement(parent.ownerDocument, name, attributes, text);
  parent.append(element);
  return element;
}

function needsSwatchStroke(hex) {
  const channels = hex
    .slice(1)
    .match(/.{2}/g)
    .map((channel) => Number.parseInt(channel, 16) / 255);
  const [red, green, blue] = channels.map((channel) =>
    channel <= 0.03928
      ? channel / 12.92
      : ((channel + 0.055) / 1.055) ** 2.4,
  );
  return 0.2126 * red + 0.7152 * green + 0.0722 * blue > 0.82;
}

function renderFamilyRangePalette() {
  const summaries = readFamilySummaries();
  const {window} = new JSDOM("<!DOCTYPE html>");
  const document = window.document;
  const width = 774;
  const height = 534;
  const cardWidth = 230;
  const cardHeight = 150;
  const cardGapX = 18;
  const cardGapY = 18;
  const cardStartX = 24;
  const cardStartY = 24;

  const svg = createSvgElement(document, "svg", {
    xmlns: "http://www.w3.org/2000/svg",
    viewBox: `0 0 ${width} ${height}`,
    role: "img",
    "aria-labelledby": "title desc",
  });
  appendSvg(svg, "title", {id: "title"}, "Huemiliator family range palette");
  appendSvg(
    svg,
    "desc",
    {id: "desc"},
    "Nine colour-chip cards showing sampled range chips for neutral, brown, red, orange, yellow, green, blue, purple, and pink.",
  );
  appendSvg(svg, "rect", {width, height, fill: "#f6f5f2"});

  const root = appendSvg(svg, "g", {"font-family": "Inter, Arial, sans-serif"});

  for (const [index, family] of familyOrder.entries()) {
    const summary = summaries.find((item) => item.family === family);
    if (!summary) {
      throw new Error(`Missing family summary: ${family}`);
    }

    const x = cardStartX + (index % 3) * (cardWidth + cardGapX);
    const y = cardStartY + Math.floor(index / 3) * (cardHeight + cardGapY);
    const card = appendSvg(root, "g", {transform: `translate(${x} ${y})`});

    appendSvg(card, "rect", {
      width: cardWidth,
      height: cardHeight,
      rx: 8,
      fill: "#ffffff",
      stroke: "#d8d4cc",
    });

    for (const [sampleIndex, sample] of summary.samples.entries()) {
      const chip = appendSvg(card, "rect", {
        x: 16 + sampleIndex * 35,
        y: 16,
        width: 28,
        height: 28,
        rx: 3,
        fill: sample.hex,
      });
      if (needsSwatchStroke(sample.hex)) {
        chip.setAttribute("stroke", "#d8d4cc");
      }
      appendSvg(
        chip,
        "title",
        {},
        `${sample.name}\nrank ${sample.rank} / ${summary.count}\nsource order ${sample.source_order}`,
      );
    }

    appendSvg(
      card,
      "text",
      {
        x: 16,
        y: 86,
        fill: "#211f1b",
        "font-size": 24,
        "font-weight": 700,
      },
      family,
    );
    appendSvg(
      card,
      "text",
      {x: 16, y: 113, fill: "#6b6258", "font-size": 13},
      `${summary.count} swatches`,
    );
    appendSvg(
      card,
      "text",
      {x: 16, y: 133, fill: "#9c948b", "font-size": 11},
      "sampled classifier range",
    );
  }

  fs.writeFileSync(familyRangePaletteOutputPath, `${svg.outerHTML}\n`);
  console.log(`wrote ${path.relative(repoRoot, familyRangePaletteOutputPath)}`);
}

function renderResidueFamilyBars() {
  const pulses = buildPulseData();
  const rows = pulses.flatMap((pulse) =>
    pulse.rows
      .filter((row) => row.pulse_label === "counted_seam")
      .map((row) => ({
        family: row.family,
        pulse: pulse.label,
        rowId: row.id,
        pair: `${row.nearest_swatch_name} -> ${row.replacement_shade_name}`,
      })),
  );
  const familyCounts = d3
    .rollups(
      rows,
      (items) => items.length,
      (row) => row.family,
    )
    .map(([family, count]) => ({family, count}))
    .sort((left, right) => d3.descending(left.count, right.count));

  const {window} = new JSDOM("<!DOCTYPE html>");
  const yDomain = familyCounts.map((item) => item.family);
  const maxCount = d3.max(familyCounts, (item) => item.count) ?? 0;

  const svg = Plot.plot({
    document: window.document,
    className: "huey-residue-family-bars",
    width: 760,
    height: 108 + yDomain.length * 34,
    marginTop: 52,
    marginRight: 72,
    marginBottom: 44,
    marginLeft: 98,
    style: {
      background: "#f6f5f2",
      color: "#26231f",
      fontFamily: "Inter, Arial, sans-serif",
      fontSize: 12,
    },
    x: {
      domain: [0, Math.max(5, maxCount)],
      label: "counted seam rows",
      grid: true,
    },
    y: {
      domain: yDomain,
      label: null,
    },
    marks: [
      Plot.ruleX([0]),
      Plot.barX(familyCounts, {
        x: "count",
        y: "family",
        fill: "#c34f4d",
        rx: 3,
        title: (item) => `${item.family}\ncounted seams: ${item.count}`,
      }),
      Plot.text(familyCounts, {
        x: "count",
        y: "family",
        text: "count",
        dx: 10,
        fill: "#26231f",
        fontWeight: 700,
      }),
    ],
  });

  svg.setAttribute("xmlns", "http://www.w3.org/2000/svg");
  svg.setAttribute("role", "img");
  svg.setAttribute("aria-labelledby", "title desc");

  const title = window.document.createElementNS("http://www.w3.org/2000/svg", "title");
  title.setAttribute("id", "title");
  title.textContent = "Huemiliator counted seams by family";

  const desc = window.document.createElementNS("http://www.w3.org/2000/svg", "desc");
  desc.setAttribute("id", "desc");
  desc.textContent =
    "Horizontal bars showing counted seam rows by Huemiliator family across row-order Beta 1.0 pulses.";

  svg.prepend(desc);
  svg.prepend(title);

  fs.writeFileSync(residueBarsOutputPath, `${svg.outerHTML}\n`);
  console.log(`wrote ${path.relative(repoRoot, residueBarsOutputPath)}`);
}

function renderFamilyCountBars() {
  const familyCounts = readFamilyCounts()
    .map((item) => ({
      family: item.family,
      count: item.count,
      order: familyOrder.indexOf(item.family),
    }))
    .sort(
      (left, right) =>
        d3.descending(left.count, right.count) ||
        d3.ascending(left.order, right.order),
    );
  const total = d3.sum(familyCounts, (item) => item.count);
  const yDomain = familyCounts.map((item) => item.family);
  const maxCount = d3.max(familyCounts, (item) => item.count) ?? 0;
  const percent = d3.format(".1%");
  const {window} = new JSDOM("<!DOCTYPE html>");

  const svg = Plot.plot({
    document: window.document,
    className: "huey-family-count-bars",
    width: 760,
    height: 108 + yDomain.length * 34,
    marginTop: 52,
    marginRight: 86,
    marginBottom: 44,
    marginLeft: 98,
    style: {
      background: "#f6f5f2",
      color: "#26231f",
      fontFamily: "Inter, Arial, sans-serif",
      fontSize: 12,
    },
    x: {
      domain: [0, maxCount],
      label: "swatches in runtime family",
      grid: true,
    },
    y: {
      domain: yDomain,
      label: null,
    },
    marks: [
      Plot.ruleX([0]),
      Plot.barX(familyCounts, {
        x: "count",
        y: "family",
        fill: (item) => familyColours.get(item.family),
        rx: 3,
        title: (item) =>
          `${item.family}\n${item.count} swatches\n${percent(
            item.count / total,
          )} of snapshot`,
      }),
      Plot.text(familyCounts, {
        x: "count",
        y: "family",
        text: "count",
        dx: 10,
        fill: "#26231f",
        fontWeight: 700,
      }),
    ],
  });

  svg.setAttribute("xmlns", "http://www.w3.org/2000/svg");
  svg.setAttribute("role", "img");
  svg.setAttribute("aria-labelledby", "title desc");

  const title = window.document.createElementNS("http://www.w3.org/2000/svg", "title");
  title.setAttribute("id", "title");
  title.textContent = "Huemiliator swatches by runtime family";

  const desc = window.document.createElementNS("http://www.w3.org/2000/svg", "desc");
  desc.setAttribute("id", "desc");
  desc.textContent =
    "Horizontal bars showing frozen swatch snapshot counts by current Huemiliator runtime family assignment.";

  svg.prepend(desc);
  svg.prepend(title);

  fs.writeFileSync(familyCountBarsOutputPath, `${svg.outerHTML}\n`);
  console.log(`wrote ${path.relative(repoRoot, familyCountBarsOutputPath)}`);
}

function buildEdgeDensityBins() {
  const binStep = 10;
  const bins = new Map();

  for (const row of readFamilyRows()) {
    const lab = d3.lab(row.hex);
    const a0 = Math.floor(lab.a / binStep) * binStep;
    const b0 = Math.floor(lab.b / binStep) * binStep;
    const key = `${a0}\0${b0}`;

    if (!bins.has(key)) {
      bins.set(key, {
        a0,
        a1: a0 + binStep,
        b0,
        b1: b0 + binStep,
        count: 0,
        families: new Map(),
        samples: [],
      });
    }

    const bin = bins.get(key);
    bin.count += 1;
    bin.families.set(row.family, (bin.families.get(row.family) ?? 0) + 1);
    if (bin.samples.length < 8) {
      bin.samples.push(`${row.name} (${row.family})`);
    }
  }

  return [...bins.values()]
    .map((bin) => {
      const families = [...bin.families.entries()].sort(
        (left, right) =>
          d3.descending(left[1], right[1]) || d3.ascending(left[0], right[0]),
      );
      const familySummary = families
        .map(([family, count]) => `${family} ${count}`)
        .join(", ");

      return {
        ...bin,
        aMid: (bin.a0 + bin.a1) / 2,
        bMid: (bin.b0 + bin.b1) / 2,
        familyCount: families.length,
        familySummary,
        title: `Lab a* ${bin.a0}..${bin.a1}\nLab b* ${bin.b0}..${bin.b1}\nswatches: ${bin.count}\nfamilies: ${familySummary}\n${bin.samples.join(
          "\n",
        )}`,
      };
    })
    .sort(
      (left, right) =>
        d3.ascending(left.a0, right.a0) || d3.ascending(left.b0, right.b0),
    );
}

function renderEdgeDensityHeatmap() {
  const bins = buildEdgeDensityBins();
  const maxCount = d3.max(bins, (bin) => bin.count) ?? 1;
  const maxMix = Math.max(1, d3.max(bins, (bin) => bin.familyCount - 1) ?? 1);
  const countPressure = d3.scaleSqrt([1, maxCount], [0.18, 1]);
  const sameFill = d3.interpolateRgb("#dfeee8", "#287a68");
  const mixedFill = d3.interpolateRgb("#f4d8d6", "#b83b45");
  const {window} = new JSDOM("<!DOCTYPE html>");

  const svg = Plot.plot({
    document: window.document,
    className: "huey-edge-density-heatmap",
    width: 860,
    height: 620,
    marginTop: 66,
    marginRight: 38,
    marginBottom: 64,
    marginLeft: 82,
    style: {
      background: "#f6f5f2",
      color: "#26231f",
      fontFamily: "Inter, Arial, sans-serif",
      fontSize: 12,
    },
    x: {
      domain: [-50, 70],
      label: "Lab a* (green to red)",
      grid: true,
      ticks: d3.range(-50, 71, 20),
    },
    y: {
      domain: [-50, 90],
      label: "Lab b* (blue to yellow)",
      grid: true,
      ticks: d3.range(-40, 91, 20),
    },
    marks: [
      Plot.rect(bins, {
        x1: "a0",
        x2: "a1",
        y1: "b0",
        y2: "b1",
        fill: (bin) => {
          const density = countPressure(bin.count);
          if (bin.familyCount === 1) {
            return sameFill(0.12 + density * 0.58);
          }
          const mixPressure = (bin.familyCount - 1) / maxMix;
          return mixedFill(0.18 + density * 0.46 + mixPressure * 0.32);
        },
        title: "title",
        inset: 0.5,
      }),
      Plot.text(
        bins.filter((bin) => bin.familyCount >= 4 && bin.count >= 8),
        {
          x: "aMid",
          y: "bMid",
          text: (bin) => bin.familyCount,
          fill: "#26231f",
          fontSize: 10,
          fontWeight: 700,
        },
      ),
      Plot.ruleX([0], {stroke: "#9c948b", strokeDasharray: "4,4"}),
      Plot.ruleY([0], {stroke: "#9c948b", strokeDasharray: "4,4"}),
      Plot.frame({stroke: "#d8d4cc"}),
    ],
  });

  svg.setAttribute("xmlns", "http://www.w3.org/2000/svg");
  svg.setAttribute("role", "img");
  svg.setAttribute("aria-labelledby", "title desc");

  const title = window.document.createElementNS("http://www.w3.org/2000/svg", "title");
  title.setAttribute("id", "title");
  title.textContent = "Huemiliator edge-density heatmap";

  const desc = window.document.createElementNS("http://www.w3.org/2000/svg", "desc");
  desc.setAttribute("id", "desc");
  desc.textContent =
    "A Lab-space heatmap showing runtime-classified swatch density and mixed-family edge pressure across colour bins.";

  svg.prepend(desc);
  svg.prepend(title);
  svg.append(buildEdgeDensityLegend(window.document));

  fs.writeFileSync(edgeDensityHeatmapOutputPath, `${svg.outerHTML}\n`);
  console.log(`wrote ${path.relative(repoRoot, edgeDensityHeatmapOutputPath)}`);
}

function buildEdgeDensityLegend(document) {
  const legend = document.createElementNS("http://www.w3.org/2000/svg", "g");
  legend.setAttribute("aria-label", "legend");
  legend.setAttribute("transform", "translate(82 22)");

  const items = [
    {label: "single-family bin", fill: "#287a68"},
    {label: "mixed-family edge", fill: "#b83b45"},
    {label: "darker cells hold more swatches", fill: "#6f6259"},
  ];

  let x = 0;
  for (const item of items) {
    const square = document.createElementNS("http://www.w3.org/2000/svg", "rect");
    square.setAttribute("x", x);
    square.setAttribute("y", 0);
    square.setAttribute("width", 12);
    square.setAttribute("height", 12);
    square.setAttribute("rx", 2);
    square.setAttribute("fill", item.fill);
    legend.append(square);

    const text = document.createElementNS("http://www.w3.org/2000/svg", "text");
    text.setAttribute("x", x + 18);
    text.setAttribute("y", 10);
    text.setAttribute("font-size", 12);
    text.setAttribute("fill", "#26231f");
    text.setAttribute("text-anchor", "start");
    text.textContent = item.label;
    legend.append(text);

    x += item.label.length > 18 ? 224 : 154;
  }

  return legend;
}

function buildNeutralSplitRows() {
  const rowIndex = rowsById(buildPulseData());

  return neutralSplitGroups.flatMap((group, groupIndex) => {
    const sourceRows = readRowsForIds(
      rowIndex,
      group.sourceIds,
      `${group.group} source`,
    );
    const proofRows = readRowsForIds(rowIndex, group.proofIds, `${group.group} proof`);
    const sourceCount = sourceRows.filter(
      (row) => row.pulse_label === "counted_seam",
    ).length;
    const proofCount = proofRows.filter((row) => row.pulse_label === "anchor").length;

    return [
      {
        group: group.group,
        phase: "source seams",
        rowLabel: `${group.group} source`,
        count: sourceCount,
        order: groupIndex * 2,
        ids: group.sourceIds,
        pairs: sourceRows.map(
          (row) => `${row.nearest_swatch_name} -> ${row.replacement_shade_name}`,
        ),
      },
      {
        group: group.group,
        phase: "closed anchors",
        rowLabel: `${group.group} proof`,
        count: proofCount,
        order: groupIndex * 2 + 1,
        ids: group.proofIds,
        pairs: proofRows.map(
          (row) => `${row.nearest_swatch_name} -> ${row.replacement_shade_name}`,
        ),
      },
    ];
  });
}

function renderActiveFailSurfaceSplit() {
  const splitRows = buildNeutralSplitRows();
  const yDomain = splitRows.map((row) => row.rowLabel);
  const {window} = new JSDOM("<!DOCTYPE html>");

  const svg = Plot.plot({
    document: window.document,
    className: "huey-active-fail-surface-split",
    width: 820,
    height: 120 + yDomain.length * 30,
    marginTop: 56,
    marginRight: 76,
    marginBottom: 44,
    marginLeft: 188,
    style: {
      background: "#f6f5f2",
      color: "#26231f",
      fontFamily: "Inter, Arial, sans-serif",
      fontSize: 12,
    },
    x: {
      domain: [0, 3],
      label: "rows in pressure group",
      ticks: [0, 1, 2, 3],
      grid: true,
    },
    y: {
      domain: yDomain,
      label: null,
    },
    marks: [
      Plot.ruleX([0]),
      Plot.barX(splitRows, {
        x: "count",
        y: "rowLabel",
        fill: (row) => splitPhaseColours.get(row.phase),
        rx: 3,
        title: (row) =>
          `${row.group}\n${row.phase}: ${row.count}\nrows ${row.ids.join(
            ", ",
          )}\n${row.pairs.join("\n")}`,
      }),
      Plot.text(splitRows, {
        x: "count",
        y: "rowLabel",
        text: "count",
        dx: 10,
        fill: "#26231f",
        fontWeight: 700,
      }),
    ],
  });

  svg.setAttribute("xmlns", "http://www.w3.org/2000/svg");
  svg.setAttribute("role", "img");
  svg.setAttribute("aria-labelledby", "title desc");

  const title = window.document.createElementNS("http://www.w3.org/2000/svg", "title");
  title.setAttribute("id", "title");
  title.textContent = "Huemiliator neutral fail-surface split";

  const desc = window.document.createElementNS("http://www.w3.org/2000/svg", "desc");
  desc.setAttribute("id", "desc");
  desc.textContent =
    "Grouped bars pairing each neutral source seam group with the proof anchors that closed it.";

  svg.prepend(desc);
  svg.prepend(title);
  svg.append(buildSplitLegend(window.document));

  fs.writeFileSync(activeFailSurfaceSplitOutputPath, `${svg.outerHTML}\n`);
  console.log(`wrote ${path.relative(repoRoot, activeFailSurfaceSplitOutputPath)}`);
}

function buildArchiveIntegrityCells() {
  const archives = readParkedArchives();
  const aggregates = new Map();

  for (const archive of archives) {
    const rowFamilyCounts = d3.rollups(
      archive.rows,
      (items) => items.length,
      (row) => row.family ?? "unknown",
    );

    for (const [rowFamily, rowCount] of rowFamilyCounts) {
      const key = `${archive.archiveFamily}\0${rowFamily}`;
      if (!aggregates.has(key)) {
        aggregates.set(key, {
          archiveFamily: archive.archiveFamily,
          rowFamily,
          rows: 0,
          surfaces: new Set(),
          labels: new Set(),
        });
      }

      const aggregate = aggregates.get(key);
      aggregate.rows += rowCount;
      aggregate.surfaces.add(archive.file);
      aggregate.labels.add(archive.label);
    }
  }

  return familyOrder.flatMap((archiveFamily) =>
    familyOrder.map((rowFamily) => {
      const aggregate = aggregates.get(`${archiveFamily}\0${rowFamily}`);
      const rows = aggregate?.rows ?? 0;
      const surfaces = aggregate ? [...aggregate.surfaces] : [];
      return {
        archiveFamily,
        rowFamily,
        rows,
        surfaceCount: surfaces.length,
        sameFamily: archiveFamily === rowFamily,
        labels: aggregate ? [...aggregate.labels] : [],
        title:
          rows === 0
            ? `archive label: ${archiveFamily}\nrow truth: ${rowFamily}\nrows: 0`
            : `archive label: ${archiveFamily}\nrow truth: ${rowFamily}\nrows: ${rows}\nsurfaces: ${surfaces.length}\n${surfaces.join(
                "\n",
              )}`,
      };
    }),
  );
}

function renderArchiveIntegrityCheck() {
  const cells = buildArchiveIntegrityCells();
  const filledCells = cells.filter((cell) => cell.rows > 0);
  const maxRows = d3.max(filledCells, (cell) => cell.rows) ?? 1;
  const intensity = d3.scaleSqrt([1, maxRows], [0.2, 1]);
  const sameFill = d3.interpolateRgb("#dfeee8", "#287a68");
  const driftFill = d3.interpolateRgb("#f4d8d6", "#c34f4d");
  const {window} = new JSDOM("<!DOCTYPE html>");

  const svg = Plot.plot({
    document: window.document,
    className: "huey-archive-integrity-check",
    width: 860,
    height: 620,
    marginTop: 66,
    marginRight: 34,
    marginBottom: 88,
    marginLeft: 104,
    style: {
      background: "#f6f5f2",
      color: "#26231f",
      fontFamily: "Inter, Arial, sans-serif",
      fontSize: 12,
    },
    x: {
      domain: familyOrder,
      label: "archive label family",
      tickRotate: -35,
    },
    y: {
      domain: familyOrder,
      label: "row family truth",
    },
    marks: [
      Plot.cell(cells, {
        x: "archiveFamily",
        y: "rowFamily",
        fill: (cell) => {
          if (cell.rows === 0) {
            return "#ece8df";
          }
          return cell.sameFamily
            ? sameFill(intensity(cell.rows))
            : driftFill(intensity(cell.rows));
        },
        title: "title",
        inset: 1,
      }),
      Plot.text(filledCells, {
        x: "archiveFamily",
        y: "rowFamily",
        text: (cell) => cell.rows,
        fill: (cell) => (cell.rows > maxRows * 0.4 ? "#ffffff" : "#26231f"),
        fontWeight: 700,
      }),
      Plot.frame({stroke: "#d8d4cc"}),
    ],
  });

  svg.setAttribute("xmlns", "http://www.w3.org/2000/svg");
  svg.setAttribute("role", "img");
  svg.setAttribute("aria-labelledby", "title desc");

  const title = window.document.createElementNS("http://www.w3.org/2000/svg", "title");
  title.setAttribute("id", "title");
  title.textContent = "Huemiliator archive integrity check";

  const desc = window.document.createElementNS("http://www.w3.org/2000/svg", "desc");
  desc.setAttribute("id", "desc");
  desc.textContent =
    "A table heatmap comparing family tokens in parked archive labels with row-family truth from each archived eval surface.";

  svg.prepend(desc);
  svg.prepend(title);
  svg.append(buildArchiveIntegrityLegend(window.document));

  fs.writeFileSync(archiveIntegrityOutputPath, `${svg.outerHTML}\n`);
  console.log(`wrote ${path.relative(repoRoot, archiveIntegrityOutputPath)}`);
}

function buildArchiveIntegrityLegend(document) {
  const legend = document.createElementNS("http://www.w3.org/2000/svg", "g");
  legend.setAttribute("aria-label", "legend");
  legend.setAttribute("transform", "translate(104 22)");

  const items = [
    {label: "label matches row truth", fill: "#287a68"},
    {label: "label drift", fill: "#c34f4d"},
    {label: "no rows", fill: "#ece8df"},
  ];

  let x = 0;
  for (const item of items) {
    const square = document.createElementNS("http://www.w3.org/2000/svg", "rect");
    square.setAttribute("x", x);
    square.setAttribute("y", 0);
    square.setAttribute("width", 12);
    square.setAttribute("height", 12);
    square.setAttribute("rx", 2);
    square.setAttribute("fill", item.fill);
    legend.append(square);

    const text = document.createElementNS("http://www.w3.org/2000/svg", "text");
    text.setAttribute("x", x + 18);
    text.setAttribute("y", 10);
    text.setAttribute("font-size", 12);
    text.setAttribute("fill", "#26231f");
    text.setAttribute("text-anchor", "start");
    text.textContent = item.label;
    legend.append(text);

    x += item.label.length > 10 ? 176 : 86;
  }

  return legend;
}

function buildSplitLegend(document) {
  const legend = document.createElementNS("http://www.w3.org/2000/svg", "g");
  legend.setAttribute("aria-label", "legend");
  legend.setAttribute("transform", "translate(188 18)");

  let x = 0;
  for (const phase of splitPhaseOrder) {
    const square = document.createElementNS("http://www.w3.org/2000/svg", "rect");
    square.setAttribute("x", x);
    square.setAttribute("y", 0);
    square.setAttribute("width", 12);
    square.setAttribute("height", 12);
    square.setAttribute("rx", 2);
    square.setAttribute("fill", splitPhaseColours.get(phase));
    legend.append(square);

    const text = document.createElementNS("http://www.w3.org/2000/svg", "text");
    text.setAttribute("x", x + 18);
    text.setAttribute("y", 10);
    text.setAttribute("font-size", 12);
    text.setAttribute("fill", "#26231f");
    text.setAttribute("text-anchor", "start");
    text.textContent = phase;
    legend.append(text);

    x += 130;
  }

  return legend;
}

function buildLegend(document) {
  const legend = document.createElementNS("http://www.w3.org/2000/svg", "g");
  legend.setAttribute("aria-label", "legend");
  legend.setAttribute("transform", "translate(118 18)");

  let x = 0;
  for (const segment of segmentOrder) {
    const label = segmentLabels.get(segment);

    const square = document.createElementNS("http://www.w3.org/2000/svg", "rect");
    square.setAttribute("x", x);
    square.setAttribute("y", 0);
    square.setAttribute("width", 12);
    square.setAttribute("height", 12);
    square.setAttribute("rx", 2);
    square.setAttribute("fill", segmentColours.get(segment));
    legend.append(square);

    const text = document.createElementNS("http://www.w3.org/2000/svg", "text");
    text.setAttribute("x", x + 18);
    text.setAttribute("y", 10);
    text.setAttribute("font-size", 12);
    text.setAttribute("fill", "#26231f");
    text.setAttribute("text-anchor", "start");
    text.textContent = label;
    legend.append(text);

    x += 120;
  }

  return legend;
}

renderFamilyRangePalette();
renderEvalPulseStack();
renderResidueFamilyBars();
renderFamilyCountBars();
renderEdgeDensityHeatmap();
renderActiveFailSurfaceSplit();
renderArchiveIntegrityCheck();
