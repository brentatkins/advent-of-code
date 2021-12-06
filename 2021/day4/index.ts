// type BingoNumbers = number[];
type BingoCard = { number: number; bingoed: boolean }[][];
type Winner = { number: number; card: BingoCard };
export type FirstToWin = "first-to-win";
export type LastToWin = "last-to-win";

type WinningStrategy = FirstToWin | LastToWin;

const convertIntutNumbers = (input: string) => input.split(",").map(Number);

const transpose = (card: BingoCard) =>
  card[0].map((_, index) => card.map((row) => row[index]));

const buildBingoCardFromInput = (input: string) =>
  input.split("\n").map((row) =>
    row
      .split(" ")
      .filter((x) => x !== "")
      .map(Number)
      .map((number) => ({ number, bingoed: false }))
  );

const markCard = (card: BingoCard, number: number): BingoCard =>
  card.map((row) =>
    row.map((x) => (x.number === number ? { number, bingoed: true } : x))
  );

const isCardAWinner = (card: BingoCard) =>
  card.some((row) => row.map((x) => x.bingoed).every((x) => x)) ||
  transpose(card).some((column) =>
    column.map((x) => x.bingoed).every((x) => x)
  );

const getCardScore = (card: BingoCard) =>
  card
    .flatMap((row) => row.filter((x) => !x.bingoed).map((x) => x.number))
    .reduce((x, y) => x + y);

const findWinners = (
  draw: number[],
  bingoCards: BingoCard[],
  winners: Winner[] = []
): Winner[] => {
  const [number, ...remainingDraw] = draw;

  if (number === undefined) {
    return winners;
  }

  const markedCards = bingoCards
    .map((card) => markCard(card, number))
    .map((card) => ({ isWinner: isCardAWinner(card), card }));
  const thisRoundWinners = markedCards
    .filter((x) => x.isWinner)
    .map((x) => ({ number, card: x.card }));
  const nonWinners = markedCards.filter((x) => !x.isWinner).map((x) => x.card);

  return findWinners(remainingDraw, nonWinners, [
    ...winners,
    ...thisRoundWinners,
  ]);
};

export const calculateBingoScore = (
  rawInput: string,
  _strategy: WinningStrategy = "first-to-win"
) => {
  const [drawString, ...rawInputCards] = rawInput.split("\n\n");

  const draw = convertIntutNumbers(drawString);
  const cards = rawInputCards.map(buildBingoCardFromInput);

  const winners = findWinners(draw, cards);

  if (winners.length > 0) {
    switch (_strategy) {
      case "first-to-win":
        return winners[0].number * getCardScore(winners[0].card);
      case "last-to-win":
        return (
          winners[winners.length - 1].number *
          getCardScore(winners[winners.length - 1].card)
        );
    }
  }

  return 0;
};
