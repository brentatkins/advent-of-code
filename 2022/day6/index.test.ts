import { input } from "./input";
import { describe, expect, it } from "vitest";
import { getMarker } from ".";

describe("day 6", () => {
  it("puzzle 1", () => {
    const marker = getMarker(input, 4);
    expect(marker).toBe(1155);
  });

  it("puzzle 2", () => {
    const marker = getMarker(input, 14);
    expect(marker).toBe(2789);
  });
});
