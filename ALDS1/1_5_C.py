import math

def koch(n, p1, p2):
    if n == 0:
        return

    s = ( (p1[0]*2+p2[0])/3, (p1[1]*2+p2[1])/3 )
    t = ( (p1[0]+p2[0]*2)/3, (p1[1]+p2[1]*2)/3 )
    Sin = math.sin(math.radians(60))
    Cos = math.cos(math.radians(60))
    u = ((t[0]-s[0])*Cos-(t[1]-s[1])*Sin+s[0], (t[0]-s[0])*Sin+(t[1]-s[1])*Cos+s[1])
    
    koch(n-1,p1,s)
    print(*s)
    koch(n-1,s,u)
    print(*u)
    koch(n-1,u,t)
    print(*t)
    koch(n-1,t,p2)

if __name__ == "__main__":
    n = int(input())
    v1 = (0, 0)
    v2 = (100, 0)
    print('%.8f %.8f'%(v1[0], v1[1]))
    koch(n, v1, v2)
    print("{:.8f} {:.8f}".format(v2[0], v2[1]))