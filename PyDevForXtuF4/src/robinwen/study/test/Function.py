print abs(-100)
print '---------'

print int(12.8888)

def my_abs(n):
    if n<0:
        return 0
    else:
        return -n

print my_abs(-100)
print my_abs(3)
print '----------------'

def power(x,n=2):
    ans = 1
    i = 1
    while i<=n:
        ans=ans*x
        i=i+1
    return ans

print power(2,10)
print power(5)

print '-------------'
def myAdd(*num):
    ans = 0
    for i in num:
        ans=ans+i 
    return ans
print myAdd(1,2,3,5)

print '-------------'













