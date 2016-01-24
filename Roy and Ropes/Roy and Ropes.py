T = input()
for _ in xrange(T):
    N = input()
    up = map(int, raw_input().strip().split())
    down = map(int, raw_input().strip().split())
    Max = 0
    for i in xrange( N - 1 ):
        up[i] += i + 1
        down[i] += i + 1
        Max = max(Max, up[i], down[i])
    Max = max(N, Max)
    print Max