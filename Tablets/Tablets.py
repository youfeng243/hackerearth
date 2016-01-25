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
    
    for i in xrange( 1, N + 1 ):
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
                
    i = N
    while i >= 1:
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
        i -= 1
                
    #print DP
    print sum(DP[1 : N + 1])
    
    
if __name__ == "__main__":
    main()