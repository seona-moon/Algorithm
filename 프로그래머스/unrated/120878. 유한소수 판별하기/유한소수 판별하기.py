import math 

def solution(a, b):
    gcd = math.gcd(a,b)
    a, b = a//gcd, b//gcd
    if b%2==0:
        while b%2==0:
            b//=2
    if b%5==0:
        while b%5==0:
            b//=5
    return 1 if b==1 else 2