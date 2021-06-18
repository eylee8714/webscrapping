# 피클 : 사용하고있는 데이터를 파일형태로 저장
import pickle

# 피클 파일로 저장하기
# wb : b는 바이너리타입인데, 피클을 쓰기위해선 항상 b타입으로 정의해줘야한다.
profile_file = open("profile.pickle", "wb")
profile = {"이름": "박명수", "나이": 30, "취미": ["축구", "골프", "코딩"]}
print(profile)
pickle.dump(profile, profile_file)  # profile에 있는 정보를 file에 저장
profile_file.close()

# 피클 파일 읽기
# rb : r 읽기, b 바이너리 명시하기
profile_file = open("profile.pickle", "rb")
profile = pickle.load(profile_file)  # file 에 있는 정보를 profile에 불러오기
print(profile)
profile_file.close()
