class ThailandPackage:
    def detail(self):
        print("[태국 패키지 3박 5일] 방콕, 파타야 여행 (야시장 투어) 50만원")


# __name__ 정보를 활용해서 직접 모듈을 쓰는건지, 외부에서 갖다 쓰는건지 구분할수있다.
if __name__ == "__main__":  # name이 main이면 이 구문은 직접실행
    print("Thailand 모듈을 직접 실행")
    trip_to = ThailandPackage()
    trip_to.detail()
else:
    print("Thailand 외부에서 모듈 호출")
