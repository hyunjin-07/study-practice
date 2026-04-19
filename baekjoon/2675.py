# problem: 2675
# tier: bronze

# 테스트 케이스 개수 T 입력
T = int(input())

for _ in range(T):
    # 반복 횟수 R과 문자열 S 입력
    R, S = input().split()
    R = int(R)
    
    # 각 문자를 R번 반복하여 새로운 문자열 생성
    P = ""
    for char in S:
        P += char * R
    
    # 결과 출력
    print(P)