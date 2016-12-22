import re


queries = ["remind me ", "weather"]



def check_reminder_request(n):
	a = re.match(r'^remind me', n)
	reminder = ""
	if a:
		for i in range(0, len(n)-1):
			if i in range(a.start(), a.end()+1):
				continue
			else:
				reminder+=n[i] # Adding all charcters without "remdind me"


	reminder+=n[::-1][0]   # Adding last character


	return reminder
