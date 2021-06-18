cabinet = {3: "유재석", 100: "김태호"}
# [ ]를 쓰거나 get을 이용해서 값을 나타낼 수 있다.
print(cabinet[3])
print(cabinet.get(3))

# [ ] 를 쓰면 값이 없는 경우, 에러나고 프로그램 종료된다.
# print(cabinet[5])

# get을 쓰면 값이 없는 경우, None 을 반환한다.
print(cabinet.get(5))
# 값이 없는 경우, None 대신 기본값 반환하기
print(cabinet.get(5, "사용가능"))

# in : 값이 있는지 확인
print(3 in cabinet)  # True
print(5 in cabinet)  # False

# string으로 키값 가능하다
cabinet = {"A-3": "유재석", "B-100": "김태호"}
print(cabinet["A-3"])
print(cabinet["B-100"])

# 새 손님 ( 추가하기 )
print(cabinet)
cabinet["A-3"] = "김종국"  # 원래있던 A-3 의 유재석이 김종국으로 바뀐다.
cabinet["C-20"] = "조세호"  # 새로운 키값은 추가된다.
print(cabinet)

# del : 간 손님 ( 지우기 )
del cabinet["A-3"]
print(cabinet)

# key 들만 출력
print(cabinet.keys())

# value 들만 출력
print(cabinet.values())

# key, value 쌍으로 출력
print(cabinet.items())

# 목욕탕 폐점 ( dictionary 지우기 )
cabinet.clear()
print(cabinet)
