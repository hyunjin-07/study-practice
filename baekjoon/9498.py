# problem: 9498
# tier: bronze

# 시험 점수 입력
score = int(input())

# 점수대별 성적 출력
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")