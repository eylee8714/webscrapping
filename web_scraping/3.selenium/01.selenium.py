# 셀레니움 설치하기
# pip install selenium

# 셀레니움을 위한 웹 드라이버 설치하기 (크롬 드라이버)
# 크롬버전 확인 : 크롬창에 입력 chrome://version/
# chromdriver 검색  https://chromedriver.chromium.org/downloads
# 크롬버전에 맞는 win 버전 다운로드하기
# 압축파일풀고, chromedriver.exe 파일 파이썬 워크스페이스에 붙여넣기

import time
from selenium import webdriver

# browser = webdriver.Chrome("c:/downloads/chromedriver.exe") # 같은경로에 없다면, chromedriver.exe 있는 경로 설정해주기
browser = webdriver.Chrome()

# 1. 네이버 이동
browser.get("http://naver.com")

# 2. 로그인 버튼 이동
elem = browser.find_element_by_class_name("link_login")
elem.click()

# 3. 아이디, 패스워드 입력
browser.find_element_by_id("id").send_keys("naver_id")
browser.find_element_by_id("pw").send_keys("naver_pw")

# 4. 로그인 버튼 클릭
browser.find_element_by_id("log.login").click()
time.sleep(3)

# 5. id를 새로 입력
browser.find_element_by_id("id").clear()  # 입력했었던 내용 지우기
browser.find_element_by_id("id").send_keys("my_id")

# 6. html 정보 출력
print(browser.page_source)

# 7. 브라우저 종료
# browser.close() # 현재 탭만 종료
browser.quit()  # 전체 브라우저 종료
