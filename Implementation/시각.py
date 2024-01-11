N = int(input())
cnt = 0

for i in range(N + 1):  # 0~N시간
    for j in range(60):  # 0~59분
        for k in range(60):  # 0~59초
            if "".join([str(i), str(j), str(k)]).count("3"):
                cnt += 1
print(cnt)
