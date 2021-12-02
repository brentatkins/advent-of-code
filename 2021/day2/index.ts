export type Direction = "forward" | "down" | "up";

type Instruction = [Direction, number];

type Position = {
  x: number;
  y: number;
  aim: number;
};

const part2Rules = ({ x, y, aim }: Position, instruction: Instruction) => {
  const [direction, amount] = instruction;

  switch (direction) {
    case "forward":
      return {
        aim,
        x: x + amount,
        y: y + aim * amount,
      };
    case "down":
      return { x, y, aim: aim + amount };
    case "up":
      return { x, y, aim: aim - amount };
    default:
      return { x, y, aim };
  }
};

export const calculateXY = (data: [Direction, number][]) =>
  data.reduce(
    (acc, inc) => {
      const [direction, amount] = inc;
      const [x, y] = acc;
      switch (direction) {
        case "forward":
          return [x + amount, y];
        case "down":
          return [x, y + amount];
        case "up":
          return [x, y - amount];
        default:
          return acc;
      }
    },
    [0, 0]
  );

export const calculateXYAim = (data: [Direction, number][]) => {
  const { x, y } = data.reduce(part2Rules, { x: 0, y: 0, aim: 0 });
  return [x, y];
};
