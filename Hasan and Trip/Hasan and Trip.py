import math

def main():
    N = input()
    point = []
    for i in xrange( N ):
        x,y,f = map(int, raw_input().strip().split())
        point.append( (x, y, f) )
    
    DP = [-10 ** 10] * N
    DP[0] = point[0][2]
    
    for i in xrange( 1, N ):
        for j in xrange( 0, i ):
            dis = math.sqrt( ( point[i][0] - point[j][0] ) ** 2 + ( point[i][1] - point[j][1] ) ** 2 )
            DP[i] = max( DP[i], DP[j] + point[i][2] - dis )
            
    print "%.6lf" % DP[N - 1]
        
if __name__=="__main__":
    main()