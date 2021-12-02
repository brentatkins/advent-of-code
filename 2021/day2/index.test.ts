import { calculateXY, calculateXYAim, Direction } from ".";
import { input } from "../input/day2";

describe("day 1", () => {
  it("should match sample for puzzle 1", () => {
    const sampleInput: [Direction, number][] = [
      ["forward", 5],
      ["down", 5],
      ["forward", 8],
      ["up", 3],
      ["down", 8],
      ["forward", 2],
    ];
    const [x, y] = calculateXY(sampleInput);
    expect(x * y).toBe(150);
  });

  it("puzzle 1", () => {
    const [x, y] = calculateXY(input as [Direction, number][]);
    expect(x * y).toBe(1692075);
  });

  it("should match sample for puzzle 2", () => {
    const sampleInput: [Direction, number][] = [
      ["forward", 5],
      ["down", 5],
      ["forward", 8],
      ["up", 3],
      ["down", 8],
      ["forward", 2],
    ];
    const [x, y] = calculateXYAim(sampleInput);
    expect(x * y).toBe(900);
  });

  it("puzzle 2", () => {
    const [x, y] = calculateXYAim(input as [Direction, number][]);
    expect(x * y).toBe(1749524700);
  });
});
