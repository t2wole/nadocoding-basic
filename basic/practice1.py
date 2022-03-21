# 시험성적
scores = {"수학" : 0, "영어" : 50, "코딩" : 100}
for subjects, score in scores.items():
    print(subjects.ljust(3), str(score).rjust(3), sep=" : ")

print("===============================================")

# 은행대기순번
# 001 002 003 ...
for num in range(1, 21):
    print("대기번호 : " + str(num).zfill(3))

print("===============================================")

# 빈 자리는 빈공간으로, 오른쪽 정렬하되, 총 10자리 공간생성
print("{0: >10}".format(500))
# 양수는 +, 음수는 -
print("{0: >+10}".format(500))
print("{0: >+10}".format(-500))
# 왼쪽정렬하고, 빈칸으로 *로 채움
print("{0:*<10}".format(500))
# 3자리마다 콤마를 찍어주기
print("{0:,}".format(10000000000000))
# 3자리마다 콤마를 찍어주고, +- 부호도 붙이기
print("{0:+,}".format(10000000000000))
print("{0:+,}".format(-10000000000000))
# 소수점 출력
print("{0:.2f}".format(5/3))

print("===============================================")

score_file = open("score.txt", "w", encoding="utf8") # 쓰기
print("수학 : 0", file=score_file)
print("영어 : 50", file=score_file)
score_file.close()

score_file = open("score.txt", "a", encoding="utf8") # 이어쓰기
score_file.write("과학 : 60\n")
score_file.write("코딩 : 100")
score_file.close()