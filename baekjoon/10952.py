# Problem: 10952
# Tier: Bronz

while True:
    
    A, B = map(int, input().split())
    
    if A == 0 and B == 0:
        break
    
    print(A + B)