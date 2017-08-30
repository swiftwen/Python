

classmates = ['one','two','three',100]
print len(classmates)
print classmates[-1]
print classmates

print '--------------'

sum = 0
for t in range(101):
    sum=sum+t
print sum

print '--------------'

d = {'zhangsan':95,'lisi':58,'wenpneg':100}
print d['zhangsan']
d['wen'] = 101
print d
print 'a' in d
print 'wen' in d
print d.get('aaa')
print d.get('bbb',-1)
print '--------------'

s = set([1,1,2,3])
print s 
s.add(4)
s.add(5)
print s
s.remove(4)
print s
print '----------'








