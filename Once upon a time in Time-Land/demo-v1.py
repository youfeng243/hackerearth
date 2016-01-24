T = input()
for _ in xrange(T):
    N,K = map(int, raw_input().strip().split())
    Array = map(int, raw_input().strip().split())
    DP = [0] * (N + K + 1)
    for i in xrange(N):
        DP[i + K + 1] = max( DP[i + K], DP[i] + Array[i] )
    print DP[N + K]