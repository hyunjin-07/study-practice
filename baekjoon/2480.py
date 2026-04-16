# problem: 2480
# tier: bronze

# 세 개의 주사위 눈 입력
a, b, c = map(int, input().split())

if a == b == c:
    # 3개의 눈이 모두 같은 경우
    print(10000 + a * 1000)
elif a == b or a == c:
    # 2개의 눈이 같은 경우 (a가 포함된 경우)
    print(1000 + a * 100)
elif b == c:
    # 2개의 눈이 같은 경우 (b와 c가 같은 경우)
    print(1000 + b * 100)
else:
    # 모두 다른 눈이 나온 경우
    print(max(a, b, c) * 100)