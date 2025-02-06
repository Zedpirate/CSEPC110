
#Helaman Menk
#Week04 Project Word Puzzle

secret = "learn"
guess_count = 1
letter_count = len(secret)

print("Welcome to the Word Puzzle Game!")
print("Try to guess the secret word.")
print()
print(f"The secret word has {letter_count} letters.")

for hint in range(letter_count):
    print("_", end=" ")

print()
print()

guess = input("What is your guess?: ")
while guess != secret:
    print("Try again!")
    print()
    guess = input("What is your guess?: ")
    guess_count = guess_count + 1
print("You guessed it!")
print(f"It took you {guess_count} guesses")
print()
print("Thanks for playing!")

