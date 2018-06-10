try:
	while(True):
		t=raw_input()
		team_a=0
		team_b=0
		for count,item in enumerate(t):
			print "item",item,"team_a",team_a,"team_b",team_b
			if count%2==0:
				if item=='1':
					team_a+=1
			elif count%2!=0:
				if item=='1':
					team_b+=1
			if team_a<(team_b/2.0) and team_b>(5/2.0) and count%2==0:
				break
			if team_b<(team_a/2.0) and team_a>(5/2.0) and count%2==0:
				break
			if count==9:
				if team_a!=team_b:
					print "5count","team_a",team_a,"team_b",team_b
					break
			if count>9 and count%2!=0 and team_a!=team_b:
				print "team_a",team_a,"team_b",team_b
				break
		if team_b>team_a:
			print "TEAM-B",count+1
		elif team_b<team_a:
			print "TEAM-A",count+1
		elif team_b==team_a:
			print "TIE"
except:
	pass