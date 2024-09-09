n = int(input())
score = list(map(int, input().split()))
max_score = max(score)

# 각 점수 순회하면서 최댓값을 바탕으로 점수 구하기
for i in range(len(score)):
    score[i] = (score[i] / max_score) * 100

print(sum(score) / len(score))