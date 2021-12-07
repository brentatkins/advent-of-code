type FuelBurnRate = "constant" | "incrementing";

export const getFuelCost = (
  input: number[],
  burnRate: FuelBurnRate = "constant"
) => {
  const max = Math.max(...input);

  const lowestCost = [...Array(max).keys()].reduce((minimum, position) => {
    const cost = calculateFuelCost(input, position, burnRate);
    return cost < minimum ? cost : minimum;
  }, Infinity);
  return lowestCost;
};

const calculateFuelCost = (
  current: number[],
  target: number,
  burnRate: FuelBurnRate
) =>
  current
    .map((position) =>
      burnRate === "constant"
        ? Math.abs(position - target)
        : calcuateMovementCost(position, target)
    )
    .reduce((x, y) => x + y);

const calcuateMovementCost = (current: number, target: number) =>
  (Math.abs(target - current) * (Math.abs(target - current) + 1)) / 2;
