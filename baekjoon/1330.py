# Problem: 1330
# Tier: Bronz

A, B = map(int, input().split())
if A > B:
    print(">")
elif A < B:
    print("<")
else:
    print("==")