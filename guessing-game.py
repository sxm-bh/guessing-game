'''
The Challenge:
Write a program that picks a random integer from 1 to 100, and has players guess the number. The rules are:
If a player's guess is less than 1 or greater than 100, say "OUT OF BOUNDS"
On a player's first turn, if their guess is
within 10 of the number, return "WARM!"
further than 10 away from the number, return "COLD!"
On all subsequent turns, if a guess is
closer to the number than the previous guess return "WARMER!"
farther from the number than the previous guess, return "COLDER!"
When the player's guess equals the number, tell them they've guessed correctly and how many guesses it took!
'''
import random

# Pick a random integer from 1 to 100 using the random module and assign it to variable num
num = random.randint(1,100)
print(num)

# Print an introduction to the game and explain the rules
print("Welcome to the guessing game!")
print("I have chosen a number between 1 and 100.")
print("Can you guess the number?")
print("If your guess is within 10 of the number, I will say 'WARM!'")
print("If your guess is further than 10 away from the number, I will say 'COLD!'")
print("If you guess the number, I will tell you how many guesses it took.")
print("Let's get started!")

# Create a list to store guesses with 0 as placeholder value
guesses = [0]


while True:
    # asks for a valid guess
    guess = int(input("Enter your guess: "))
    print(guess)

    # If a player's guess is less than 1 or greater than 100, say "OUT OF BOUNDS"
    if guess < 1 or guess > 100:
        print('OUT OF BOUNDS')
        continue

    # compares the player's guess to our number. If the player guesses correctly, tell them they've guessed correctly and how many guesses it took! then break from the loop.
    if guess == num:
        print(f"You've guessed correctly! You took {len(guesses)} guesses!" )
        break

    # if you append all new guesses to variable guesses, then the previous guess is given as guesses[-2]
    guesses.append(guess)

    # Otherwise, tell the player if they're warmer or colder, and continue asking for guesses.
    if guesses[-2]:
        # On all subsequent turns, if a guess is closer to the number than the previous guess return "WARMER!"
        if abs(guess-num) < abs((guesses[-2])-num):
            print('WARMER!')
        # farther from the number than the previous guess, return "COLDER!"
        else:
            print('COLDER!')
    
    # On a player's first turn, if their guess is within 10 of the number, return "WARM!"
    else:
        if abs(guess-num) <= 10:
            print('WARM!')
    #further than 10 away from the number, return "COLD!"
        else:
            print('COLD!')