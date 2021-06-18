import pickle

# with 를 쓰면 매번 close를 할 필요없이, with문을 빠져나오면서 자동으로 종료해준다.
# 파일쓰는것 읽는것 간단하게 몇줄안되는 코드로 작성할 수 있다.

# profile.pickle 파일을 열어서, profile_file 변수로 저장해두고,
with open("profile.pickle", "rb") as profile_file:
    # profile_file 내용을 pickle.load로 불러와서 print해준다.
    print(pickle.load(profile_file))


# with 사용해서 일반파일 저장하기
with open("study.txt", "w", encoding="utf8") as study_file:
    study_file.write("파이썬을 열심히 공부하고 있어요")

# with 사용해서 일반파일 불러오기
with open("study.txt", "r", encoding="utf8") as study_file:
    print(study_file.read())
