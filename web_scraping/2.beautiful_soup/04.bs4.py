# pip install beautifulsoup4 설치하기 (스크래핑위한 라이브러리)
# pip install lxml 설치하기 (구문분석 파서)

import requests
from bs4 import BeautifulSoup
url = "https://comic.naver.com/webtoon/weekday.nhn"
res = requests.get(url)
res.raise_for_status()

# html 문서를 lxml파서를 통해 BeautifulSoup 객체로 만든것.
soup = BeautifulSoup(res.text, "lxml")

# --------------------------------------------------------------------

# print(soup.title)  # soup 객체를 통해 엘리먼트 정보 접근할 수 있다.
# print(soup.title.get_text())
# print(soup.a)  # 첫번째로 발견되는 엘리먼트의 정보를 가져온다.
# print(soup.a.attrs)  # a 엘리먼트의 속성값 가져오기
# print(soup.a["href"])  # a 엘리먼트의 href 속성값 정보를 가져온다.

# --------------------------------------------------------------------

# soup객체에서 find 함수를 이용하면, 해당값 중 처음으로발견되는 엘리먼트가져온다.
# print(soup.find("a", attrs={"class": "Nbtn_upload"}))
# print(soup.find(attrs={"class": "Nbtn_upload"}))
# print(soup.find("li", attrs={"class": "rank01"}))

# rank1 = soup.find("li", attrs={"class": "rank01"})
# print(rank1.a)
# print(rank1.a.get_text())  # get_text() : 글자뽑기

# --------------------------------------------------------------------

# # 다음 형제 엘리먼트 뽑기 : next_sibling
# print(rank1.next_sibling)  # 개행문자있으면 안나올수있다. 두번써보기.
# print(rank1.next_sibling.next_sibling)
# rank2 = rank1.next_sibling.next_sibling
# rank3 = rank2.next_sibling.next_sibling
# print(rank3.a.get_text())

# --------------------------------------------------------------------

# # 이전 형제 엘리먼트 뽑기 : previous_sibling
# rank2 = rank3.previous_sibling.previous_sibling
# print(rank2.a.get_text())

# --------------------------------------------------------------------

# # 부모 엘리먼트 뽑기 : parent
# print(rank1.parent)

# --------------------------------------------------------------------

# 조건에 해당하는 next_sibling 찾기
# rank2 = rank1.find_next_sibling("li")
# print(rank2.a.get_text())
# rank3 = rank2.find_next_sibling("li")
# print(rank3.a.get_text())
# rank2 = rank3.find_previous_sibling("li")
# print(rank2.a.get_text())

# --------------------------------------------------------------------

# rank1 기준으로 다음 형제들을 모두 가져오기 : find_next_siblings
# print(rank1.find_next_siblings("li"))

# --------------------------------------------------------------------

webtoon = soup.find("a", text="외모지상주의")
print(webtoon)
