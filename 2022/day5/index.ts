const splitIntoLines = (input: string) => input.split(/\r?\n/);

const getParts = (input: string) => {
  const [stacks1, moves1] = input.split("\n\n");

  const stackLines = splitIntoLines(stacks1);
  const moveLines = splitIntoLines(moves1);

  const stacks: string[][] = [];

  for (const line of stackLines) {
    const chunks = line.match(/.{1,4}/g);
    for (const [i, chunk] of chunks!.entries()) {
      if (!stacks[i]) {
        stacks[i] = [];
      }
      if (chunk.trim()) {
        stacks[i].push(chunk[1]);
      }
    }
  }
  stacks.forEach((x) => x.reverse());

  const moves = moveLines
    .map((line) => line.match(/\d+/g)?.map((x) => parseInt(x)) as number[])
    .map(([count, from, to]) => ({ from, to, count }));

  return { stacks, moves };
};

export const calculate1 = (input: string) => {
  const { stacks, moves } = getParts(input);

  moves.forEach((move) => {
    for (let i = 0; i < move.count; i++) {
      const crate = stacks[move.from - 1].pop();
      stacks[move.to - 1].push(crate!);
    }
  });

  const topCrate = stacks.map((stack) => stack[stack.length - 1]).join("");
  return topCrate;
};

export const calculate2 = (input: string) => {
  const { stacks, moves } = getParts(input);

  moves.forEach(({ from, to, count }) => {
    const crates = stacks[from - 1].splice(
      stacks[from - 1].length - count,
      count
    );
    stacks[to - 1].push(...crates);
  });

  const topCrate = stacks.map((stack) => stack[stack.length - 1]).join("");
  return topCrate;
};
