from random import *
from math import *

# 숫자형 자료형
print(5)
print(-10)
print(3.14)
print(1000)
print(5+3)
print(2*8)
print(3*(3+1))

# 문자형 자료형
print('풍선')
print("나비")
print("ㅋㅋㅋㅋㅋㅋㅋㅋㅋ")

# 숫자형, 문자형 섞어쓰기
print("ㅋ"*9)

# boolean 자료형
print(5 > 10)
print(5 < 10)
print(True)
print(False)
print(not True)
print(not False)
print(not (5 > 10))

# --------------------------------------------------------------------

# 변수
animal = "고양이"
name = "해피"
age = 4
hobby = "낮잠"
is_adult = age >= 3

print("우리집"+animal+"의 이름은"+name+"예요")
hobby = "공놀이"
# 콤마 , 로 + 대신 할 수 있지만 공백이 들어간다
print(name, "는 ", age, "살이며, ", hobby, "을 아주 좋아해요")
print(name + "는 어른일까요? " + str(is_adult))

'''이렇게하면
여러문장이
주석이됩니다.'''

# --------------------------------------------------------------------

# 연산자
print(2**3)  # 2^3 = 8
print(5 % 3)  # 나머지 = 2
print(5//3)  # 몫 = 1
print(3 == 3)  # 같다 = True
print(1 != 3)  # 같지않다 = True
print(not(1 != 3))  # False

print((3 > 0) and 3 < 5)  # True
print((3 > 0) & (3 < 5))  # True

print((3 > 0) or (3 > 5))  # True  둘중하나가 true면 true
print((3 > 0) | (3 > 5))  # True

# --------------------------------------------------------------------

# 숫자처리함수 math
# from math import *
print(abs(-5))  # 절대값 = 5
print(pow(4, 2))  # 4^2
print(max(5, 12))  # 12
print(min(5, 12))  # 5
print(round(3.5))  # 반올림 = 4
print(round(3.1497), 2)  # 소수점 2째자리까지 표시
print(floor(4.99))  # 내림 = 4
print(ceil(3.14))  # 올림 = 4
print(sqrt(16))  # 제곱근 = 4

# --------------------------------------------------------------------

# 랜덤함수 random
# from random import *
print(random())  # 0.0 ~ 1.0 미만의 임의 값 생성
print(random()*10)  # 0.0 ~ 10.0 미만의 임의 값 생성
print(int(random()*10))  # 0 ~ 10 미만의 임의값 생성
print(int(random()*10)+1)  # 1 ~ 10 이하의 임의값 생성
print(int(random()*45)+1)  # 1 ~ 45 이하의 임의의 값 생성
print(randrange(1, 45))  # 1 ~ 45 미만의 임의의 값 생성
print(randint(1, 45))  # 1 ~ 45 이하의 임의의 값 생성

# --------------------------------------------------------------------

sentence = """
파이썬은
쉬워요
"""
print(sentence)

# --------------------------------------------------------------------

# 슬라이싱
jumin = "990120-1234567"
print("성별 : " + jumin[7])
print("연 : " + jumin[0:2])  # 0 ~ 2 직전까지 (0, 1)
print("월 : " + jumin[2:4])
print("일 : " + jumin[4:6])
print("생년월일 : " + jumin[:6])  # 처음부터 6직전까지
print("뒤 7자리 : " + jumin[7:])  # 7부터 끝까지
print("뒤 7자리(뒤에부터) : " + jumin[-7:])  # 맨 뒤에서 7째부터 끝까지

# --------------------------------------------------------------------

# 문자열 처리함수
python = "Python is Amazing"
print(python.lower())  # 소문자 출력
print(python.upper())  # 대문자 출력
print(python[0].isupper())  # 대문자인지 확인
print(len(python))  # 길이 반환
print(python.replace("Python", "Java"))  # 단어 변경

index = python.index("n")  # n이 나온 위치 찾기
print(index)
index = python.index("n", index + 1)  # 6번째 문자 이후부터 n이 나온 위치 찾기
print(index)
# print(python.index("Java"))  # 찾을 수 없는 경우 에러가 난다.
print(python.find("Java"))  # 찾을 수 없는 경우 -1을 반환한다.
print(python.count("n"))  # n이 몇번 나왔는지 계산한다.

# --------------------------------------------------------------------

# 문자열 포맷
print("a"+"b")
print("a", "b")

# 방법 1
print("나는 %d살입니다." % 20)  # d는 정수값
print("나는 %s을 좋아해요." % "파이썬")  # s는 문자열
print("Apple은 %c로 시작해요." % "A")  # c는 caracter
print("나는 %s색과 %s색을 좋아해요" % ("파란", "빨간"))

# 방법 2
print("나는 {}살입니다.".format(20))
print("나는 {}색과 {}색을 좋아해요".format("파란", "빨간"))
print("나는 {0}색과 {1}색을 좋아해요".format("파란", "빨간"))  # 0번쨰, 1번째 넣기
print("나는 {1}색과 {0}색을 좋아해요".format("파란", "빨간"))  # 1번쨰, 0번째 넣기

# 방법 3
print("나는 {age}살이며, {color}색을 좋아해요.".format(age=20, color="빨간"))

# 방법 4 (v3.6 이상 ~)
age = 20
color = "빨간"
print(f"나는 {age}살이며, {color}색을 좋아해요.")

# --------------------------------------------------------------------

# 탈출문자

# \n : 줄바꿈
print("백문이 불여일견 \n백견이 불여일타")

# \" \' : 문장 내에서 따옴표
print("저는 \"이은영\"입니다.")
print("저는 \'이은영\'입니다.")

# \\ : 문장내에서 \
print("C:\\Users")

# \r : 커서를 맨앞으로 이동 (덮어쓰여진다.)
print("Red Apple\rPine")

# \b : 백스페이스 (한 글자 삭제)
print("Redd\bApple")

# \t : 탭
print("Red\tApple")
