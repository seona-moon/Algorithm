s, p = map(int, input().split())  # 문자열 길이 S, 부분문자열의 길이 P
string = input()  # DNA 문자열
min_str = list(
    map(int, input().split())
)  # 부분문자열에 포함되어야 할 {‘A’, ‘C’, ‘G’, ‘T’} 의 최소 개수
current_str = [0] * 4
cnt = 0


def add(c):  # 문자가 들어왔을 때 계산하는 함수
    global current_str
    if c == "A":
        current_str[0] += 1
    elif c == "C":
        current_str[1] += 1
    elif c == "G":
        current_str[2] += 1
    else:
        current_str[3] += 1


def sub(c):  # 문자가 빠질 때 계산하는 함수
    global current_str
    if c == "A":
        current_str[0] -= 1
    elif c == "C":
        current_str[1] -= 1
    elif c == "G":
        current_str[2] -= 1
    else:
        current_str[3] -= 1


def check():  # 최소 값을 만족시키는지 확인
    global cnt, current_str, min_str
    if (
        current_str[0] >= min_str[0]
        and current_str[1] >= min_str[1]
        and current_str[2] >= min_str[2]
        and current_str[3] >= min_str[3]
    ):
        cnt += 1


for i in range(p):  # 부분 문자열 개수 초기화
    if string[i] == "A":
        current_str[0] += 1
    elif string[i] == "C":
        current_str[1] += 1
    elif string[i] == "G":
        current_str[2] += 1
    else:
        current_str[3] += 1

check()

# 슬라이딩 윈도우
for i in range(1, s - p + 1):
    add(string[i + p - 1])  # 이후 문자열 추가
    sub(string[i - 1])  # 이전 문자열 제거
    check()
print(cnt)
