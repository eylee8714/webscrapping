# 클래스 : 서로 연관있는 변수와 함수의 집합

class Unit:
    def __init__(self, name, hp, damage):  # __init__ : 파이썬에서 쓰이는 생성자. (기본적으로 적어주기.)
        self.name = name  # 클래스내에서 정의된 변수를 멤버변수라고한다. (name, hp, damage)
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성되었습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))


# 클래스사용하기 ( self 빼고 동일한 개수만큼 값을 적어주어야한다.)
# 클래스로부터 만들어지는 것을 객체라고한다. (marine1, marine2, tank)
# marine과 tank는 Unit클래스의 인스턴스이다.
marine1 = Unit("마린", 40, 5)
marine2 = Unit("마린", 40, 5)
tank = Unit("탱크", 150, 35)


# 레이스 : 공중유닛, 비행기. 특수기능 : 클로킹(상대방에게 보이지 않음)
wraith1 = Unit("레이스", 80, 5)

# 멤버변수를 외부에서 쓸 수 있다.
# . 을 이용해 멤버변수에 접근할 수 있다.
print("유닛 이름 : {0}, 공격력 : {1}".format(wraith1.name, wraith1.damage))

# 마인드 컨트롤 : 상대방 유닛을 내것으로 만드는것(빼앗음)
wraith2 = Unit("빼앗은 레이스", 80, 5)
# 클래스 외부에서 원하는 변수 확장할 수 있다.
wraith2.clocking = True

if wraith2.clocking == True:
    print("{0} 는 현재 클로킹 상태입니다.".format(wraith2.name))
