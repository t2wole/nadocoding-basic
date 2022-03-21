# 1명은 치킨, 3명은 커피 쿠폰을 받게 된다.

# 조건1: 댓글은 20명이 작성했고 아이디는 1 ~ 20이라 가정
# 조건2: 내용과 상관없이 무작위 추첨하되 중복불가
# 조건3: random 모듈의 shuffle과 sample을 사용

# 예제:
# -- 당첨자 발표 --
# 치킨 당첨자 : 1
# 커피 당첨자 : [2, 3, 4]
# -- 축하합니다  --
from random import*

users = range(1, 21)
users = list(users)
print(users)

shuffle(users)
print(users)

winners = sample(users, 4)
print(winners)

print("-- 당첨자 발표 --")
print("치킨 당첨자 : {0}".format(winners[0]))
print("커피 당첨자 : {0}".format(winners[1:]))
print("-- 축하합니다  --")

print("===============================================")

# 50명의 승객과 매칭 기회가 있을 때, 총 탑승 승객 수를 구하는 프로그램

# 조건1: 운행 소요 시간은 5분 ~ 50분 사이
# 조건2: 당신은 소요시간 15분 이하의 승객만 매칭한다.

# 예제:
# [o] 1번째 손님 (소요시간 : 15분)
# [ ] 2번째 손님 (소요시간 : 50분)
# [o] 3번째 손님 (소요시간 : 10분)
# ...
# [ ] 50번째 손님 (소요시간 : 16분)

# 총 탑승 승객 : 2분

count = 0

for i in range(1, 51):
    time = randrange(5, 51)
    if 5 <= time <= 15:
        print("[o] {0}번째 손님 (소요시간 : {1}분)".format(i, time))
        count += 1
    else:
        print("[ ] {0}번째 손님 (소요시간 : {1}분)".format(i, time))

print("총 탑승 승객 : {0}".format(count))

print("===============================================")

# 표준 체중 구하기

# 남자: 키 * 키 * 22
# 여자: 키 * 키 * 21

# 조건1: 함수명: std_weight
#        전달값: 키(height), 성별(gender)
# 조건2: 소수점 둘째자리까지 표시

# 예시:
# 키 175cm 남자의 표준 체중은 67.38kg 입니다.

def std_weight(height, gender):
    if gender == "남자":
        return height * height * 22
    else:
        return height * height * 21
    
height = 175
gender = "남자"
weight = round(std_weight(height / 100, gender), 2)
print("키 {0}cm {1}의 표준체중은 {2}kg입니다.".format(height, gender, weight))    