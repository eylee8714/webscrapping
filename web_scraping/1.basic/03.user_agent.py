# 접속하는 브라우저에 따라 userAgent 가 다르다.
# 구글에서 user agent string 검색
# https://www.whatismybrowser.com/detect/what-is-my-user-agent


import requests
url = "http://nadocoding.tistory.com"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"}
res = requests.get(url, headers=headers)
res.raise_for_status()  # 문제가 생겼을때, 오류가 생기고 프로그램 끝낸다..

with open("nadocoding.html", "w", encoding="utf8") as f:
    f.write(res.text)
