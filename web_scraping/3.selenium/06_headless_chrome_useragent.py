# headless 크롬은 크롬창을 띄우지 않고 크롬을 쓸 수 있는, 백그라운드에서 작업한다. (빠른 성능)

from bs4 import BeautifulSoup

import requests
import time
from selenium import webdriver

# 🔑 options 를 추가해서 headless를 True 옵션을 준다.
options = webdriver.ChromeOptions()
options.headless = True
options.add_argument("window-size=1920x1080")  # 해상도값 넣어준다.
# HeadlessChrome 을 사용하게되면, user-agent 값에 HeadlessChrome가 명시된다. 이걸 숨기기위해서, 일반크롬창 열었을때 값을 넣어준다.
options.add_argument(
    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36")
browser = webdriver.Chrome(options=options)
browser.maximize_window()
