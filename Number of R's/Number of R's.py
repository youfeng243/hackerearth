def main():
    N = input()
    for _ in xrange(N):
        A = list(raw_input().strip())
        #cnt = A.count('R') - A.count('K')
        Max = 0
        temp = 0
        index = -1
        for i in xrange(len(A)):
            if A[i] == 'K':
                temp += 1
            elif temp - 1 >= 0:
                temp -= 1
            if temp > Max:
                Max = temp
                index = i
                
        if index == -1:
            print len(A) - 1
            continue
                
        temp = index
        while index >= 0 and Max > 0:
            if A[index] == 'K':
                Max -= 1
                index -= 1
            else:
                Max += 1
                index -= 1
        
        index += 1
        for i in xrange( index, temp + 1 ):
            if A[i] == "K":
                A[i] = "R"
            else:
                A[i] = "K"
        
        print A.count("R")
        #print "Max = ", Max
        #print cnt + Max
              
    
if __name__=="__main__":
    main()