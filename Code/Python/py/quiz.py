from random import choice

def pick_number(frm=1,to=10):
	return choice(range(frm,to+1))

def ask_question(first,second):
	qstr="What's "+str(first)+" times "+str(second)+ "? "
	ans=raw_input(qstr)
	if ans=="":
		return 0
	else:
		return int(ans)

questions = 5
right=0

for i in range(questions):
	first=pick_number()
	second=pick_number()
	ans=ask_question(first,second)
	rans=first*second
	if ans==rans:
		print "That's right : well done"
		right+=1
	else:
		print "Oh sorry, the right answer is :",rans

print "you got ",right," out of ",questions

