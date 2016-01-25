def main():
    N = input()
    A = []
    for i in xrange(N):
        A.append(input())
    
    A.insert(0, A[0])
    A.append( A[-1] )
    DP = [0] * (N + 2)
    DP[0] = 1
    DP[-1] = 1
    
    start = 1
    end = N + 1
    step = 1
    for _ in xrange( 2 ):
        for i in xrange( start, end, step ):
            if A[i] > A[i - 1]:
                if A[i] > A[i + 1]:
                    if DP[i - 1] != 0 and DP[i + 1] != 0:
                        DP[i] = max(DP[i - 1], DP[i + 1]) + 1
                elif A[i] <= A[i + 1]:
                    if DP[i - 1] != 0:
                        DP[i] = DP[i - 1] + 1
            elif A[i] <= A[i - 1]:
                if A[i] > A[i + 1]:
                    if DP[i + 1] != 0:
                        DP[i] = DP[i + 1] + 1
                elif A[i] <= A[i + 1]:
                    DP[i] = 1
        start = N
        end = 0
        step = -1
                                
    print sum(DP[1 : N + 1])
    
    
if __name__ == "__main__":
    main()