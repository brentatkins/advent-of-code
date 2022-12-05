import { input } from "./input";
import { describe, expect, it } from "vitest";
import { calculate1, calculate2 } from ".";

const sampleInput = `    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2`;

describe("day 5", () => {
  it("puzzle 1", () => {
    const topStack = calculate1(input);
    expect(topStack).toBe('RTGWZTHLD');
  });

  it("puzzle 1 sample", () => {
    const topStack = calculate1(sampleInput);
    expect(topStack).toBe('CMZ');
  });

  it("puzzle 2", () => {
    const topStack = calculate2(input);
    expect(topStack).toBe('STHGRZZFR');
  });
});
