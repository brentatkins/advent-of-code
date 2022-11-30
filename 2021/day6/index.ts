import * as R from "ramda";

export const countLanternFish = (ages: number[], days: number) => {
  const agesObject = R.pipe(
    R.groupBy((x) => `${x}`),
    R.mapObjIndexed((x) => x.length)
  )(ages);
  const aged = timeMachine(agesObject, days);
  const totalFish = R.pipe(R.values, R.sum)(aged);
  return totalFish;
};

const ageLanternFish = (
  ages: Record<string, number>
): Record<string, number> => {
  return {
    "8": ages["0"] ?? 0,
    "7": ages["8"] ?? 0,
    "6": (ages["7"] ?? 0) + (ages["0"] ?? 0),
    "5": ages["6"] ?? 0,
    "4": ages["5"] ?? 0,
    "3": ages["4"] ?? 0,
    "2": ages["3"] ?? 0,
    "1": ages["2"] ?? 0,
    "0": ages["1"] ?? 0,
  };
};

const timeMachine = (
  ages: Record<string, number>,
  days: number
): Record<string, number> =>
  days === 0 ? ages : timeMachine(ageLanternFish(ages), days - 1);
