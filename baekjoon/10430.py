# problem: 10430
# tier: bronze

# 세 정수 A, B, C 입력 및 변환
A, B, C = map(int, input().split())

# (A+B)%C 계산 및 출력
print((A + B) % C)
# ((A%C) + (B%C))%C 계산 및 출력
print(((A % C) + (B % C)) % C)
# (A*B)%C 계산 및 출력
print((A * B) % C)
# ((A%C) * (B%C))%C 계산 및 출력
print(((A % C) * (B % C)) % C)