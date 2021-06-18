import csv  # csv 파일 라이브러리 가져오기
import requests
from bs4 import BeautifulSoup

url = "https://finance.naver.com/sise/sise_market_sum.nhn?sosok=0&page="

# csv 파일로 저장
filename = "시가총액1-200.csv"
# newline=""은 자동 줄바꿈 없애기 | 엑셀파일을 열때 인코딩 문제가 생기면 encoding="utf-8-sig" 로 한다.
f = open(filename, "w", encoding="utf-8-sig", newline="")
writer = csv.writer(f)

# csv 파일 맨 윗줄에 추가하기
title = "N	종목명	현재가	전일비	등락률	액면가	시가총액	상장주식수	외국인비율	거래량	PER	ROE	토론실".split("\t")
print(type(title))
writer.writerow(title)

for page in range(1, 5):
    res = requests.get(url + str(page))
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")

    data_rows = soup.find("table", attrs={"class": "type_2"}).find(
        "tbody").find_all("tr")
    for row in data_rows:
        columns = row.find_all("td")
        if len(columns) <= 1:  # 의미없는 데이터 skip
            continue
        data = [column.get_text().strip()
                for column in columns]  # 1줄 for 문 | strip()은 양쪽공백 삭제
        # print(data)
        writer.writerow(data)  # csv 저장 : [] 리스트 형태로 넣어주어야한다.
