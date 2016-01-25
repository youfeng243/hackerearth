import math
def getNum( Max ):
    used = [0] * (Max + 1)
    prime = [2]
    for i in xrange( 3, int(math.sqrt(Max) + 1), 2 ):
        if used[i] == 1:
            continue
        for j in xrange( i * i, Max + 1, i ):
            used[j] = 1
    for i in xrange( 3, Max + 1, 2 ):
        if used[i] == 0:
            prime.append(i)
    
    for i in xrange(len(prime)):
        temp = prime[i] ** prime[i]
        if temp > Max:
            break
        prime.append(temp)
        
    prime.sort()
    
    #print prime
    return prime
    
    

def main():
    T = input()
    Question = []
    Max = 0
    for _ in xrange(T):
        Question.append(input())
    Max = max(Question)
    Num = getNum( Max )
    length = len(Num)
    
    ans = [-1] * ( Max + 1 )
    
    for i in xrange(T):
        if ans[ Question[i] ] != -1:
            print ans[ Question[i] ]
            continue
        
        DP = [10 ** 10] * (Question[i] + 1)
        for j in xrange(length):
            if Num[j] > Question[i]:
                break
            DP[ Num[j] ] = 1
        
        for k in xrange( length ):
            if Num[k] > Question[i]:
                break
            for j in xrange( Num[k], Question[i] + 1 ):
                DP[j] = min( DP[j - Num[k]] + 1, DP[j] )
        
        ans[ Question[i] ] = DP[Question[i]]
        print DP[Question[i]]
    

if __name__=="__main__":
    main()