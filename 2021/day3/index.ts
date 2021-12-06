const trackOccurences = (counts: number[], reportedValue: string) => {
  return counts.map((count, i) =>
    reportedValue[i] === "1" ? count + 1 : count - 1
  );
};

const calculateMostLeastCommon = (
  data: string[],
  handleEquallyCommon: boolean = false
) => {
  const startingCounts = data[0].split("").map((_) => 0);
  const counts = data.reduce(trackOccurences, startingCounts);
  if (!handleEquallyCommon && counts.find((count) => count === 0)) {
    throw Error("Counts total of zero not supported");
  }
  const mostCommon = counts.map((count) => (count >= 0 ? 1 : 0)).join("");
  const leastCommon = counts.map((count) => (count < 0 ? 1 : 0)).join("");

  return [mostCommon, leastCommon];
};

export const calculateGammaEpsilon = (data: string[]) => {
  const [gamma, epsilon] = calculateMostLeastCommon(data);
  return [parseInt(gamma, 2), parseInt(epsilon, 2)];
};

export const calculateOxygenC02 = (data: string[]) => {
  const inner = (
    input: string[],
    position: number,
    reportMostCommon: boolean
  ): string => {
    if (input.length === 1) {
      return input[0];
    } else {
      const [mostCommon, leastCommon] = calculateMostLeastCommon(input, true);
      return inner(
        input.filter(
          (diagnostic) =>
            diagnostic[position] ===
            (reportMostCommon ? mostCommon[position] : leastCommon[position])
        ),
        position + 1,
        reportMostCommon
      );
    }
  };

  const co2Generator = inner(data, 0, true);
  const co2Scrubber = inner(data, 0, false);
  return [parseInt(co2Generator, 2), parseInt(co2Scrubber, 2)];
};
