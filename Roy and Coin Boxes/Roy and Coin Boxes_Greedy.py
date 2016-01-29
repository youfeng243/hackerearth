def main():
    N = input()
    M = input()
    A = [0] * ( N + 2 )
    for _ in xrange( M ):
        L,R = map(int, raw_input().strip().split())
        A[L] += 1
        A[R + 1] += -1
    
    DP = [0] * (N + 1)
    for i in xrange( 1, N + 1 ):
        A[i] += A[i - 1]
        DP[A[i]] += 1
    
    for i in xrange( N - 1, 0, -1 ):
        DP[i] += DP[i + 1]
    
    Q = input()
    for i in xrange( Q ):
        print DP[input()]

if __name__=="__main__":
    main()