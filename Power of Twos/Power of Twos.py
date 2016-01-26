#coding=utf-8
import math

def getPrime( Max ):
    used = [0] * (Max + 1)
    prime = [2]
    
    length = int( math.sqrt(Max) ) + 1
    for i in xrange(3, length, 2):
        if used[i] == 1:
            continue
        for j in xrange( i * i, Max + 1, i ):
            used[j] = 1
    
    for i in xrange( 3, Max, 2 ):
        if used[i] == 0:
            prime.append(i)
     
    return prime

def main():
    T = input()
    N = []
    for _ in xrange(T):
        N.append(input())
        
    Max = max(N)
    primeMax = int(math.sqrt(Max)) + 1
    prime = getPrime(primeMax)
    
    dp = [0] * (Max + 1)
    dp[1] = 0
    dp[2] = 1
    dp[3] = 1
    for i in xrange( 4, Max + 1 ):
        sqrttemp = int(math.sqrt(i) + 1)
        dp[i] = 1
        for j in xrange( len(prime) ):
            if prime[j] >= sqrttemp:
                break
            if i % prime[j] == 0:
                if i / prime[j] == prime[j]:
                    dp[i] += 1
                else:
                    dp[i] += 2
    DP = [0] * (Max + 1)
    DP[1] = 0
    for i in xrange( 2, Max + 1 ):
        DP[i] = DP[i - 1] + dp[i]
    
    for i in N:
        print DP[i]
    
    
if __name__=="__main__":
    main()