# problem: 11021
# tier: bronze

# 테스트 케이스 개수 입력
T = int(input())

# 1부터 T까지 순회하며 합계 계산
for i in range(1, T + 1):
    # 두 정수 입력 및 변환
    A, B = map(int, input().split())
    # Case 번호와 두 수의 합 출력
    print(f"Case #{i}: {A + B}")