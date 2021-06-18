# 패키지, 모듈 위치 : 현재 작성중인 파일과 동일한 경로 또는 파이썬 라이브러리 모여있는 폴더에 있어야한다.


# 모듈 : 필요한 것끼리 부품처럼 잘 만들어진 파일
# 유지보수, 재사용 쉽다.
# 모듈의 확장자는 py

# import theater_module  # 확장자 py 쓸 필요 없다.
# theater_module.price(3)  # 3명 영화 가격
# theater_module.price_morning(4)  # 4명 조조할인 가격
# theater_module.price_soldier(5)  # 5명 군인할인 가격

# import theater_module as mv  # theater_module 대신 별명 mv 를 사용하기
# mv.price(3)
# mv.price_morning(4)
# mv.price_soldier(5)

from theater_module import *  # * 을 사용해서 모두 가져와서 쓰기 ( 모듈명 쓸 필요없다. )
price(3)
price_morning(4)
price_soldier(5)

# from theater_module import price, price_morning  # 원하는 것만 가져다쓰기
# price(5)
# price_morning(6)

# from theater_module import price_soldier as price  # price_soldier 대신 별명 price 사용하기
# price(5)
