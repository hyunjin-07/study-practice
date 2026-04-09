# problem: 5597
# tier: bronze

# 출석부 초기화 (1~30번)
arr = [0] * 31

# 제출자 28명 체크
for _ in range(28):
    num = int(input())
    arr[num] = 1

# 미제출자 번호 출력
for i in range(1, 31):
    if arr[i] == 0:
        print(i)