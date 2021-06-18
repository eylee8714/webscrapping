import requests
from bs4 import BeautifulSoup


for year in range(2015, 2020):
    url = "https://search.daum.net/search?nil_suggest=btn&w=tot&DA=SBC&q={}%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84".format(
        year)
    res = requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")
    images = soup.find_all("img", attrs={"class": "thumb_img"})

    for idx, image in enumerate(images):  # for문에서 idx 사용할 때 enumerate 쓴다.
        # print(image["src"])
        image_url = image["src"]
        if image_url.startswith("//"):  # //로 시작하는 데이터는 https 붙이기
            image_url = "https:" + image_url

        print(image_url)

        # img 를 jpg 파일로 저장하기
        image_res = requests.get(image_url)
        image_res.raise_for_status()

        # 이미지는 텍스트 아닌데이터라서 wb 붙인다.
        with open("movie_{}_{}.jpg".format(year, idx+1), "wb") as f:
            # image_res 가 가진 content 정보를 write 파일로 쓴다.
            f.write(image_res.content)

        if idx >= 4:  # 상위 5개 이미지 까지만 다운로드
            break
