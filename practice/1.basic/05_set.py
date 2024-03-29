# --------------------------------------------------------------------

# 세트 : 집합
# 중복 안됨, 순서 없음
my_set = {1, 2, 3, 3, 3}
print(my_set)

java = {"유재석", "김태호", "양세형"}
python = set(["유재석", "박명수"])

# intersection : 교집합 (java와 python을 모두 할 수 있는 개발자)
print(java & python)
print(java.intersection(python))

# union : 합집합 (java도 할 수 있거나 python을 할 수 있는 개발자)
print(java | python)
print(java.union(python))

# difference : 차집합 (java 할 수 있지만 python은 할 줄 모르는 개발자)
print(java - python)
print(java.difference(python))

# add : python 할 줄 아는 사람 늘어남
python.add("김태호")
print(python)

# remove : java를 잊었어요
java.remove("김태호")
print(java)
