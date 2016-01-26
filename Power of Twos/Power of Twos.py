#coding=utf-8
import math

def main():
    T = input()
    N = []
    for _ in xrange(T):
        N.append(input())
        
    Max = max(N)
    dp = [1] * ( Max + 1 )
    end = Max / 2
    for i in xrange( 2, end + 1 ):
        for j in xrange( i + i, Max + 1, i ):
            dp[j] += 1
    dp[1] = 0
    
    #print dp
    
    DP = [0] * (Max + 1)
    DP[1] = dp[1]
    for i in xrange( 2, Max + 1 ):
        DP[i] = DP[i - 1] + dp[i]
    
    for i in N:
        print DP[i]
        
if __name__=="__main__":
    main()