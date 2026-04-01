# Problem: 2439
# Tier: Bronz

A = int(input())

for i in range(1, A + 1):
    A -= 1
    print((" ") * A + ("*") * i)