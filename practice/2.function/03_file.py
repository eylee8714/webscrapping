# 파일 입출력

# 쓰기목적으로 열기 W | 한글쓰기위해 utf8 적기

# 파일 열기 w : 파일이 이미 존재하면 덮어쓰기 된다.
score_file = open("score.txt", "w", encoding="utf8")
print("수학 : 0", file=score_file)  # print를 쓰면 자동으로 줄바꿈된다.
print("영어 : 50", file=score_file)
# 파일 열면 항상 닫아주기
score_file.close()

print("--------------------------------------------------")


# 존재하는 파일에 이어서 쓸때 a
score_file = open("score.txt", "a", encoding="utf8")
score_file.write("과학 : 80")
score_file.write("\n코딩 : 100")  # write를 쓰면 줄바꿈되지 않아서 \n 쓴다.
score_file.close()

print("--------------------------------------------------")


# 읽을 목적 r
score_file = open("score.txt", "r", encoding="utf8")
print(score_file.read())  # 파일에 있는 모든 내용 읽어와서 터미널에 출력한다.
score_file.close()

print("--------------------------------------------------")

# 한줄씩 읽기 readline()
score_file = open("score.txt", "r", encoding="utf8")
print(score_file.readline())  # 줄별로 읽기, 한줄 읽고 커서는 다음 줄로 이동
print(score_file.readline())  # print는 자동으로 줄바꿈된다.
print(score_file.readline(), end="")  # end="" 추가하면 줄바꿈되지않는다.
print(score_file.readline())
score_file.close()

print("--------------------------------------------------")


# 파일의 라인 수를 알수없을때, while 문을 이용한다.
score_file = open("score.txt", "r", encoding="utf8")
while True:
    line = score_file.readline()
    if not line:
        break
    print(line, end="")
score_file.close()

print("\n--------------------------------------------------")

# 파일의 라인 수를 알수없을때, list에 넣어서 처리하기
score_file = open("score.txt", "r", encoding="utf8")
lines = score_file.readlines()  # list 형태로 저장 ( score_file의 모든 줄 list에 추가)
for line in lines:  # 리스트에서 한줄씩 불러와서 출력한다.
    print(line, end="")
score_file.close()
