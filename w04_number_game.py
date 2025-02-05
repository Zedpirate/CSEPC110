

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

magic_number = 6  
  while guess != magic_number
    guess = float(input("Guess a number?: "))
print()
    if guess < magic_number:
  print("Guess Higher")
    elif guess > magic_number:
  print("Guess Lower")
    else:
  print("You guessed it!")
