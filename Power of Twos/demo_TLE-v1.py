#coding=utf-8
import math

def getPrime( Max ):
    used = [0] * Max
    
    length = int( math.sqrt(Max) ) + 1
    for i in xrange(3, length, 2):
        if used[i] == 1:
            continue
        for j in xrange( i * i, Max, i ):
            used[j] = 1
    
    for i in xrange( 4, Max, 2 ):
        used[i] = 1
    
    return used

def main():
    T = input()
    N = []
    for _ in xrange(T):
        N.append(input())
        
    Max = max(N)
    
    used = getPrime( Max + 1 )
    
    dp = [0] * (Max + 1) 
    dp[1] = 0
    dp[2] = 1
    dp[3] = 1
    for i in xrange( 4, Max + 1 ):
        sqrttemp = int(math.sqrt(i) + 1)
        dp[i] = 1
        
        if used[i] == 0:
            continue
        
        for j in xrange( 2, sqrttemp ):
            if i % j == 0:
                if i / j == j:
                    dp[i] += 1
                else:
                    dp[i] += 2

    print dp
                    
    DP = [0] * (Max + 1)
    DP[1] = dp[1]
    for i in xrange( 2, Max + 1 ):
        DP[i] = DP[i - 1] + dp[i]
    
    for i in N:
        print DP[i]
        
if __name__=="__main__":
    main()