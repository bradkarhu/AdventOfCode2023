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
| 1 | 71% | 0.026 | 81% | 0.021 |
| 2 | 68% | 0.025 | 56% | 0.029 |
| 3 | 68% | 0.026 | 80% | 0.021 |
| 4 | 70% | 0.024 | 63% | 0.025 |
| 5 | 65% | 0.024 | 64% | 0.026 |
| 6 | 58% | 0.027 | 62% | 0.024 |
| 7 | 64% | 0.026 | 64% | 0.026 |
| 8 | 67% | 0.028 | 83% | 0.053 |
| 9 | 64% | 0.027 | 61% | 0.028 |
| 10 | 66% | 0.033 | 68% | 0.033 |
| 11 | 94% | 0.269 | 96% | 0.311 |
| 12 | 80% | 0.047 | 98% | 0.65 |
| 13 | 67% | 0.025 | 62% | 0.028 |
| 14 | 63% | 0.027 | 98% | 0.42 |
| 15 | 61% | 0.028 | 65% | 0.025 |
| 16 | 64% | 0.028 | 98% | 0.472 |
| 17 | 97% | 0.476 | 98% | 1.048 |
| 18 | 63% | 0.026 | 80% | 0.019 |
| 19 | 67% | 0.029 | 72% | 0.033 |
| 20 | 91% | 0.113 | 97% | 0.38 |
| 21 | 89% | 0.092 | 98% | 0.649 |
| Total | 71% | 1.4260 | 78% | 4.3210 |