# 다른 사람들이 만든 패키지 설치방법

# pypi.org 들어가기

# 터미널에서 pip install 패키지명 적기
# pip install beautifulsoup4

# 현재 설치된 패키지명 보기
# pip list

# 해당 패키지 정보 보기
# pip show beautifulsoup4

# 업그레이드
# pip install --upgrade beautifulsoup4

# 삭제
# pip uninstall beautifulsoup4

from bs4 import BeautifulSoup
soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
print(soup.prettify())
