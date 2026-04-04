# problem: 11022
# tier: bronze

# 테스트 케이스 개수 입력
T = int(input())

# 1부터 T까지 반복하며 형식에 맞춰 출력
for i in range(1, T + 1):
    # 두 정수 입력 및 변환
    A, B = map(int, input().split())
    # f-string을 이용한 결과 포맷팅 출력
    print(f"Case #{i}: {A} + {B} = {A + B}")