# 일반 유닛 클래스
class Unit:
    def __init__(self, name, hp, speed):  # __init__ : 파이썬에서 쓰이는 생성자. (기본적으로 적어주기.)
        self.name = name  # 클래스내에서 정의된 변수를 멤버변수라고한다. (name, hp, damage)
        self.hp = hp
        self.speed = speed

    def move(self, location):
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]"
              .format(self.name, location, self.speed))


# 공격 유닛 클래스
class AttackUnit(Unit):  # 상속 받고싶은 클래스를 괄호안에 적는다.
    def __init__(self, name, hp, speed, damage):  # __init__ : 파이썬에서 쓰이는 생성자. (기본적으로 적어주기.)
        Unit.__init__(self, name, hp, speed)  # Unit 클래스의 상속받고자하는 멤버변수 적어준다.
        self.damage = damage  # AttackUnit에만 있는 멤버변수

    # 클래스 내에서 매소드 앞에는 항상 self 적어준다. "self.변수명" 을 통해 자기자신의 변수에 접근할 수 있다.
    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]"
              .format(self.name, location, self.damage))  # self.name 은 __init__ 에서의 자기자신의 name과 damage를 쓰는거고, location은 전달받은 값을 쓰겠다는 것이다.

    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))

# 날수 있는 유닛 클래스


class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]"
              .format(name, location, self.flying_speed))

# 공중 공격 유닛 클래스


class FlyableAttackUnit(AttackUnit, Flyable):  # AttackUnit,Flyable 클래스 다중상속
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage)  # 지상 speed 0
        Flyable.__init__(self, flying_speed)

    # 메소드 오버라이딩
    def move(self, location):
        print("[공중 유닛 이동]")
        self.fly(self.name, location)

# 건믈


class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        # Unit.__init__(self, name, hp, 0) ** 다중상속시, 명시적으로 클래스이름 적어줘야한다.**
        # super를 쓸땐 () 붙여야하고, self 없이 쓴다. **super() 를 쓰면 다중상속시, 맨처음 기입한 클래스만 상속이 된다. **
        super().__init__(name, hp, 0)
        self.location = location


# 서플라이 디폿 : 건물, 1개건물 = 8유닛생성
supply_depot = BuildingUnit("서플라이 디폿", 500, "7시")


# 메딕(일반유닛) : 의무병
# 파이어뱃(공격유닛) : 공격 유닛, 화염방사기
firebat1 = AttackUnit("파이어뱃", 50, 3, 16)
firebat1.attack("5시")
# 공격 2번 받는다.
firebat1.damaged(25)
firebat1.damaged(25)

# 드랍쉽 : 공중유닛, 수송기. 마린 / 파이어뱃 / 탱크 등을 수송. 공격 x

# 발키리 : 공중 공격 유닛, 한번에 14발 미사일 발사.
valkyrie = FlyableAttackUnit("발키리", 200, 6, 5)
valkyrie.fly(valkyrie.name, "3시")

# 벌쳐 : 지상 유닛, 기동성이 좋음
vulture = AttackUnit("벌쳐", 80, 10, 20)

# 배틀크루저 : 공중 유닛, 체력도 굉장히 좋음, 공격력 좋음
battlecruiser = FlyableAttackUnit("배틀크루져", 500, 25, 3)


vulture.move("11시")
# battlecruiser.fly("배틀크루져", "9시")
battlecruiser.move("9시")    # 메소드 오버라이딩


# pass : 코드 완성하지 않았지만, 일단 넘어갈때 사용한다.
def game_start():
    print("[알림] 새로운 게임을 시작합니다.")


def game_over():
    pass


game_start()
game_over()
