# problem: 2588
# tier: bronze

A = int(input())
B = int(input())

# B의 일의 자리와 A의 곱
print(A * (B % 10))

# B의 십의 자리와 A의 곱
print(A * ((B // 10) % 10))

# B의 백의 자리와 A의 곱
print(A * (B // 100))

# A와 B의 전체 곱
print(A * B)