#coding=utf-8

class BIT(object):
    def __init__( self, N ):
        self.bit = [0] * (N + 1)
        self.N = N
        
    def lowbit( self, x ):
        return x & (-x)
        
    def Sum( self, x ):
        res = 0
        while x > 0:
            res += self.bit[x]
            x -= self.lowbit(x)
        return res
    
    def Add( self, x, n ):
        while x <= self.N:
            self.bit[x] += n
            x += self.lowbit(x)
        
    def Update( self, x, y, n ):
        self.Add( x, n )
        self.Add( y + 1, -n )
        print self.bit
    
    def Query( self, x ):
        return self.Sum(x) - self.Sum(x - 1)
        
def main():
    N = input()
    M = input()
    B = BIT(N)
    
    for _ in xrange( M ):
        start, end = map( int, raw_input().strip().split() )
        B.Update( start, end, 1 )
    
    Num = [0] * ( N + 1 )
    for i in xrange( 1, N + 1 ):
        Num[i] = B.Query( i )
    
    print Num
    
    DP = [0] * (N + 1)
    for i in xrange( 1, N + 1 ):
        DP[Num[i]] += 1
    
    for i in xrange( N - 1, 0, -1 ):
        DP[i] += DP[i + 1]
        
    Q = input()
    for _ in xrange(Q):
        X = input()
        print DP[X]
    
if __name__ == "__main__":
    main()