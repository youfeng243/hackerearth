
def main():
    T = input()
    
    for _ in xrange(T):
        N,M = map(int, raw_input().strip().split())
        DP = [0] * (N + 1)
        DP[M] = 1
        for i in xrange( M + 1, N + 1 ):
            DP[i] = DP[i - 1] * 2
            DP[i] %= (10**9 + 7)
        #DP[N] %= (10 ** 9 + 7)
        print DP[N]
        
if __name__=="__main__":
    main()