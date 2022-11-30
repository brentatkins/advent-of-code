import {countLanternFish} from ".";
import {input} from "../input/day6";
import { describe, expect, it } from 'vitest'

describe("day 6", () => {
    it("should match sample for puzzle 1", () => {
        const sampleInput = [3, 4, 3, 1, 2];

        const result = countLanternFish(sampleInput, 80);
        expect(result).toBe(5934);
    });

    it("puzzle 1", () => {

        const result = countLanternFish(input, 80);
        expect(result).toBe(386640);
    });

    it("should match sample for puzzle 1", () => {
        const sampleInput = [3, 4, 3, 1, 2];

        const result = countLanternFish(sampleInput, 256);
        expect(result).toBe(26984457539);
    });

    it("puzzle 2", () => {
        const result = countLanternFish(input, 256);
        expect(result).toBe(1733403626279);
    });
});
