import { input } from "./input";
import { describe, expect, it } from "vitest";
import { getScore, getScore2 } from ".";

describe("day 2", () => {
  it("puzzle 1", () => {
    const sampleInput = `A Y
    B X
    C Z`;
    const score = getScore(input);
    expect(score).toBe(12772);
  });

  it("puzzle 2", () => {
    const sampleInput = `A Y
    B X
    C Z`;
    const score = getScore2(input);
    expect(score).toBe(11618);
  });
});
