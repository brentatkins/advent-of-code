import { getPointsWithOverlappingLines } from ".";
import { input } from "../input/day5";
import { describe, expect, it } from 'vitest'

describe("day 5", () => {
  it("should match sample for puzzle 1", () => {
    const sampleInput = `0,9 -> 5,9
    8,0 -> 0,8
    9,4 -> 3,4
    2,2 -> 2,1
    7,0 -> 7,4
    6,4 -> 2,0
    0,9 -> 2,9
    3,4 -> 1,4
    0,0 -> 8,8
    5,5 -> 8,2`;

    const score = getPointsWithOverlappingLines(sampleInput, 2);
    expect(score).toBe(5);
  });

  it("puzzle 1", () => {
    const score = getPointsWithOverlappingLines(input, 2);
    expect(score).toBe(6007);
  });

  it("should match sample for puzzle 2", () => {
    const sampleInput = `0,9 -> 5,9
    8,0 -> 0,8
    9,4 -> 3,4
    2,2 -> 2,1
    7,0 -> 7,4
    6,4 -> 2,0
    0,9 -> 2,9
    3,4 -> 1,4
    0,0 -> 8,8
    5,5 -> 8,2`;

    const score = getPointsWithOverlappingLines(sampleInput, 2, true);
    expect(score).toBe(12);
  });

  it("puzzle 2", () => {
    const score = getPointsWithOverlappingLines(input, 2, true);
    expect(score).toBe(19349);
  });
});
