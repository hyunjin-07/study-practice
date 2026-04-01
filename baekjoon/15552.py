# Problem: 15552
# Tier: Bronz

import sys

T = int(sys.stdin.readline())

for _ in range(T):
    A, B = map(int, sys.stdin.readline().split())
    print(A + B)