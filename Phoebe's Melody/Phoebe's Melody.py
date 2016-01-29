
def main():
    T = input()
    for _ in xrange( T ):
        N, K = map(int, raw_input().strip().split())
        A = map(int, raw_input().strip().split())
        index = [0] * (N + 1)
        for i in xrange( N ):
            index[A[i]] = i
        
        DP = [0] * (N + 1)
        for i in xrange( 2, N + 1 ):
            DP[i] = 10**10
            for j in xrange( 1, i ):
                if abs(index[ j ] - index[ i ]) >= K:
                    DP[i] = min( DP[i], abs(index[ j ] - index[ i ]) )
                if DP[i] <= K:
                    break
            if DP[i] == 10**10:
                DP[i] = 0
        print sum(DP)
        
if __name__=="__main__":
    main()