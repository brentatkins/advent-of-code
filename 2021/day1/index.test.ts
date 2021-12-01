import { countMeasurementsLarger, createSlidingWindows } from ".";
import { input } from "../input/day1";

describe("day 1", () => {
  it("should match sample for puzzle 1", () => {
    const sampleInput = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263];
    const result = countMeasurementsLarger(sampleInput);
    expect(result).toBe(7);
  });

  it("puzzle 1 result", () => {
    const result = countMeasurementsLarger(input);
    expect(result).toBe(1226);
  });

  it("should match sample for puzzle 1", () => {
    const sampleInput = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263];
    const slidingWindowsOf3 = createSlidingWindows(sampleInput, 3);
    const result = countMeasurementsLarger(slidingWindowsOf3);
    expect(result).toBe(5);
  });

  it("puzzle 2 result", () => {
    const slidingWindowsOf3 = createSlidingWindows(input, 3);
    const result = countMeasurementsLarger(slidingWindowsOf3);
    expect(result).toBe(1252);
  });

});
