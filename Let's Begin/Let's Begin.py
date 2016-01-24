def main():
    T = input()
    Question = []
    for _ in xrange(T):
        Question.append(input())
    Max = max(Question)
    prime = [2, 3, 5, 7]
    
    for k in xrange(T):
        DP = [10 ** 10] * (Question[k] + 1)
        for i in xrange( len(prime) ):
            if prime[i] > Question[k]:
                break
            DP[prime[i]] = 1
        
        for i in xrange( len(prime) ):
            if prime[i] > Question[k]:
                break
            for j in xrange( prime[i], Question[k] + 1 ):
                if DP[j - prime[i]] <= 0:
                    continue
                DP[j] = min( DP[j - prime[i]] + 1, DP[j] )
        if DP[Question[k]] == 10 ** 10:
            print -1
            continue
        print DP[Question[k]]
        
if __name__ == "__main__":
    main()