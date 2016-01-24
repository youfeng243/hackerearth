T = input()

for _ in xrange(T):
    string = raw_input().strip()
    length = len(string)
    DP = [0] * (length + 1)
    
    if length <= 2:
        print length
    
    if length == 3:
        if string[0] == string[1] and string[0] == string[2]:
            print length
            continue
        print 0
        continue
    DP[0] = 0
    DP[1] = 0
    DP[2] = 0
    Max = 0
    for i in xrange( 3, length + 1 ):
        if string[i - 1] == string[i - 2] and string[i - 1] == string[i - 3]:
            DP[i] = 0
        else:
            DP[i] = DP[i - 3] + 3
        if DP[i] > Max:
            Max = DP[i]
    print length - Max
    