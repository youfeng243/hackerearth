#coding=utf-8

def SumA( startA, endA ):
    if startA == endA:
        return A[startA]
    if startA > endA:
        return 0
    
    #偶数
    if startA % 2 == 0:
        if startA == 0:
            return eveA[endA]
        return eveA[endA] - eveA[startA - 2]
    
    if startA == 1:
        return oddA[endA]
    return oddA[endA] - oddA[startA - 2]
    
def SumB( startB, endB ):
    if startB == endB:
        return B[startB]
    if startB > endB:
        return 0
    
    #偶数
    if startB % 2 == 0:
        if startB == 0:
            return eveB[endB]
        return eveB[endB] - eveB[startB - 2]
    
    if startB == 1:
        return oddB[endB]
    return oddB[endB] - oddB[startB - 2]
    
def main():

    global eveA
    global oddA
    global eveB
    global oddB
    global A
    global B

    N,Q = map(int, raw_input().strip().split())
    A = map(int, raw_input().strip().split())
    B = map(int, raw_input().strip().split())

    eveA = [0] * N
    oddA = [0] * N
    eveB = [0] * N
    oddB = [0] * N

    
    
    #计算偶数序列和
    eveA[0] = A[0]
    for i in xrange( 2, N, 2 ):
        eveA[i] += eveA[i - 2] + A[i]

    if N >= 1:
        oddA[1] = A[1]
        for i in xrange( 3, N, 2 ):
            oddA[i] += oddA[i - 2] + A[i]
            
            
    eveB[0] = B[0]
    for i in xrange( 2, N, 2 ):
        eveB[i] += eveB[i - 2] + B[i]

    if N >= 1:
        oddB[1] = B[1]
        for i in xrange( 3, N, 2 ):
            oddB[i] += oddB[i - 2] + B[i]

    for _ in xrange( Q ):
        turn, start, end = map(int, raw_input().strip().split())
        start -= 1
        end -= 1
        
        Astart = 0
        Aend = 0
        Bstart = 0
        Bend = 0
        if turn == 1: #A开头
            Astart = start
            Bstart = start + 1
            
            if start % 2 == end % 2:
                Aend = end
                Bend = end - 1
            else:
                Bend = end
                Aend = end - 1
                
        if turn == 2:  #B开头
            Bstart = start
            Astart = start + 1
            
            if start % 2 == end % 2:
                Bend = end
                Aend = end - 1
            else:
                Aend = end
                Bend = end - 1
            
        print SumA(Astart, Aend) + SumB( Bstart, Bend )
        
if __name__ == "__main__":
    main()
            
