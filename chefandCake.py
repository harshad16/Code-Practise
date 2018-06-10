t=input()
for _ in range(t):
	n,m=map(int,raw_input().split(" "))
	k=[]
	for i in range(n):
		k.append(list(raw_input()))
	
	cost1=0
	for a in k:
		# print "a cost1",a,"x",a[0]
		x=a[0]
		for j in range(1,m):
			if a[j]==x:
				if a[j]=="R":
					x="G"
					cost1+=5
				elif a[j]=="G":
					x="R"
					cost1+=3
			else:
				x=a[j]
		# print cost1
	
	cost2=0
	for a in k:
		# print "a cost2",a,"x",a[m-1]
		x=a[m-1]
		for j in range(m-2,-1,-1):
			if a[j]==x:
				if a[j]=="R":
					x="G"
					cost2+=5
				elif a[j]=="G":
					x="R"
					cost2+=3
			else:
				x=a[j]
		# print cost2

	if cost1<cost2:
		print cost1
	else:
		print cost2


