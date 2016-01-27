#coding=utf-8

class Node(object):
    def __init__( self ):
        self.cnt = 0
        self.addMark = 0  #ÑÓ³Ù±ê¼Ç

class Tree(object):
    def __init__( self, N ):
        self.segNode = [ Node for _ in xrange( N * 2 + 100 ) ]
        self.build( 1, 1, N )
        #print self.segNode
    
    def build( self, root, start, end ):
        self.segNode[root].addMark = 0
        if start == end:
            self.segNode[root].cnt = 0
        else:
            mid = ( start + end ) / 2
            self.build( root * 2 + 1, start, mid )
            self.build( root * 2 + 2, mid + 1, end )
    
    def pushDown( self, root ):
        if self.segNode[root].addMark != 0:
            self.segNode[root * 2 + 1].addMark += self.segNode[root].addMark
            self.segNode[root * 2 + 2].addMark += self.segNode[root].addMark
            
            self.segNode[root * 2 + 1].cnt += self.segNode[root].addMark
            self.segNode[root * 2 + 2].cnt += self.segNode[root].addMark
            
            self.segNode[root].addMark = 0
            
            
    def insert( self, root, nodeStart, nodeEnd, useStart, useEnd, val ):
        if nodeStart > useEnd or nodeEnd < useStart:
            return
        
        if nodeStart >= useStart and nodeEnd <= useEnd:
            self.segNode[root].addMark += val
            self.segNode[root].cnt += val
            return
        
        self.pushDown(root)
        
        mid = ( nodeStart + nodeEnd ) / 2
        self.insert( root * 2 + 1, nodeStart, mid, useStart, useEnd, val )
        self.insert( root * 2 + 2, mid + 1, nodeEnd, useStart, useEnd, val )
        
    def query( self, root, nstart, nend, num ):
    
        if nstart == num and nend == num:
            return self.segNode[root].cnt
        
        self.pushDown(root)
        
        mid = ( nstart + nend ) / 2
        
        if num >= nstart and num <= mid:
            return self.query( root * 2 + 1, nstart, mid, num )
        return self.query( root * 2 + 2, mid + 1, nend, num )
        
def main():
    N = input()
    M = input()
    tree = Tree(N)
    
    for _ in xrange( M ):
        start, end = map( int, raw_input().strip().split() )
        tree.insert( 1, 1, N, start, end, 1 )
    
    DP = [0] * ( N + 1 )
    for i in xrange( 1, N + 1 ):
        DP[i] = tree.query( 1, 1, N, i )
    
    print DP
    
    for i in xrange( N - 1, 0, -1 ):
        DP[i] += DP[i + 1]
        
    Q = input()
    for _ in xrange(Q):
        X = input()
        print DP[X]
    
if __name__=="__main__":
    main()