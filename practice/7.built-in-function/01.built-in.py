# 내장함수 : 구글에서 python built in function 검색
#  https://docs.python.org/ko/3/library/functions.html


# input : 사용자 입력을 받는 함수
# language = input("무슨 언어를 좋아하세요?")
# print("{0}은 아주 좋은 언어입니다!".format(language))


# dir : 어떤 객체를 넘겨줬을 때 그 객체가 어떤 변수와 함수를 가지고 있는지 표시
import pickle  # 외장 함수
import random  # 외장 함수
print(dir())
print(dir(random))  # random. 점찍었을때 나오는 내용들과 유사한 내용들이 나온다.
lst = [1, 2, 3]
print(dir(lst))
name = "Jim"
print(dir(name))
