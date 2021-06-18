from selenium import webdriver

# [엘리먼트 로딩될때까지 기다리기]
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()
browser.maximize_window()  # 창 최대화

url = "https://flight.naver.com/flights/"
browser.get(url)  # url로 이동

# 가는 날 선택 클릭
browser.find_element_by_link_text("가는날 선택").click()

# 이번달 27일, 28일 선택
# browser.find_elements_by_link_text("27")[0].click()  # [0] -> 이번달
# browser.find_elements_by_link_text("28")[0].click()  # [0] -> 이번달

# 다음달 27일, 28일 선택
# browser.find_elements_by_link_text("27")[1].click()  # [1] -> 다음달
# browser.find_elements_by_link_text("28")[1].click()  # [1] -> 다음달

# 이번달 27일, 다음달 28일 선택
browser.find_elements_by_link_text("27")[0].click()  # [0] -> 이번달
browser.find_elements_by_link_text("28")[1].click()  # [1] -> 다음달

# 제주도 선택
browser.find_element_by_xpath(
    "//*[@id='recommendationList']/ul/li[1]/div/span").click()  # xpath쓸 때, 따옴표 확인하기

# 항공권 검색 클릭
browser.find_element_by_link_text("항공권 검색").click()

# 오류 나면 browser.quit() 하기위해 try 문 써준다.
try:
    # [엘리먼트 로딩될때까지 기다리기] 최대 10초 동안 기다린다. XPATH 조건(EC)에 해당하는 엘리먼트가 나올 때 까지
    elem = WebDriverWait(browser, 10).until(EC.presence_of_element_located(
        (By.XPATH, "//*[@id='content']/div[2]/div/div[4]/ul/li[1]")))
    # 첫번째 결과 출력
    print(elem.text)

finally:
    browser.quit()
