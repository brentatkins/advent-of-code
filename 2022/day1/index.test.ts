import { input } from "./input";
import { describe, expect, it } from "vitest";
import { getTotals } from ".";

describe("day 1", () => {
  it("puzzle 1", () => {
    const totals = getTotals(input);
    const max = Math.max(...totals);
    expect(max).toBe(71506);
  });

  it("puzzle 2", () => {
    const totals = getTotals(input);
    totals.sort().reverse();
    const [top1, top2, top3] = totals;
    expect(top1 + top2 + top3).toBe(209603);
  });
});
