# Final Project Python Programming --- Khari Shiver
# I created a Wheel of Fortune game.


print('Hello and welcome to a Wheel of Fortune-ish game!')
print('What is your name?')
playerName = input()
print('Hello ' + playerName + '!' + ' Let\'s get started.')
print('There are three categories to choose from: expensive cars, sayings, and 70s soul musicians.\nA random amount '
	  'for a correctly guessed letter will be assigned and vowels can be purchased for $500. '
	  '\nIf you feel like you know the answer, type \'guess\'. The computer will now randomly pick a category.')

import random
# A variable is created to store the player's score along with values that will be assigned to letters.
playerScore = 0
scoreValues = [100, 250, 350, 400, 500, 750, 1500, 3000, 5000]
# A dictionary is created to store items the player will try to guess.
categories = {'Expensive Cars': ['Porsche', 'Mercedes Benz', 'Audi', 'BMW', 'Maserati', 'Lambroghini', 'Ferrari',
                                 'Lotus'],
              'Sayings': ['Actions speak louder than words', 'A bird in the hand is worth two in the bush',
                          'All good things come to an end', 'Among the blind the one eyed man is king',
                          'Fortune favors the bold', 'Ignorance is bliss'],
              '70s Soul Musicians': ['James Brown', 'Sly Stone', 'Aretha Franklin', 'Earth Wind & Fire',
                                     'Stevie Wonder', 'Chaka Khan']}

# A list is created to store letters that the player guesses.
alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
         'W', 'X', 'Y', 'Z']

# A list of vowels is created separately from 'alpha' to allow the player to be charged for their use.
vowels = ['A', 'E', 'I', 'O', 'U']

# Use the random function to randomly select a key/category, the select a value from the previously selected
# key/category. The key/category is printed so the players knows what they should be guessing.
randCategory = random.randint(0, (len(categories) - 1))
print('The category is:', list(categories.keys())[randCategory])
randVal = (categories[list(categories.keys())[randCategory]][random.randint(0, (len(list(categories[list(categories.keys())[randCategory]])) - 1))]).upper()
print('Please enter a letter ' + playerName)

# An empty list is created to store the blank values for the value selected.
guessList = []
for letter in randVal:
	if letter.isalpha():
	    guessList.append('_')
	else:
	    guessList.append(letter)

# A function is created to print the image of what begins as blanks and is filled as the players guesses correctly.
def guesslistprint(randVal):
    for letter in randVal:
        print(letter, end = ' ')
    print()
guesslistprint(guessList)

# A while loop is used to have the player input letters to guess the clue.
while True:
	while True:
		# A random amount is assigned to the letter picked and the player guess is taken.
		letterValue = random.choice(scoreValues)
		print('$' + str(letterValue), 'per correct letter')
		userGuess = input().upper()
		# If a player would like to guess the phrase prior to picking all the letters.
		if userGuess == 'GUESS':
			while True:
				correctAnswer = 0
				userGuess = input().upper()
				for char in range(len(userGuess)):
					if userGuess[char] == randVal[char]:
						correctAnswer += 1
					else:
						break
				if correctAnswer == len(userGuess):
					for char in range(len(userGuess)):
						if userGuess[char] == randVal[char]:
							if not guessList[char].isalpha():
								guessList[char] = userGuess[char]
								if userGuess[char] not in vowels and userGuess[char].isalpha():
									playerScore += letterValue
				else:
					print('Nice try but that is not correct. Please pick another letter.')
					guesslistprint(guessList)
					break
				if '_' not in guessList:
					guesslistprint(guessList)
					print('You have $' + str(playerScore) + ' in your bank. Keep going!')
					break
				else:
					for letter in range(len(guessList)):
						if randVal[letter] == userGuess:
							guessList[letter] = userGuess
				print('$' + str(playerScore))
				guesslistprint(guessList)
				if '_' not in guessList:
					break
			break
		# A player should only be able to guess a letter once. If they pick it a subsequent time, they are alerted and
		# given their total again
		elif userGuess not in alpha:
			print('You previously picked that letter. Please try again.')
			print('You have $' + str(playerScore) + ' in your bank. Keep going!')
		# A player can buy a vowel at which point the amount of the vowel is deducted from their bank.
		elif userGuess in vowels:
			if playerScore >= 500:
				alpha.remove(userGuess)
				for letter in range(len(guessList)):
					if randVal[letter] == userGuess:
						playerScore -= 500
						guessList[letter] = userGuess
			# If the player does not have enough money in their bank they cannot buy a vowel.
			else:
				print('You do not have enough money to buy a vowel. Keep guessing!')
			print('You have $' + str(playerScore) + ' in your bank. Keep going!')
			guesslistprint(guessList)
			if '_' not in guessList:
				break
		# If the player correctly guesses the letter, the it is removed from alpha and placed into the guessList and
		# their score in increased by the appropriate randomly generated amount.
		else:
			alpha.remove(userGuess)
			for letter in range(len(guessList)):
				if randVal[letter] == userGuess:
					guessList[letter] = userGuess
					playerScore += letterValue
			print('ou have $' + str(playerScore) + ' in your bank. Keep going!')
			guesslistprint(guessList)
			if '_' not in guessList:
				break
	# When the player all the _ have been replaced by actual values, the phrase has been successfully guessed.
	if '_' not in guessList:
		print('Congrats! You won the game ' + playerName + '!' + ' You really know your ' + list(categories.keys())[randCategory] + '!')
		break