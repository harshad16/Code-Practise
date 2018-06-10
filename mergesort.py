def mergesort(a,b):
	c=[]
	while len(a)!=0 and len(b)!=0:
		if a[0]>b[0]:
			c.append(b[0])
			b.remove(b[0])
		else:
			c.append(a[0])
			a.remove(a[0])
	if len(a)==0:
		c+=b
	else:
		c+=a
	# print "c:",c
	return c


def merge(x):
	if len(x)==0 or len(x)==1:
		return x
	else:
		mid=len(x)/2
		a=merge(x[:mid])
		# print "a:",a
		b=merge(x[mid:])
		# print "b:",b
		return mergesort(a,b)

x=map(int,raw_input().strip())
print "before:",x
print "after:",merge(x)