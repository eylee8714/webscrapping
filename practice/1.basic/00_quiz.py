from random import *
count = 0
for customer in range(1, 51):
    time = randrange(5, 51)  # 5 ~ 51 미만의 임의의 값 생성
    if 5 <= time <= 15:
        print("[O] {0}번째 손님 (소요시간 : {1}분)".format(customer, time))
        count += 1
    else:
        print("[ ] {0}번째 손님 (소요시간 : {1}분)".format(customer, time))
print("총 탑승 승객 : {0}분".format(count))


print("--------------------------------------------------")


def std_weight(height, gender):
    if gender == "male":
        return height * height * 22

    else:
        return height * height * 21


height = 175
gender = "male"
weight = round(std_weight(height / 100, gender), 2)
print("키 {0} {1}의 표준체중은 {2}kg입니다.".format(height, gender, weight))

print("--------------------------------------------------")

# 50 개의 보고서 파일 만들기
for week in range(1, 51):
    with open("{0}주차.txt".format(week), "w", encoding="utf8") as week_file:
        week_file.write(" - {0}주차 주간보고 - ".format(week))
        week_file.write("\n부서 :")
        week_file.write("\n이름 :")
        week_file.write("\n업무 요약 :")
