export type Direction = "forward" | "down" | "up";

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

export const calculateXYAim = (data: [Direction, number][]) =>
  data.reduce(
    (acc, inc) => {
      const [direction, amount] = inc;
      const [x, y, aim] = acc;
      switch (direction) {
        case "forward":
          return [x + amount, y + (aim * amount), aim];
        case "down":
          return [x, y, aim + amount];
        case "up":
          return [x, y, aim - amount];
        default:
          return acc;
      }
    },
    [0, 0, 0]
  );
