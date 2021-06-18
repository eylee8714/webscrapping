# 패키지, 모듈 위치 : 현재 작성중인 파일과 동일한 경로 또는 파이썬 라이브러리 모여있는 폴더에 있어야한다.

# 패키지 : 모듈들을 모아놓은 집합. 하나의 디렉토리에 여러 모듈 파일들을 갖다놓은 것
# 패키지 (폴더) 안에 모듈들 (.py 파일들) 넣어주고 가져와서 쓴다. __init__.py 파일 만들어놓기.

# 타일랜드 패키지 가져와서 사용하기
# import를 쓸때는 모듈이나 패키지만 가능하다 (클래스나 함수는 import 직접 바로 할 수 없다.)

# import travel.thailand
# trip_to = travel.thailand.ThailandPackage()
# trip_to.detail()

# ------------------------------------------------------------------

# from import 구문에서는 클래스나 함수 사용할수있다.

# from travel.thailand import ThailandPackage  # ThailandPackage 클래스 임포트
# trip_to = ThailandPackage()
# trip_to.detail()

# from travel import vietnam
# trip_to = vietnam.VietnamPackage()
# trip_to.detail()

# ------------------------------------------------------------------


# from travel import *  # * 을 사용하면 __init__ 에 명시해준 모듈만 가져온다.

# # trip_to = vietnam.VietnamPackage()
# trip_to = thailand.ThailandPackage()

# trip_to.detail()


# ------------------------------------------------------------------
# inspect : 파일 위치 확인
# 패키지, 모듈 위치 : 현재 작성중인 파일과 동일한 경로 또는
# 파이썬 라이브러리 모여있는 폴더에 있어야한다. (C:\Python39\lib)
#
import random
import inspect
from travel import *
print(inspect.getfile(random))
print(inspect.getfile(thailand))
