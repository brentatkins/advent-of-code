type Section = { start: number; end: number };

const splitIntoLines = (input: string) =>
  input.split(/\r?\n/).map((x) => x.trim());

const convertToSection = (input: string) => ({
  start: +input.substring(0, input.indexOf("-")),
  end: +input.substring(input.indexOf("-") + 1, input.length),
});

const isOverlap = (sections: Section[]) =>
  (sections[0].start <= sections[1].start &&
    sections[1].end <= sections[0].end) ||
  (sections[1].start <= sections[0].start &&
    sections[0].end <= sections[1].end);

const isAnyOverlap = (sections: Section[]) =>
  !(sections[0].end < sections[1].start || sections[1].end < sections[0].start);

export const getOverlap = (input: string) => {
  const lines = splitIntoLines(input)
    .map((line) => line.split(","))
    .map((sections) => sections.map(convertToSection))
    .filter(isOverlap);

  return lines.length;
};

export const getOverlap2 = (input: string) => {
  const lines = splitIntoLines(input)
    .map((line) => line.split(","))
    .map((sections) => sections.map(convertToSection))
    .filter(isAnyOverlap);

  return lines.length;
};
