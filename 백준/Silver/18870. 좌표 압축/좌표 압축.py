import sys
import copy

n = int(sys.stdin.readline())

ns = list(map(int, sys.stdin.readline().split()))

ns2 = sorted(list(set(ns)))

index_map = {ns2[i]: i for i in range(len(ns2))}


for i in ns:
    print(index_map[i],end=' ')