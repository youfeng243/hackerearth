def main():
    N = input()
    M = input()
    Num = [0] * (N + 1)
    
    for _ in xrange(M):
        L,R = map(int, raw_input().strip().split())
        for i in xrange(L, R + 1):
            Num[i] += 1
    
    DP = [0] * (N + 1)
    for i in xrange(N + 1):
        DP[Num[i]] += 1
    
    for i in xrange( N - 1, 0, -1 ):
        DP[i] += DP[i + 1]
    
    Q = input()
    for _ in xrange( Q ):
        index = input()
        print DP[index]
    
if __name__=="__main__":
    main()