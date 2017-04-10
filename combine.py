#!/usr/bin/env python

import json

with open('part1.json') as f:
  p1 = json.load(f)

with open('part2.json') as f:
  p2 = json.load(f)

p1['profiles'] += p2['profiles']

print(len(p1['profiles']))
with open('data.json', 'w') as f:
  json.dump(p1, f)
