const splitIntoLines = (input: string) => input.split(/\r?\n/);

const getBefore = (row: number[], col: number) => row.slice(0, col);
const getAfter = (row: number[], col: number) => row.slice(col + 1, row.length);

export const calculate1 = (input: string) => {
  const lines = splitIntoLines(input);

  const visibleOnEdge = lines[0].length * 2 + (lines.length - 2) * 2;

  const treeGrid = lines.map((line) => line.split("").map(Number));

  let visibleInterior = 0;
  for (let row = 1; row < treeGrid.length - 1; row++) {
    const line = treeGrid[row];

    for (let col = 1; col < treeGrid.length - 1; col++) {
      const tree = line[col];
      const isSmallerThanMe = (x: number) => x < tree;

      const thisColumn = treeGrid.map((x) => x[col]);

      const visibleLeft = () => getBefore(line, col).every(isSmallerThanMe);
      const visibleRight = () => getAfter(line, col).every(isSmallerThanMe);

      const visibleUp = () => getBefore(thisColumn, row).every(isSmallerThanMe);
      const visibleDown = () =>
        getAfter(thisColumn, row).every(isSmallerThanMe);

      if (visibleUp() || visibleDown() || visibleLeft() || visibleRight()) {
        visibleInterior++;
      }
    }
  }

  return visibleOnEdge + visibleInterior;
};

const getScore = (trees: number[], tree: number) => {
  const indexOfBlocker = trees.findIndex((x) => x >= tree);
  return indexOfBlocker === -1 ? trees.length : indexOfBlocker + 1;
};

const max = (a: number, b: number) => Math.max(a, b);

export const calculate2 = (input: string) => {
  const lines = splitIntoLines(input);
  const treeGrid = lines.map((line) => line.split("").map(Number));

  const scores: number[][] = [];
  for (let row = 1; row < treeGrid.length - 1; row++) {
    const line = treeGrid[row];
    if (!scores[row]) {
      scores[row] = [];
    }
    for (let col = 1; col < treeGrid.length - 1; col++) {
      const tree = line[col];
      const thisColumn = treeGrid.map((x) => x[col]);

      const left = getScore(getBefore(line, col).reverse(), tree);
      const right = getScore(getAfter(line, col), tree);
      const up = getScore(getBefore(thisColumn, row).reverse(), tree);
      const down = getScore(getAfter(thisColumn, row), tree);

      scores[row][col] = left * right * up * down;
    }
  }
  const maxScore = scores.map((rows) => rows.reduce(max)).reduce(max);
  return maxScore;
};
