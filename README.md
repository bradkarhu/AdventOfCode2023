# Advent of Code 2023 - Python

## Setup

Install required dependencies
``` sh
brew install scarvalhojr/tap/aoc-cli
pip3 install -r requirements.txt
```

Save AOC session cookie to `~/.adventofcode.session` (see [instructions](https://github.com/scarvalhojr/aoc-cli?tab=readme-ov-file#session-cookie-))

Download AOC files (input.txt, puzzle.md) into each day's folder by running:
``` sh
python3 download.py
```

## Benchmarking
``` sh
python3 time_all.py
```

MacBook Pro M1 Max using Python 3.11.6

| Day | p1 cpu | p1 sec | p2 cpu | p2 sec |
| --- | --- | --- | --- | --- |
| 1 | 69% | 0.027 | 66% | 0.026 |
| 2 | 62% | 0.027 | 61% | 0.025 |
| 3 | 63% | 0.027 | 66% | 0.023 |
| 4 | 62% | 0.026 | 61% | 0.025 |
| 5 | 63% | 0.026 | --- | --- |
| 6 | 64% | 0.026 | 80% | 0.019 |
| 7 | 74% | 0.024 | 67% | 0.024 |
| 8 | 65% | 0.03 | 83% | 0.054 |
| 9 | 65% | 0.027 | 67% | 0.025 |
| 10 | 71% | 0.03 | 71% | 0.032 |
| 11 | 95% | 0.27 | 97% | 0.307 |
| 12 | 84% | 0.046 | 99% | 0.648 |
| 13 | 64% | 0.027 | 66% | 0.027 |
| 14 | 59% | 0.031 | 97% | 0.422 |
| 15 | 61% | 0.029 | 64% | 0.025 |
| 16 | 61% | 0.03 | 98% | 0.473 |
| 17 | 97% | 0.479 | 99% | 1.039 |
| 18 | 63% | 0.026 | 59% | 0.026 |
| 19 | 69% | 0.029 | 74% | 0.032 |
| 20 | 92% | 0.116 | 97% | 0.376 |
| 21 | 88% | 0.093 | 98% | 0.647 |
| Total | 71% | 1.4460 | 78% | 4.2750 |