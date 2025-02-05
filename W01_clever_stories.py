#I added in \t and \n to make the story look better once it prints. Also added extra verbs and colors for the user to input. I made the input "asks" into sentences so it would read more human when the user was prompted to pick a word.

##W01 Project: Clever Stories
##Author: Helaman Menk

print("Please enter the following words:")
adjective = input("Type an adjective: ")
animal = input("Please type the name of an animal: ")
verb = input("Please type an action word: ")
exclamation = input("Please type an exclamation: ")
verb2 = input("Please type another action word: ")
verb3 = input("Please type a third action word: ")
verb_past = input("Please type an action word in the past tense: ")
color = input("Choose a color: ")

print("Your story is:")
print(f" \t The other day, I was really in trouble. It all started when I saw a very {adjective} {animal} {verb} down the hallway.'{exclamation.title()}'! I yelled. \n But all I could think to do was to {verb2} over and over. Miraculously, that caused it to stop, but not before it tried to {verb3} right in front of my family.\n It's been weeks and I can't get it out of my head, the {animal} could have {verb_past}.")