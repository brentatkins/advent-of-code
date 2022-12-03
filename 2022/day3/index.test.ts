import { input } from "./input";
import { describe, expect, it } from "vitest";
import { calculatePriority, calculatePriority2 } from ".";

const sampleInput = `vJrwpWtwJgWrhcsFMMfFFhFp
    jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
    PmmdzqPrVvPwwTWBwg
    wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
    ttgJtRGJQctTZtZT
    CrZsJsPPZsGzwwsLwLmpwMDw`;

describe("day 2", () => {
  it("puzzle 1", () => {
    const score = calculatePriority(input);
    expect(score).toBe(8349);
  });

  it("puzzle 2", () => {
    const score = calculatePriority2(input);
    expect(score).toBe(2681);
  });
});
