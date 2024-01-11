N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# 배열 A의 모든 원소의 합이 최대가 되도록 -> A의 최솟값과 B의 최댓값을 바꿔치기한다.
# K번만 실행될 수 있기 때문에 A와 B는 미리 정렬이 되어있어야 한다!

A.sort()
B.sort(reverse=True)
for i in range(K):
    if A[i] < B[i]:
        A[i], B[i] = B[i], A[i]
    else:
        # A의 최솟값이 이미 B의 최댓값보다 크거나 같다면 더 이상 교환할 필요가 없다. (최대 K번이므로)
        break

print(sum(A))
