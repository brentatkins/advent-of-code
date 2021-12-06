import { calculateGammaEpsilon, calculateOxygenC02 } from ".";
import { input } from "../input/day3";

describe("day 3", () => {
  it("should match sample for puzzle 1", () => {
    const sampleInput = [
      "00100",
      "11110",
      "10110",
      "10111",
      "10101",
      "01111",
      "00111",
      "11100",
      "10000",
      "11001",
      "00010",
      "01010"]
    const [gamma, epsilon] = calculateGammaEpsilon(sampleInput);
    expect(gamma * epsilon).toBe(198);
  });

  it("puzzle 1", () => {
    const [gamma, epsilon] = calculateGammaEpsilon(input);
    expect(gamma * epsilon).toBe(2724524);
  });

  it("should match sample for puzzle 2", () => {
    const sampleInput = [
      "00100",
      "11110",
      "10110",
      "10111",
      "10101",
      "01111",
      "00111",
      "11100",
      "10000",
      "11001",
      "00010",
      "01010"]
    const [co2Rating, co2Scrubber] = calculateOxygenC02(sampleInput);
    expect(co2Rating * co2Scrubber).toBe(230);
  });

  it("puzzle 1", () => {
    const [co2Rating, co2Scrubber] = calculateOxygenC02(input);
    expect(co2Rating * co2Scrubber).toBe(2775870);
  });


});
