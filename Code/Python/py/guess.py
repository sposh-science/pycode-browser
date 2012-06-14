from random import choice
import string

def gen_guess():
	return choice(range(1,1001))

def read_yesorno(prompt='Yes or no? '):
    if prompt<>'' and prompt[-1] not in string.whitespace:
        prompt = prompt + ' '
    while 1:
        result = raw_input(prompt)
        try: result = string.lower(string.split(result)[0])
        except: result=''
        if result=='yes' or result=='y': return 1
        if result=='no' or result=='n': return 0
        print "Please answer yes or no."


chances=10
while True:
	guessed=False
	print "I'v thought of a number between 1 and 1000."
	guess=gen_guess()
	for i in range(chances):
		num=input("make a guess: ")
		if num < guess:
			print "That's too low"
		elif num >guess:
			print "That's too high"
		else:
			print "That was my number, well done!"
			print "you took ",i,"guesses"
			guessed=True
			break
	if not guessed:
		print "The number i thought is ",guess," game over"
	if not read_yesorno("Would you like to play another? (yes/no) ") :
		break