# 2609번 최대공약수와 최소공배수
n,m = map(int,input().split())

def gcd(a,b):
    if a%b==0:
        return b
    return gcd(b,a%b)

def lcm(a,b):
    return abs(a*b) // gcd(a,b)

print(gcd(n,m))
print(lcm(n,m))