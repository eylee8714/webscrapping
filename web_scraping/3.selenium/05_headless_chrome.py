# headless 크롬은 크롬창을 띄우지 않고 크롬을 쓸 수 있는, 백그라운드에서 작업한다. (빠른 성능)

from bs4 import BeautifulSoup

import requests
import time
from selenium import webdriver

# 🔑 options 를 추가해서 headless를 True 옵션을 준다.
options = webdriver.ChromeOptions()
options.headless = True
options.add_argument("window-size=1920x1080")  # 해상도값 넣어준다.
browser = webdriver.Chrome(options=options)
browser.maximize_window()

# 페이지
url = "https://play.google.com/store/movies/top"
browser.get(url)

# 지정한 위치로 스크롤 내리기 : 해상도 1920 x 1080 이라서  1080 위치로 스크롤 내리기
# browser.execute_script("window.scrollTo(0,1080)")


# 화면 가장 아래로 스크롤 내리기 : document.body.scrollHeight 현재 문서의 높이만큼 스크롤 내리기
# browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")

interval = 2  # 2초에 한번씩 스크롤 내림

# 현재 문서 높이를 가져와서 저장
prev_height = browser.execute_script("return document.body.scrollHeight")

# 반복 수행
while True:
    # 스크롤 가장 아래로 내림
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")

    # 페이지 로딩 대기
    time.sleep(interval)

    # 현재 문서 높이를 가져와서 저장
    curr_height = browser.execute_script("return document.body.scrollHeight")
    if curr_height == prev_height:
        break

    prev_height = curr_height

print("스크롤 완료")
# 🔑 스크롤 다 되었을 때의 headless크롬에서 확인하기 위해 스크린샷을 찍는다.
browser.get_screenshot_as_file("google_movie.png")


# 스크롤 완료된 페이지의 타이틀 엘리먼트 가져오기
soup = BeautifulSoup(browser.page_source, "lxml")

movies = soup.find_all("div", attrs={"class": ["Vpfmgd"]})
print(len(movies))

for movie in movies:
    title = movie.find("div", attrs={"class": "WsMG1c nnK0zc"}).get_text()

    # 할인 전 가격
    original_price = movie.find("span", attrs={"class": "SUZt4c djCuy"})
    if original_price:
        original_price = original_price.get_text()
    else:
        continue

    # 할인 된 가격
    price = movie.find(
        "span", attrs={"class": "VfPpfd ZdBevf i5DZme"}).get_text()

    # 링크
    link = movie.find("a", attrs={"class": "JC71ub"})["href"]
    # 올바른 링크 : https://play.google.com + link

    print(f"제목:{title}")
    print(f"할인 전 금액 :{original_price}")
    print(f"할인 후 금액 :{price}")
    print("링크:", "https://play.google.com"+link)
    print("-" * 100)

browser.quit()
