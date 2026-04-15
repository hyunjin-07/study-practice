# problem: 25314
# tier: bronze

# 바이트 수(N) 입력
N = int(input())

# 4바이트당 "long "을 한 번씩 반복하고 마지막에 "int" 추가
# N은 항상 4의 배수라고 가정
print("long " * (N // 4) + "int")