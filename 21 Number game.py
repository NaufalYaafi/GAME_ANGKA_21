import random

# Python code to play 21 Number game

# returns the nearest multiple to 4
def nearestMultiple(num):
	if num >= 4:
		near = num + (4 - (num % 4))
	else:
		near = 4
	return near


def lose1():
	print ("\n\nYOU LOSE !")
	print("Better luck next time !")
	exit(0)
	
# checks whether the numbers are consecutive
def check(xyz):
	i = 1
	while i<len(xyz):
		if (xyz[i]-xyz[i-1])!= 1:
			return False
		i = i + 1
	return True

# starts the game

def start1():
	xyz = []
	last = 0
	while True:
		print ("Enter 'F' to take the first chance.")
		print("Enter 'S' to take the second chance.")
		chance = input('> ').strip().lower().upper()
		
		# player takes the first chance
		if chance == "F" :
			while True:
				if last >= 21:
					lose1()
				else:
					print ("\nYour Turn.")
					print ("\nHow many numbers do you wish to enter?")
					inp = int(input('> '))
					
					if inp > 0 and inp <= 3:
						comp = 4 - inp
						a = 1
						x = random.randint(a, comp)
						
					else:
						print ("Wrong input. You are disqualified from the game.")
						lose1()
			
					i, j = 1, 1

					print ("Now enter the values")
					while i <= inp:
						a = input('> ')
						if a.isdigit():
							a = int(a)
						else :
							print("Please input only a number")
						xyz.append(a)
						i = i + 1
					
					# store the last element of xyz.
					last = xyz[-1] 
					
					# checks whether the input 
					# numbers are consecutive
					if check(xyz) == True: 
						if last >= 21:
							lose1()
							
						else:
							#"Computer's turn."
							while j <= x:
								xyz.append(last + j)
								j = j + 1
							print ("Order of inputs after computer's turn is: ")
							print (xyz)
							last = xyz[-1]
							if last >= 21:
								print ("\n\nCONGRATULATIONS !!!")
								print ("YOU WON !")
								exit(0)
					else:
						print ("\nYou did not input consecutive integers.")
						lose1()
			
						
		# player takes the second chance
		elif chance == "S":
			while last <=21:
				comp = random.randint(1,3)
				#"Computer's turn"
				j = 1
				while j <= comp:
					xyz.append(last + j)
					j = j + 1
				print ("Order of inputs after computer's turn is:")
				print (xyz)
				if xyz[-1] >= 21:
					print ("\n\nCONGRATULATIONS !!!")
					print ("YOU WON !")
					exit(0)
					
				else:
					print ("\nYour turn.")
					print ("\nHow many numbers do you wish to enter?")
					inp = int(input('> '))
					i = 1
					print ("Enter your values")
					while i <= inp:
						xyz.append(int(input('> ')))
						i = i + 1
					last = xyz[-1]
					if check(xyz) == True:
						if last >= 21:
							lose1()
						
					else:
						# if inputs are not consecutive
						# automatically disqualified
						print ("\nYou did not input consecutive integers.")
						# print ("You are disqualified from the game.")
						lose1()
			print ("\n\nCONGRATULATIONS !!!")
			print ("YOU WON !")
			exit(0)
			
		else:
			print ("wrong choice")
						
		
game = True
while game == True:
		print ("Player 2 is Computer.")
		print("Do you want to play the 21 number game? (Yes / No)")
		ans = input('> ').strip().lower()
		if ans =='yes':
			start1()
		else:
			print ("Do you want quit the game?(yes / no)")
			nex = input('> ').strip().lower()
			if nex == "yes":
				print ("You are quitting the game...")
				exit(0)
			elif nex == "no":
				print ("Continuing...")

			else:
				print ("Wrong choice")
				

			
