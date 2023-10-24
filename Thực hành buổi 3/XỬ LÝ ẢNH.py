def solve(a, k, m, n):
    stripSum = [[0] * 500 for _ in range(500)]
    for j in range(n):
        sum = 0
        for i in range(k):
            sum += a[i][j]
        stripSum[0][j] = sum
        for i in range(1, m - k + 1):
            sum += (a[i + k - 1][j] - a[i - 1][j])
            stripSum[i][j] = sum
    for i in range(m - k + 1):
        sum = 0
        for j in range(k):
            sum += stripSum[i][j]
        print(sum // (k * k), end=" ")
        for j in range(1, n - k + 1):
            sum += (stripSum[i][j + k - 1] - stripSum[i][j - 1])
            print(sum // (k * k), end=" ")
        print()

t = int(input())
for _ in range(t):
    m, n, k = map(int, input().split())
    M = [[0] * 500 for _ in range(500)]
    for i in range(m):
        M[i] = list(map(int, input().split()))
    solve(M, k, m, n)

# 2
# 4 4 3
# 2 1 0 0
# 3 2 1 1
# 4 5 2 1
# 2 2 9 0
# 3 3 3
# 1 2 3
# 4 5 6
# 7 8 9