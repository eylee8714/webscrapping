for waiting_no in [0, 1, 2, 3, 4]:
    print("대기번호 : {0}".format(waiting_no))


print("--------------------------------------------------")

# randrange()
for waiting_no in range(1, 6):  # 1, 2, 3, 4, 5
    print("대기번호 : {0}".format(waiting_no))

print("--------------------------------------------------")

starbucks = ["아이언맨", "토르", "아이엠 그루트"]
for customer in starbucks:
    print("{0}, 커피가 준비되었습니다.".format(customer))

print("--------------------------------------------------")

# 출석번호가 1, 2, 3, 4 앞에 100을 붙이기로 함 -> 101, 102, 103, 104
students = [1, 2, 3, 4, 5]
print(students)
students = [i+100 for i in students]
print(students)

print("--------------------------------------------------")

# 학생 이름을 길이로 변환
students = ["Iron man", "Thor", "I am groot"]
students = [len(i) for i in students]
print(students)

print("--------------------------------------------------")

# 학생 이름을 대문자로 변환
students = ["Iron man", "Thor", "I am groot"]
students = [i.upper() for i in students]
print(students)


print("--------------------------------------------------")
# for문에서 idx 사용할 때 enumerate 쓴다.
# web_scraping 09_daum_movies.py 에 코드 있다.
# for idx, image in enumerate(images):
