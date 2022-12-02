type play = "rock" | "paper" | "sciccors";

const winMap: Record<play, play> = {
  paper: "rock",
  rock: "sciccors",
  sciccors: "paper",
};

const opponentPlay: Record<"A" | "B" | "C", play> = {
  A: "rock",
  B: "paper",
  C: "sciccors",
};
const myPlay: Record<"X" | "Y" | "Z", play> = {
  X: "rock",
  Y: "paper",
  Z: "sciccors",
};

export const getScore = (input: string) => {
  const lines = input.split(/\r?\n/).map((x) => x.trim());

  const scores = lines
    .map((line) => ({
      theirs: opponentPlay[line[0]] as play,
      mine: myPlay[line[2]] as play,
    }))
    .map((line) => ({
      ...line,
      playScore: playScore(line.mine),
      winScore: winScore(line.theirs, line.mine),
    }));

  return scores
    .map((x) => x.playScore + x.winScore)
    .reduce((acc, inc) => acc + inc, 0);
};

export const getScore2 = (input: string) => {
  const lines = input.split(/\r?\n/).map((x) => x.trim());

  const scores = lines
    .map((line) => ({
      theirs: opponentPlay[line[0]] as play,
      mine: getMyPlay(
        opponentPlay[line[0]] as play,
        line[2] === "X" ? "lose" : line[2] === "Y" ? "draw" : "win"
      ),
    }))
    .map((line) => ({
      ...line,
      playScore: playScore(line.mine),
      winScore: winScore(line.theirs, line.mine),
    }));

  return scores
    .map((x) => x.playScore + x.winScore)
    .reduce((acc, inc) => acc + inc, 0);
};

const getMyPlay = (theirs: play, outcome: "win" | "draw" | "lose"): play => {
  switch (outcome) {
    case "win":
      return winMap[winMap[theirs]];
    case "lose":
      return winMap[theirs];
    case "draw":
      return theirs;
    default:
      const _exhaustiveCheck: never = outcome;
      return _exhaustiveCheck;
  }
};

const playScore = (play: play) =>
  play === "rock" ? 1 : play === "paper" ? 2 : 3;

const winScore = (theirs: play, mine: play): 0 | 3 | 6 => {
  if (theirs === mine) {
    return 3;
  }
  return winMap[mine] === theirs ? 6 : 0;
};
