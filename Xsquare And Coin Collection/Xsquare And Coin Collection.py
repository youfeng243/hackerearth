def main():
    T = input()
    for _ in xrange(T):
        N,K = map(int, raw_input().strip().split())
        A = map(int, raw_input().strip().split())
        
        Max = 0
        temp = 0
        for i in xrange(N):
            if A[i] <= K:
                temp += A[i]
            else:
                temp = 0
            Max = max(Max, temp)
        
        print Max

        
if __name__ == "__main__":
    main()