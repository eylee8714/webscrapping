import requests
from bs4 import BeautifulSoup
url = "https://comic.naver.com/webtoon/weekday.nhn"
res = requests.get(url)
res.raise_for_status()

# html 문서를 lxml파서를 통해 BeautifulSoup 객체로 만든것.
soup = BeautifulSoup(res.text, "lxml")

# 네이버 웹툰 전체 목록 가져오기
cartoons = soup.find_all("a", attrs={"class": "title"})

# 클래스 속성이 title인 모든 a 엘리먼트 반환
for cartoon in cartoons:
    print(cartoon.get_text())
