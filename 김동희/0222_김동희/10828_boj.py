import sys

a = int(sys.stdin.readline())
ls = []
while a > 0 :
    b=sys.stdin.readline().strip()
    if b.split()[0] == 'push' :
        num = int(b.split()[1])
        ls.append(num)
    elif b == 'top':
        if len(ls) ==0:
            print(-1)
        else:
            print(ls[-1])
    elif b == 'size':
        print(len(ls))
    elif b == 'empty':
        if len(ls) == 0:
            print(1)
        else:
            print(0)
    elif b == 'pop':
        if len(ls) ==0:
            print(-1)
        else:
            print(ls[-1])
            del ls[-1]
    a -= 1