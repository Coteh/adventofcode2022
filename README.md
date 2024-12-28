# adventofcode2022

[![CI](https://github.com/Coteh/adventofcode2022/actions/workflows/ci.yml/badge.svg)](https://github.com/Coteh/adventofcode2022/actions/workflows/ci.yml)

These are my solutions for [Advent of Code (AoC) 2022](https://adventofcode.com/2022).

Like last year, I wanted to pick a language I was familiar with and focus on the challenges. So I went with Python.

## Running the Solutions

First, [`pytest`](https://docs.pytest.org/en/stable/index.html) will need to be installed to run some of the tests:

```sh
pip install pytest
```

Each day is implemented in a separate file.

You can run them like this:

```sh
./<day>/<day>.py ./<day>/<input file name>
```

Example:

```
./01/01.py ./01/input
```

To run the test suite:

```
./test.sh
```

## Progress

| Day  | Part 1 | Part 2 |
|------|--------|--------|
|  1   |   ✅   |   ✅   |
|  2   |   ✅   |   ✅   |
|  3   |   ✅   |   ✅   |
|  4   |   ✅   |   ✅   |
|  5   |   ✅   |   ✅   |
|  6   |   ✅   |   ✅   |
|  7   |   ✅   |   ✅   |
|  8   |   ✅   |   ✅   |
|  9   |   ✅   |   ✅   |
|  10  |   ✅   |   ✅   |
|  11  |   ✅   |   ✅*  |
|  12  |        |        |
|  13  |   ✅   |   ✅   |
|  14  |        |        |
|  15  |        |        |
|  16  |        |        |
|  17  |        |        |
|  18  |        |        |
|  19  |        |        |
|  20  |        |        |
|  21  |        |        |
|  22  |        |        |
|  23  |        |        |
|  24  |        |        |
|  25  |        |        |

\* I "cheated" for Day 11 Part 2 by looking at the subreddit for the technique that needed to be used to solve the problem. See the `NOTE` in `./11/11.py` for more details.
