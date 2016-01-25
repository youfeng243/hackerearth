def main():
    T = input()
    for _ in xrange(T):
        N,P = map(int, raw_input().strip().split())
        DP = [0] * (N + 1)
        DP[1] = 1
        for i in xrange( 2, N + 1 ):
            DP[i] += DP[i - 1]
            if i < P + 1:
                DP[i] += DP[i - 1]
            elif i == P + 1:
                DP[i] += (DP[i - 1] - DP[i - P])
            else:
                DP[i] += (DP[i - 1] - DP[i - P - 1])
            DP[i] %= 1000000007
        
        print DP[N]
            
if __name__ == "__main__":
    main()