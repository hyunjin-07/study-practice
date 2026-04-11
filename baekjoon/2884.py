# problem: 2884
# tier: bronze

# 시간(H), 분(M) 입력
H, M = map(int, input().split())

# 45분 앞당기기 로직
if M >= 45:
    M -= 45
else:
    # 0시인 경우 23시로, 그 외는 1시간 차감
    if H == 0:
        H = 23
    else:
        H -= 1
    # 부족한 분 계산 (60 - 45 + M)
    M += 15

# 결과 출력
print(H, M)