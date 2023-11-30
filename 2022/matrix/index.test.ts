import { describe, expect, it } from "vitest";
import { bfsPrint, shortestPathBinaryMatrix } from ".";

describe.only("matrix tests", () => {
  it.only("test 1", () => {
    const result = shortestPathBinaryMatrix([
      [0, 0, 0],
      [1, 1, 0],
      [1, 1, 1],
    ]);
    expect(result).toBe(-1);
  });

  // it("bfs print", () => {
  //   const result = bfsPrint([
  //     [1, 2, 3, 4],
  //     [5, 6, 7, 8],
  //     [9, 10, 11, 12],
  //     [13, 14, 15, 16],
  //   ]);
  //   expect(result).toEqual([
  //     1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16,
  //   ]);
  // });
});
