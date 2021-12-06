import R from "ramda";

class Point {
  constructor(public x: number, public y: number) {}

  equals(other: Point) {
    return this.x === other.x;
  }

  key() {
    return `key-x${this.x}-y${this.y}`;
  }
}

type LineSegment = {
  start: Point;
  end: Point;
};

type LineDirection = "vertical" | "horizontal" | "diagonal";

const parseInput = (rawInput: string): LineSegment[] => {
  return rawInput
    .split("\n")
    .map((s) => s.trim())
    .map((line) =>
      line.split(" -> ").map((part) => part.split(",").map(Number))
    )
    .map((lineParts) => ({
      start: new Point(lineParts[0][0], lineParts[0][1]),
      end: new Point(lineParts[1][0], lineParts[1][1]),
    }));
};

const getLineDirection = (line: LineSegment): LineDirection =>
  line.start.x === line.end.x
    ? "horizontal"
    : line.start.y === line.end.y
    ? "vertical"
    : "diagonal";

    // yuk
const getPointsCoveredByLine =
  (includeDiagonals: boolean) =>
  (line: LineSegment): Point[] => {
    const lineDirection = getLineDirection(line);

    if (lineDirection === "horizontal") {
      const [start, end] =
        line.start.y < line.end.y
          ? [line.start, line.end]
          : [line.end, line.start];
      const points = [...Array(end.y - start.y + 1).keys()].map(
        (i) => new Point(start.x, start.y + i)
      );
      return points;
    }

    if (lineDirection === "vertical") {
      const [start, end] =
        line.start.x < line.end.x
          ? [line.start, line.end]
          : [line.end, line.start];

      const points = [...Array(end.x - start.x + 1).keys()].map(
        (i) => new Point(start.x + i, start.y)
      );
      return points;
    }

    if (includeDiagonals && lineDirection === "diagonal" ) {
      const pointCount =
        (line.start.x < line.end.x
          ? line.end.x - line.start.x
          : line.start.x - line.end.x) + 1;

      const points = [...Array(pointCount).keys()].map(
        (i) =>
          new Point(
            line.start.x < line.end.x ? line.start.x + i : line.start.x - i,
            line.start.y < line.end.y ? line.start.y + i : line.start.y - i
          )
      );

      return points;
    }

    return [];
  };

export const getPointsWithOverlappingLines = (
  rawInput: string,
  minimumOverlap: number,
  includeDiagonals: boolean = false
) => {
  const lineSegments = parseInput(rawInput);

  const countAboveMin = R.pipe(
    R.map<LineSegment, Point[]>(getPointsCoveredByLine(includeDiagonals)),
    R.flatten,
    R.groupBy((point) => point.key()),
    R.values,
    R.map((x) => x.length),
    R.filter<number>((x) => x >= minimumOverlap),
    R.length
  )(lineSegments);

  return countAboveMin;
};
