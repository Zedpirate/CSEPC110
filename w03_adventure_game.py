#Milestone
#Week03 Adventure Game

#Author: Helaman Menk
#Creativity: I included many different options inwhich the player will be able to go through the story a few different times to try to figure out what's going on. I also got to show off my game to a couple of friends and it worked for them as well, it was pretty cool!

game = input("Hello, would you like to play a game? Yes or No:  ")

game_std = game.lower()

if game_std == "no":
    print()
    print("Game Over! You lose the game")

else: 
    print()
    print("You are walking through a dark forest and find two items: a MATCH and a FLASHLIGHT.")
    choice1 = input("Which one do you want to pick up?: ")
    choice1_std = choice1.lower()
    print(f"You chose the {choice1_std}! That could possible help.")
    
    if choice1_std == "match":
        choice2 = input("You pick up the match and strike it, and for an instant, the forest around you is illuminated. \n You see a large grizzly bear, and then the match burns out. \n Do you want to RUN, or HIDE behind a tree?: ")
        choice2_std = choice2.lower()
        
        if choice2_std == "run":
            choice3 = input("Which direction will you run? NORTH, SOUTH, WEST or EAST?: ")
            direction = choice3.lower()

            if direction == "north":
                    print()
                    print("You have run deeper into the forest, never to be seen again.")
            elif direction == "south":
                    print()
                    print("You realize you went right back to where you were and find a match and a flashlight again")
            elif direction == "east":
                    print()
                    print("You ran straight into the bear, what were you thinking? \n GAME OVER!")
            elif direction == "west":
                    print()
                    print("You come across a clearing where you can see the sky and sunlight shines into the area.")
        else:
            print()
            print("You tried to hide, however the bear still got to you! You lose the game!")
    else:
        if choice1_std == "flashlight":
            path2 = input("The flashlight keeps flickering, something weird is in the air. \n Do you want to explore, YES or NO?: ")
            path2_std = path2.lower()

            if path2_std == "yes":
                direction_path2 = input("Do you go towards the sound of running WATER, towards SINGING, or towards the smell of FOOD?: ")
                path3 = direction_path2.lower()

                if path3 == "water":
                    print()
                    print("You come across a huge body of water. As far as the eye can see. \n Once you look back you realize the forest is gone.")
                    path3 = input("Now you have only a small patch of sand to stand on, do you try to SWIM or STAY there?: ")
                    path3_std = path3.lower()
                    if path3_std == "SWIM":
                        print()
                        print("You swim until you can no longer swim. You try to float to stay alive. \n You are never seen again. \n GAME OVER!")
                    else:
                        print()
                        print("You wait and wait and wait. Eventually the sun sets and you wake up back in your bedroom, \n 'what a nightmare'")
                elif path3 == "singing":
                    print()
                    print("You see the most beautiful woman imaginable, an ethereal other worldly person. \n As soon as they see you, they start screeching, and you black out. \n You wake up back in your room, safe and sound")
                else: 
                    print()
                    print("You have found the very real home of the Fae, now you can never go home.")
            else:
                print()
                print("A bear runs at you and there is no escape!")     


              
            