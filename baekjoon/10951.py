# problem: 10951
# tier: bronze

import sys

# EOF(입력 종료)까지 반복하여 한 줄씩 읽기
for line in sys.stdin:
    # 읽어온 줄을 공백 기준으로 나눠 정수로 변환
    A, B = map(int, line.split())
    # 두 수의 합 출력
    print(A + B)