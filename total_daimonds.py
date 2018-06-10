t=input()
a=[]
for _ in range(t):
	n=input()
	k=(n-1)*(6)
	if k:
		a.append(n*k)
	else:
		a.append(2)
for i in a:
	print i