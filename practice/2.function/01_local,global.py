# 지역변수
# 함수 호출 때 만들어졌다가, 끝나면 사라진다.

# 전역변수
# 프로그램 모든공간에서 사용가능한 변수

# 일반적으로 전역변수를 많이 사용하면, 코드관리 어려워져서 권장하지 않는다.

gun = 10


def checkpoint(soldiers):  # 경계근무 군인 수
    global gun  # 전역 공간에 있는 gun 사용
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))


print("전체 총:{0}".format(gun))
checkpoint(2)  # 2명이 경계 근무 나감
print("남은 총 : {0}".format(gun))

print("--------------------------------------------------")


# 가급적 함수의 파라미터로 던져서 계산하고 반환값을 받아야한다.

def checkpoint_ret(gun, soldiers):
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))
    return gun


print("전체 총:{0}".format(gun))
gun = checkpoint_ret(gun, 2)  # 2명이 경계 근무 나감
print("남은 총 : {0}".format(gun))
