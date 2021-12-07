import { getFuelCost } from ".";
import { input } from "../input/day7";

describe("day 7", () => {
  it("should match sample for puzzle 1", () => {
    const sampleInput = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14];
    const result = getFuelCost(sampleInput);
    expect(result).toBe(37);
  });

  it("puzzle 1", () => {
    const result = getFuelCost(input);
    expect(result).toBe(328318);
  });

  it("should match sample for puzzle 2", () => {
    const sampleInput = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14];
    const result = getFuelCost(sampleInput, 'incrementing');
    expect(result).toBe(168);
  });

  it("puzzle 2", () => {
    const result = getFuelCost(input, 'incrementing');
    expect(result).toBe(89791146);
  });
});
