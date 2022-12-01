export const getTotals = (input: string) => {
  const totals = input.split(/\r?\n/).reduce<number[]>((acc, inc) => {
    if (inc === "") {
      return [0, ...acc];
    }

    const [current, ...rest] = acc;
    return [(current ?? 0) + parseInt(inc), ...rest];
  }, []);

  return totals;
};
