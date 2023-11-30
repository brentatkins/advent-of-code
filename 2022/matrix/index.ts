export const shortestPathBinaryMatrix = (grid: number[][]): number => {
  type Q = [row: number, col: number, count: number];
  let q: Q[] = [];
  let visited = grid.map((x) => x.map((y) => false));
  let result = -1;

  const directions = [
    [-1, -1],
    [-1, 0],
    [-1, 1],
    [0, -1],
    [0, 1],
    [1, -1],
    [1, 0],
    [1, 1],
  ];

  if (grid[0][0] !== 0) {
    return result;
  }

  q.push([0, 0, 1]);

  while (q.length > 0) {
    const [row, col, count] = q.shift() as Q;

    if (
      Math.min(row, col) < 0 ||
      Math.max(row, col) >= grid.length ||
      visited[row][col] ||
      grid[row][col] !== 0
    ) {
      continue;
    }

    if (row === grid.length - 1 && col === grid.length - 1) {
      return count;
    }

    visited[row][col] = true;

    const brothers = directions.map(
      ([r, c]) => [row + r, col + c, count + 1] as Q
    );

    q.push(...brothers);
  }

  return result;
};

export const bfsPrint = (grid: number[][]): number[] => {
  let q: number[][] = [];
  let visited = grid.map((x) => x.map((y) => false));
  let result: number[] = [];

  q.push([0, 0]);
  visited[0][0] = true;

  while (q.length > 0) {
    const [row, col] = q[0];

    result.push(grid[row][col]);
    q.shift();

    const brothers = getAdjacentElements(grid, row, col);

    for (let [bRow, bCol] of brothers) {
      if (!visited[bRow][bCol]) {
        q.push([bRow, bCol]);
        visited[bRow][bCol] = true;
      }
    }
  }

  return result;
};

const getAdjacentElements = (grid: number[][], row: number, col: number) => {
  const top = row > 0 ? [row - 1, col] : undefined;
  const bottom = row < grid.length - 1 ? [row + 1, col] : undefined;
  const right = col < grid[row].length - 1 ? [row, col + 1] : undefined;
  const left = col > 0 ? [row, col - 1] : undefined;

  return [left, right, top, bottom].filter((x): x is number[] => !!x);
};
