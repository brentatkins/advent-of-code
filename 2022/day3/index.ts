const splitIntoLines = (input: string) =>
  input.split(/\r?\n/).map((x) => x.trim());

const splitIntoCompartments = (rucksack: string) => [
  rucksack.substring(0, rucksack.length / 2),
  rucksack.substring(rucksack.length / 2, rucksack.length),
];

const findItemsInBoth = (contents: string[]) =>
  Array.from(contents[0]).filter((char) => contents[1].indexOf(char) >= 0);

const getPriorityOfItem = (item: string) =>
  item?.toUpperCase() === item
    ? item?.charCodeAt(0) - 38
    : item?.charCodeAt(0) - 96;

export const calculatePriority = (input: string) => {
  const score = splitIntoLines(input)
    .map(splitIntoCompartments)
    .map(findItemsInBoth)
    .map((x) => getPriorityOfItem(x[0]))
    .reduce((acc, inc) => acc + inc, 0);

  return score;
};

const divideIntoGroups = (lines: string[]) =>
  lines.reduce<string[][]>((acc, inc, index) => {
    const [head, ...tail] = acc;
    return index % 3 === 0 ? [[inc], ...acc] : [[...head, inc], ...tail];
  }, []);

const findItemInAllGroups = (items: string[]) =>
  findItemsInBoth([findItemsInBoth([items[0], items[1]]).join(""), items[2]]);

export const calculatePriority2 = (input: string) => {
  const lines = splitIntoLines(input);
  const score = divideIntoGroups(lines)
    .map(findItemInAllGroups)
    .map((x) => getPriorityOfItem(x[0]))
    .reduce((acc, inc) => acc + inc, 0);
  return score;
};
