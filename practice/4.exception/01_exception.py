#  예외처리
# try 문장을 잘 실행하다가, 문제가 발생하면,
# except 구문을 찾아서 해당하는 에러인지 찾는다.
# 찾으면 그 에러의 내용을 실행한다.
# as err 를 적으면 해당 에러내용 출력한다.

try:
    print("나누기 전용 계산기입니다.")
    nums = []
    nums.append(int(input("첫 번째 숫자를 입력하세요 : ")))
    nums.append(int(input("두 번째 숫자를 입력하세요 : ")))
    #nums.append(int(nums[0] / nums[1]))
    print("{0} / {1} = {2}".format(nums[0], nums[1], nums[2]))
except ValueError:
    print("에러! 잘못된 값을 입력하였습니다.")
except ZeroDivisionError as err:  # 에러내용 출력하기
    print(err)
except Exception as err:  # 명시하지 않은 모든 에러에 대한 처리
    print("알 수 없는 에러가 발생하였습니다.")
    print(err)
