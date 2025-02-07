
#Helaman Menk
#Week04 Project Word Puzzle
#Creativity I was able to make it work like a word puzzle game, including the hints with Uppercase and lowercase letters.
#I found online on how to make random choices from a list and used it to make the game more interesting. I created index called secrets for the word to be chosen randomly from there.


import random

secrets = ["learn", "python", "coding", "programming", "data", "science", "machine", "learning"]
secret = random.choice(secrets)

guess_count = 0
letter_count = len(secret)

print("Welcome to the Word Puzzle Game!")
print("Try to guess the secret word.")
print()
print(f"The secret word has {letter_count} letters.")

for hint in range(letter_count):
    print("_", end=" ")

print()
print()

guess = ""
while guess != secret:
    guess = input("What is your guess?: ")
    guess_count = guess_count + 1
    
    if len(guess) != letter_count:
      print(f"Your guess must have {letter_count} letters.")
      print()
      continue
    else: 
      if len(guess) == letter_count:
        for i, letter in enumerate(guess):    
          if letter == secret[i]:
            print(letter.upper(), end=" ")
          elif letter in secret:
            print(letter, end=" ")
          else:
            print("_", end=" ")
        print()
        print("Try again!")
print("You guessed it!")
print(f"It took you {guess_count} guesses")
print()
print("Thanks for playing!")
