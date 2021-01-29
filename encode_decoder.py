for _ in range(int(input())):
	s=input()
	l=len(s)
	cap=0
	smal=0
	spec=0
	num=0
	flag=0
	if l<10:
		print("NO")
	else:
		for i in s:
			if (i>=chr(65) and i<=char(90)):
				cap=cap+1
			if (i>=chr(97) and i<=chr(122)):
				smal=smal+1
			if (i>=chr(48) and i<=chr(57)):
				num=num+1
			if (i=="@" or i=="?" or i=="#" or i=="%" or i=="&"):
				spec=spec+1
		if cap>=1 and smal>=1 and spec>=1 and num>=1:
			if cap==1:
				if (s[0]>=chr(65) and s[0]<=chr(90)) or (s[l-1]>=chr(65) and s[l-1]<=chr(90)):
					flag=1
			if num==1:
				if (s[0]>=chr(48) and s[0]<=chr(57)) or (s[l-1]>=chr(48) and s[l-1]<=chr(57)):
					flag=1
			if spec==1:
				if (s[0]=="@" or s[0]=="?" or s[0]=="#" or s[0]=="%" or s[0]=="&") or (s[l-1]=="@" or s[l-1]=="?" or s[l-1]=="#" or s[l-1]=="%" or s[l-1]=="&"):
					flag=1
			if flag==1:
				print("N0")
			else:
				print("YES")
		else:
			print("NO")




