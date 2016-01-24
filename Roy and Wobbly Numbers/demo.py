#coding=utf-8

T = input()
for _ in xrange(T):
    N,K = map(int, raw_input().strip().split())
    
    div = K / 9
    mod = K % 9
    mod -= 1
    if mod < 0:
        mod = 8
        div -= 1
    
    if div >= 9:
        print "-1"
        continue
        
    string = ["" for i in xrange(N)]
    for i in xrange(0, N, 2):
        string[i] = str(div + 1)
    
    if mod >= int(string[0]):
        mod += 1
    if mod > 9:
        print "-1"
        continue
    
    for i in xrange(1, N, 2):
        string[i] = str(mod)
    
    print "".join(string)
    