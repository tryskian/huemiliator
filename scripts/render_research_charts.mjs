import {execFileSync} from "node:child_process";
import fs from "node:fs";
import path from "node:path";

import * as d3 from "d3";
import * as Plot from "@observablehq/plot";
import {JSDOM} from "jsdom";

const repoRoot = process.cwd();
const parkedDir = path.join(repoRoot, ".local", "parked");
const evalDb = path.join(repoRoot, ".local", "evals.sqlite");
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
      source === "live" ? " live" : ""
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
        label: `active ${liveFamily} proof surface ${d3.min(
          liveRows,
          (row) => row.id,
        )}..${d3.max(liveRows, (row) => row.id)}`,
        sequence: maxPulse + 1,
      }),
    );
  }

  return pulses.sort((left, right) => d3.ascending(left.sequence, right.sequence));
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
    text.textContent = label;
    legend.append(text);

    x += 120;
  }

  return legend;
}

renderEvalPulseStack();
renderResidueFamilyBars();
