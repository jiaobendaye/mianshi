# -*- coding: utf-8 -*-

from sys import stdin
import collections
import heapq


if __name__ == "__main__":

    team = []
    while True:
        line = stdin.readline().strip()
        if line=='':
            break
        item = line.split()
        item = [int(i) for i in item]
        team.append(item)
            
    print(team)