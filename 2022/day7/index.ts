const splitIntoLines = (input: string) => input.split(/\r?\n/);
const sum = (a: number, b: number) => a + b;
const ascending = (a: number, b: number) => a - b;

const isCdCommand = (line: string) => line.startsWith("$ cd");
const isLsCommand = (line: string) => line.startsWith("$ ls");
const isDir = (line: string) => line.startsWith("dir");

const getFolderSizeTree = (input: string) => {
  const lines = splitIntoLines(input);
  const currentDir: string[] = [];
  let tree = { "/": 0 };

  for (const line of lines) {
    if (isCdCommand(line)) {
      const dir = line.substring(5, 100);
      if (dir === "..") {
        currentDir.pop();
      } else {
        currentDir.push(dir);
      }

      tree[currentDir.join(".")] = tree[currentDir.join(".")] || 0;
      continue;
    }

    if (isLsCommand(line) || isDir(line)) {
      continue;
    }

    const fileSize = parseInt(line.split(" ")[0]);

    // add to each folder in current dir path
    let path = "";
    for (const dir of currentDir) {
      path = path ? `${path}.${dir}` : dir;
      tree[path] += fileSize;
    }
  }

  return tree;
};

export const calculate1 = (input: string) => {
  const tree = getFolderSizeTree(input);
  const result = Object.values(tree)
    .filter((x) => x <= 100_000)
    .reduce(sum);
  return result;
};

export const calculate2 = (input: string) => {
  const tree = getFolderSizeTree(input);

  const minCleanup = 30_000_000 - (70_000_000 - tree["/"]);

  const [first, ..._] = Object.values(tree)
    .filter((x) => x > minCleanup)
    .sort(ascending);

  return first;
};
