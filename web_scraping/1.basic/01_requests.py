'''
웹 스크래핑 : 웹페이지에서 원하는 부분만 떼오는 것
웹 크롤링 : 웹페이지내에 있는 링크들을 따라가면서 모든 내용을 가져오는 것
'''



# requests 라이브러리 설치
# pip install requests

import requests
res = requests.get("http://google.com")
res.raise_for_status()  # 문제가 생겼을때, 오류가 생기고 프로그램 끝낸다..


''' 
# res.raize_for_status() 한줄이면 밑에 줄 안적어도된다.

# print("응답코드 : ", res.status_code)  # 200 정상

# if res.status_code == requests.codes.ok:
#     print("정상입니다.")
# else:
#     print("문제가 생겼습니다. [에러코드", res.status_code, "]")

#'''


print(len(res.text))  # 받아온 html 글자갯수 확인
# print(res.text) # 받아온 html 내용 확인

# 받아온 html 파일로 생성
with open("mygoogle.html", "w", encoding="utf8") as f:
    f.write(res.text)
