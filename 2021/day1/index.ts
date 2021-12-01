export const countMeasurementsLarger = (data: number[]) =>
  data.reduce(
    (acc, inc, index, source) => (inc > source[index - 1] ? acc + 1 : acc),
    0
  );

export const createSlidingWindows = (data: number[], _size: number) => data.reduce<number[]>((acc, inc, index, source) => {
  if (index > 1) {
    return  [...acc, inc + source[index - 1] + source[index - 2]]
  }
  return acc;
}, []);
