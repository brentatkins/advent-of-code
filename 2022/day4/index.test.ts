import { input } from "./input";
import { describe, expect, it } from "vitest";
import { getOverlap, getOverlap2 } from ".";

const sampleInput = `2-4,6-8
2-3,4-5 
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8`;

describe("day 4", () => {
  it("puzzle 1", () => {
    const score = getOverlap(input);
    expect(score).toBe(567);
  });

  it("puzzle 1", () => {
    const score = getOverlap2(input);
    expect(score).toBe(907);
  });
});
