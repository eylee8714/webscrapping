# selenium 공부 사이트
# https://selenium-python.readthedocs.io/


# 터미널에서 python 작동했음
# >>> browser.get("http://naver.com")
# >>> elem = browser.find_element_by_class_name("link_login")
# >>> elem
# <selenium.webdriver.remote.webelement.WebElement (session="2e9edbbb0bc4643d68631cf197856ab7", element="ead64f5a-4d46-431c-8555-ced831f2148a")>
# >>> elem.click()
# >>> browser.back()
# >>> browser.forward()
# >>> browser.refresh()
# >>> browser.back()
# >>> elem = browser.find_element_by_id("query")
# >>> elem
# <selenium.webdriver.remote.webelement.WebElement (session="2e9edbbb0bc4643d68631cf197856ab7", element="dd5f0389-7325-45fa-bd84-1a29749457b6")>
# >>> from selenium.webdriver.common.keys import Keys
# >>> elem.send_keys("이은영")
# >>> elem.send_keys(Keys.ENTER)
# >>> elem = browser.find_elements_by_tag_name("a")
# >>> elem
# for e in elem:
# ...     e.get_attribute("href")


# 다음에서 검색하기
# >>> browser.get("http://daum.net")
# >>> elem = browser.find_element_by_name("q")
# >>> elem
# <selenium.webdriver.remote.webelement.WebElement (session="2e9edbbb0bc4643d68631cf197856ab7", element="c72093ca-1490-43c7-91b3-85ddedcb3b63")>
# >>> elem.send_keys("이은영")
# >>> elem.send_keys(Keys.ENTER)
# >>> browser.back()
# >>> elem = browser.find_element_by_name("q")
# >>> elem.send_keys("이은영")
# >>> elem = browser.find_element_by_xpath("//*[@id='daumSearch']/fieldset/div/div/button[2]") # xpath 사용하기 | 큰따옴표 겹칠때 작은따옴표 사용하기
# >>> elem
# <selenium.webdriver.remote.webelement.WebElement (session="2e9edbbb0bc4643d68631cf197856ab7", element="18182664-a6cf-4069-afb1-ca54fec77c16")>
# >>> elem.click()
# >>> browser.close() # 현재 열려있는 탭 닫기
# >>> browser.quit() # 브라우저 종료
