def main():
    T = input()
    for _ in xrange(T):
        N = input()
        Array = []
        for i in xrange( N ):
            R,H = map(int, raw_input().strip().split())
            Array.append( (R, H) )
        Array.sort(lambda x, y: x[0] - y[0])
        #print Array
        DP = [0] * (N + 1)
        for i in xrange( 1, N + 1 ):
            DP[i] = Array[i - 1][1]
        
        Max = 0
        for i in xrange( 1, N ):
            for j in xrange( i ):
                if Array[i][1] > Array[j][1] and Array[i][0] > Array[j][0]:
                    DP[i + 1] = max( DP[i + 1], DP[j + 1] + Array[i][1] )
                Max = max(Max, DP[i + 1])
        #print DP
        #print DP[N]
        print Max

if __name__ == "__main__":
    main()