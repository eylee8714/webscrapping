'''
🔑팁 : 터미널에서 python 입력 후 , 
코드를 넣어서 바로 바로 가져온 값을 확인할수있다.
exit() 로 터미널에서 빠져나올 수 있다.

🔑팁 : 뷰티풀숩 한글문서
https://www.crummy.com/software/BeautifulSoup/bs4/doc.ko/
'''

import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/list.nhn?titleId=675554"
res = requests.get(url)
res.raise_for_status()

# html 문서를 lxml파서를 통해 BeautifulSoup 객체로 만든것.
soup = BeautifulSoup(res.text, "lxml")

# cartoons = soup.find_all("td", attrs={"class": "title"})
# title = cartoons[0].a.get_text()
# link = cartoons[0].a["href"]
# print(title)
# print("https://comic.naver.com"+link)

# 만화제목 + 링크 가져오기
# for cartoon in cartoons:
#     title = cartoon.a.get_text()
#     link = "https://comic.naver.com" + cartoon.a["href"]
#     print(title, link)

# 평점 가져오기
total_rates = 0
cartoons = soup.find_all("div", attrs={"class": "rating_type"})
for cartoon in cartoons:
    rate = cartoon.find("strong").get_text()
    print(rate)
    total_rates += float(rate)
print("전체 점수 : ", total_rates)
print("평균 점수 : ", total_rates / len(cartoons))
