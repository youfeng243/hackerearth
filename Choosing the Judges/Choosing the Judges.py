def main():
    T = input()
    for _ in xrange(T):
        N = input()
        Array = map(int, raw_input().strip().split())
        
        if N == 1:
            print "Case %d: %d" % (_ + 1, Array[0])
            continue
        
        if N == 2:
            print "Case %d: %d" % (_ + 1, max(Array[0], Array[1]))
            continue
        
        DP = [0] * N
        DP[0] = Array[0]
        DP[1] = Array[1]
        for i in xrange(2, N):
            if i == 2:
                DP[i] = max( DP[i - 1], DP[i - 2] + Array[i] )
            else:
                DP[i] = max( DP[i - 1], DP[i - 2] + Array[i], DP[i - 3] + Array[i] )
        print "Case %d: %d" % (_ + 1, DP[N - 1])
        
       
if __name__ == "__main__":
    main()