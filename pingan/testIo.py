from sys import stdin
from collections import Counter
team = []
while True:
    line = stdin.readline().strip()
    if line=='':
        break
    team.append(line)
s1 = team[0]
s2 = team[1]
print(s1)
print(s2)