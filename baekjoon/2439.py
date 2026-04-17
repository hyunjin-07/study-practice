# problem: 2439
# tier: bronze

# 별의 개수(N) 입력
N = int(input())

# 1부터 N까지 반복하며 별 찍기
for i in range(1, N + 1):
    # 공백은 (N-i)개, 별은 i개 출력하여 오른쪽 정렬 구현
    print(" " * (N - i) + "*" * i)