file = open('names', 'r')
for line in file:
	if line.startswith("\n"):
		break;
	else:
		f = open("names2.txt","a")
		line = line.strip()
		l = ["\"", line, "\", "]
		f.writelines(l)
		
	
