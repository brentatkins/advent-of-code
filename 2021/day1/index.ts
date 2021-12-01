export const countMeasurementsLarger = (data: number[]) =>
  data.reduce(
    (acc, inc, index, source) => (inc > source[index - 1] ? acc + 1 : acc),
    0
  );
