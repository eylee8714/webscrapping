# 리스트 []
subway = [10, 20, 30]
print(subway)

subway = ["유재석", "조세호", "박명수"]
print(subway)

# index : 조세호씨가 몇 번쨰 칸에 타고있는가?
print(subway.index("조세호"))

# append : 하하씨가 다음 정류장에서 다음 칸에 탐
subway.append("하하")  # 리스트 맨 뒤에 추가
print(subway)

# insert : 정형돈씨를 유재석 | 하하 사이에 넣어봄
subway.insert(1, "정형돈")  # 1번째에 추가
print(subway)

# pop : 지하철에 있는 사람을 한 명씩 뒤에서 꺼냄
print(subway.pop())
print(subway)

# count : 같은 이름의 사람이 몇 명 있는지 확인
subway.append("유재석")
print(subway)
print(subway.count("유재석"))


# --------------------------------------------------------------------

# sort : 정렬
num_list = [5, 2, 4, 3, 1]
num_list.sort()
print(num_list)

# 순서 뒤집기
num_list.reverse()
print(num_list)

# 모두 지우기
num_list.clear()
print(num_list)

# --------------------------------------------------------------------

# 리스트에 다양한 자료형 함께 사용
mix_list = ["조세호", 20, True]
print(mix_list)

# 리스트 확장
num_list = [5, 2, 4, 3, 1]
num_list.extend(mix_list)
print(num_list)
