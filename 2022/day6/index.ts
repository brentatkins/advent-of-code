export const getMarker = (input: string, start: number) => {
  let buffer: string[] = input.substring(0, start).split("");

  for (let i = start; i < input.length; i++) {
    const [_, ...tail] = buffer;
    buffer = [...tail, input[i]];

    if (new Set(buffer).size === buffer.length) {
      return i + 1;
    }
  }

  throw Error("No marker found");
};
