

#Helaman Menk
#Week04 Activity Number Game

#To import Python library that generates random number:
import random

number = random.randint(1, 10)
print(number)

magic_number = 6
guess = float(input("Guess a number?: "))

if guess < magic_number:
  print("Guess Higher")
elif guess > magic_number:
  print("Guess Lower")
else:
  print("You guessed it!")


guess = float(input("Guess a number?: "))
print()
if guess < magic_number:
  print("Guess Higher")
elif guess > magic_number:
  print("Guess Lower")
else:
  print("You guessed it!")


##Generates Random Number and gives hint in order to guess the number.
magic_number = random.randint(1,100)  
guess_count = 0

guess = float(input("Guess a number?: "))
guess_count = guess_count + 1
continue_playing = "yes"

while continue_playing == "yes":
    while guess != magic_number:
      if guess < magic_number:
        print("Guess Higher")
      elif guess > magic_number:
        print("Guess Lower")
      else:
        print("You guessed it!")
      guess = float(input("Guess a number?: "))
      guess_count = guess_count + 1
    print()
    print(f"It took you {guess_count} guesses")  
    playing = input("Would you like to play again (yes/no)?:  ")
    continue_playing = playing.lower()
    guess_count = 0
    magic_number = random.randint(1,10)  
    guess = float(input("Guess a number?: "))
print("Thanks for playing!")
