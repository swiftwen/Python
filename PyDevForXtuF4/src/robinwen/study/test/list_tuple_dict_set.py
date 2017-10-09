def myabs(x):
    if x<0:
        return -x
    else:
        return x

d={'wen':100,'wang':60,'zhang':70,'liu':99}
for k in d.iterkeys():
    print k
for v in d.itervalues():
    print v
for k,v in d.iteritems():
    print k,v