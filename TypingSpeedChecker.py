from datetime import datetime
class TypingSpeedChecker:
	def start(self):
		word='python makes problem solving enjoyable'
		print(word)
		print()
		start=datetime.now()
		type_sentence=input('type the word you: ').lower()
		end=datetime.now()
		
		cal_time=(end-start).total_seconds()
		
		
		print(f'you took {cal_time:.2f} seconds to finish typing')
		print()
		no_letters=len(type_sentence.split())
		if cal_time > 0:
			WPM=(no_letters/cal_time)*60
			print(f'your typing speed is {WPM:.2f}')
			print()
		else:
			print('''can't be divisible by 0''')
		correct=0
		for i in range (len(word)):
		      if word[i] == type_sentence[i]:
		      	correct+=1
		total_characters=len(word)
		accuracy=(correct/total_characters)*100
		print(f'accuracy = {accuracy:.2f}%')
		
		
type=TypingSpeedChecker()
while True:
	print('''====TYPING SPEED TESTER====
	1. enter typing speed checker
	2. exit''')
	choose=int(input('what do you want to do: '))
	match choose:
		case 1:
			type.start()
		case 2:
			break
		case _:
			print('invalid message')
