T = input()
for _ in xrange(T):
    N,K = map(int, raw_input().strip().split())
    Array = map(int, raw_input().strip().split())
    DP = [0] * N
    for i in xrange(N):
        if Array[i] <= 0:
            if i - 1 >= 0:
                DP[i] = DP[i - 1]
            else:
                DP[i] = 0
            continue
        if i - K - 1 >= 0:
            DP[i] = max(DP[i - 1], DP[i - K - 1] + Array[i])
        elif i - 1 >= 0:
            DP[i] = max(DP[i - 1], Array[i])
        else:
            DP[i] = Array[i]
    print DP[N - 1]