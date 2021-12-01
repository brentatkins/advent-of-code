import { countMeasurementsLarger } from ".";
import { input } from "../input/day1";

describe("day 1", () => {
  it("should match sample", () => {
    const sampleInput = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263];
    const result = countMeasurementsLarger(sampleInput);
    expect(result).toBe(7);
  });

  it("puzzle 1 result", () => {
    const result = countMeasurementsLarger(input);
    expect(result).toBe(1226);
  });
});
