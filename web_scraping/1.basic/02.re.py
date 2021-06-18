# 정규식 : 정해진 형태를 의미하는 식
# 주민번호, 이메일주소, 차량번호, ip주소 ...

# 참고사이트 : https://www.w3schools.com/python/python_regex.asp
# 참고사이트2 : https://docs.python.org/3/library/re.html

# ----------------------------------------------------------------------------


import re  # 정규식 라이브러리 쓴다.

p = re.compile("ca.e")  # 원하는 형태로 컴파일한다.
# compile에 사용 되는 문자
# . : 하나의 문자
# ^ : 문자열의 시작 ^a 라고쓰면 a로 시작하는 단어를 찾는다.
# $ : 문자열의 끝 $a 라고쓰면 a로 끝나는 단어를 찾는다.


def print_match(m):
    if m:
        print("m.group():", m.group())  # 일치하는 문자열 반환
        print("m.string:", m.string)  # 입력받은 문자열 (함수가 아니고 변수이다.)
        print("m.start():", m.start())  # 일치하는 문자열의 시작 index
        print("m.end():", m.end())  # 일치하는 문자열의 끝 index
        print("m.span():", m.span())  # 일치하는 문자열의 시작 / 끝 index
    else:
        print("매칭되지 않음")


# m = p.match("careless")  # match : 주어진 문자열의 처음부터 일치하는지 확인
# print_match(m)

# m = p.search("good care")  # search : 주어진 문자열 중에 일치하는게 있는지 확인
# print_match(m)

# lst = p.findall("good care cafe")  # findall : 일치하는 모든 것을 "리스트" 형태로 반환
# print(lst)
