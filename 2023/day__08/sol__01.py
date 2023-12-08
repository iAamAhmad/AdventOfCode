import re
from itertools import cycle
from math import lcm
file_path = "2023\day__08\input.txt"

with open(file_path) as f:
    ws = [re.findall("\w+", l) for l in f.read().strip().split("\n")]

dirs = ws[0][0]
left = {start: l for start, l, _ in ws[2:]}
right = {start: r for start, _, r in ws[2:]}


def length(here, part1):
    for i, d in enumerate(cycle(dirs)):
        here = (left if d == "L" else right)[here]
        if (part1 and here == "ZZZ") or (not part1 and here[-1] == "Z"):
            return i + 1


# Part 1
print(length("AAA", True))

# Part 2
starts = [start for start, _, _ in ws[2:] if start[-1] == "A"]
print(lcm(*(length(start, False) for start in starts)))