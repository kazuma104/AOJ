import math

def solve():
    a,b,C = map(int, input().split())
    sin = math.sin
    cos = math.cos
    PI = math.pi
    print(a*b*sin(C*PI/180)/2, a+b+(a**2+b**2-2*a*b*cos(C*PI/180))**0.5, b*sin(C*PI/180))

if __name__ == '__main__':
    solve()