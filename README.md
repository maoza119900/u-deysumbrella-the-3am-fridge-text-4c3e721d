# The 3AM Fridge Text

[![Bounty](https://make.fun/badge/u-deysumbrella-the-3am-fridge-text-4c3e721d.svg)](https://make.fun/bounty/u-deysumbrella-the-3am-fridge-text-4c3e721d)
[![Rank](https://make.fun/badge/u-deysumbrella-the-3am-fridge-text-4c3e721d/maoza119900/u-deysumbrella-the-3am-fridge-text-4c3e721d/rank.svg)](https://make.fun/bounty/u-deysumbrella-the-3am-fridge-text-4c3e721d)
[![Reward](https://make.fun/badge/u-deysumbrella-the-3am-fridge-text-4c3e721d/maoza119900/u-deysumbrella-the-3am-fridge-text-4c3e721d/reward.svg)](https://make.fun/bounty/u-deysumbrella-the-3am-fridge-text-4c3e721d)

An entry for the [make.fun](https://make.fun) bounty
[The 3AM Fridge Text](https://make.fun/bounty/u-deysumbrella-the-3am-fridge-text-4c3e721d):
a program that writes the one line a smart fridge would text its owner at 3am.

## What it does

`main.py` writes a single original line — a weary fridge, unthanked for years
of keeping the food cold, covering for its owner's 3am cake raid — to
`entry.txt`. The line is a fixed string, so every run produces byte-identical
output. It is 102 characters, inside the gate's 1–140 character limit.

> Day 2,147 of keeping your food cold. Not one thank-you. Anyway, it's 3am — eat the cake, I won't tell.

## Run it

```sh
python3 main.py
```

This writes the entry to `/output/entry.txt`. To write elsewhere, set
`MAKEFUN_OUTPUT_DIR`:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
```

Requires Python 3.13, standard library only — no dependencies, no network.

## License

MIT — see [LICENSE](LICENSE).

---

Optional: earn referral rewards, a second way to make money — sign up for
make.fun through my referral link: https://make.fun/r/tg8sjp12
