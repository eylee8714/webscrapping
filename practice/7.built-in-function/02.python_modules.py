# 외장함수 : 구글에서 list of python modules 검색
#  https://docs.python.org/ko/3/py-modindex.html

# glob : 현재 디렉토리 내의 폴더 / 파일 목록 조회 (윈도우 dir 명령어와 같다)
# import glob
# print(glob.glob("*.py"))  # 확장자가 py인 모든 파일 조회

# -----------------------------------------------------------------------


# os : 운영체제에서 제공하는 기본 기능 (폴더삭제, 폴더생성..)
# import os
# print(os.getcwd())  # 현재 디렉토리 확인

# folder = "sample_dir"

# if os.path.exists(folder):
#     print("이미 존재하는 폴더입니다.")
#     os.rmdir(folder)
#     print(folder, "폴더를 삭제하였습니다.")
# else:
#     os.makedirs(folder)  # 폴더생성
#     print(folder, "폴더를 생성하였습니다.")

# print(os.listdir())  # glob과 같은 기능


# -----------------------------------------------------------------------

# time : 시간 관련 함수
# import time
# print(time.localtime())
# print(time.strftime("%Y-%m-%d %H:%M:%S"))

# -----------------------------------------------------------------------
# datetime : 날짜 관련 함수

import datetime
print("오늘 날짜는", datetime.date.today())

# -----------------------------------------------------------------------

# timedelta : 두 날짜 사이의 간격
today = datetime.date.today()  # 오늘 날짜 저장
td = datetime.timedelta(days=100)  # 100일 저장
print("우리가 만난지 100일은 ", today + td)  # 오늘부터 100일 후
