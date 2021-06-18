# 함수
def open_account():
    print("새로운 계좌가 생성되었습니다.")


def deposit(balance, money):  # 입금
    print("입금이 완료되었습니다. 잔액은 {0}원 입니다.".format(balance+money))
    return balance + money


def withdraw(balance, money):  # 출금
    if balance >= money:  # 잔액이 출금보다 많으면
        print("출금이 완료되었습니다. 잔액은 {0}원입니다.".format(balance-money))
        return balance - money
    else:
        print("출금이 완료되지 않았습니다. 잔액은 {0}원입니다.".format(balance))
        return balance


def withdraw_night(balance, money):  # 저녁에 출금
    commission = 100  # 수수료 100원
    return commission, balance - money - commission  # 두개의 값을 , 로 구분해서 여러개 값 반환


open_account()
balance = 0  # 잔액
balance = deposit(balance, 10000)
balance = withdraw(balance, 500)
commission, balance = withdraw_night(balance, 500)
print("수수료 {0} 원이며, 잔액은 {1}원입니다.".format(commission, balance))


print("--------------------------------------------------")

# 함수에서 기본값 설정


def profile(name, age=17, main_lang="파이썬"):
    print("이름 : {0}\t 나이:{1}\t주 사용언어 : {2}"
          .format(name, age, main_lang))


profile("유재석")
profile("김태호")

print("--------------------------------------------------")

# 함수에서 키워드값 설정 ( 인자 순서가 바껴도 됨)


def keyword(name, age, main_lang):
    print(name, age, main_lang)


keyword(name="유재석", main_lang="파이썬", age=20)
keyword(main_lang="자바", age=25, name="김태호")

print("--------------------------------------------------")

# 가변인자 :  *매개변수명
# print에서 줄바꿈안하고 이어서쓰기 : end=" " 를 추가한다.


def argument(name, age, *language):
    print("이름 : {0}\t나이 : {1}\t".format(name, age), end="  ")
    for lang in language:
        print(lang, end=" ")
    print()


argument("유재석", 20, "python", "Java", "C", "C++", "C#", "JavaScript")
argument("김태호", 25, "python", "JavaScript")
print("--------------------------------------------------")
