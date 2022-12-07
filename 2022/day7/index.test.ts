import { input } from "./input";
import { describe, expect, it } from "vitest";
import { calculate1, calculate2 } from ".";

const sampleInput = `$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k`



describe("day 7", () => {
  it("puzzle 1", () => {
    const result = calculate1(input)
    expect(result).toBe(1432936);
  });

  it("puzzle 2", () => {
    const result = calculate2(input)
    expect(result).toBe(272298);
  });
});
