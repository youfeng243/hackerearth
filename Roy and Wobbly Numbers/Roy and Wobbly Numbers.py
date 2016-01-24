#coding=utf-8

def Add(string, num):
    length = len(string)
    if length % 2 == 1:
        if string[1] == "9":
            for i in xrange(0, length, 2):
                string[i] = chr(ord(string[i]) + 1)
            for i in xrange(1, length, 2):
                string[i] = "0"
            return string
        if ord(string[1]) + 1 == ord(string[0]):
            for i in xrange(1, length, 2):
                string[i] = chr(ord(string[i]) + 2)
                if ord(string[i]) > ord('9'):
                    string[0] = "-1"
                    return string
            return string
        for i in xrange(1, length, 2):
            string[i] = chr(ord(string[i]) + 1)
        return string
    
    if string[1] == "9":
        for i in xrange(1, length, 2):
            string[i] = "0"
        for i in xrange(0, length, 2):
            string[i] = chr(ord(string[i]) + 1)
        return string
    
    if ord(string[1]) + 1 == ord(string[0]):
        for i in xrange( 1, length, 2 ):
            string[i] = chr(ord(string[i]) + 2)
            if ord(string[i]) > ord('9'):
                string[0] = "-1"
                return string
        return string
        
    for i in xrange( 1, length, 2 ):
        string[i] = chr(ord(string[i]) + 1)
    return string

T = input()
for _ in xrange(T):
    N,K = map(int, raw_input().strip().split())
    
    #得到初始值
    string = ""
    for i in xrange(N):
        if i % 2 == 0:
            string += "1"
        else:
            string += "0"
    string = list(string)
    for i in xrange( 1, K ):
        string = Add( string, 1 )
        if string[0] == "-1":
            break
    if string[0] != "-1":
        print "".join(string)
    else:
        print -1
        
    