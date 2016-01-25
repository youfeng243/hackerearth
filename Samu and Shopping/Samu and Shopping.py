def main():
    T = input()
    for _ in xrange(T):
        N = input()
        cost = []
        for i in xrange(N):
            cost.append(map(int, raw_input().strip().split()))
        
        DP = [ [0, 0, 0] for _ in xrange(N) ]
        DP[0][0] = cost[0][0]
        DP[0][1] = cost[0][1]
        DP[0][2] = cost[0][2]
        
        for i in xrange(1, N):
            DP[i][0] = min( DP[i - 1][1], DP[i - 1][2] ) + cost[i][0]
            DP[i][1] = min( DP[i - 1][0], DP[i - 1][2] ) + cost[i][1]
            DP[i][2] = min( DP[i - 1][0], DP[i - 1][1] ) + cost[i][2]
        
        print min( DP[N - 1][0], DP[N - 1][1], DP[N - 1][2] )
        
if __name__ == "__main__":
    main()