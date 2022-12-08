import { input } from "./input";
import { describe, expect, it } from "vitest";
import { calculate1, calculate2 } from ".";

const sampleInput = `30373
25512
65332
33549
35390`;

describe("day 7", () => {
  it("puzzle 1", () => {
    const result = calculate1(input);
    expect(result).toBe(1681);
  });

  it("puzzle 2", () => {
    const result = calculate2(input);
    expect(result).toBe(201684);
  });
});
