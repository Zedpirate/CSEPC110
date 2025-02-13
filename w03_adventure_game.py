#Milestone
#Week03 Adventure Game

#Author: Helaman Menk
#Creativity: I included many different options inwhich the player will be able to go through the story a few different times to try to figure out what's going on. I also got to show off my game to a couple of friends and it worked for them as well, it was pretty cool!

game = input("Hello, would you like to play a game? YES or NO:  \n type 'FINISH' when you want to stop")

game_std = game.lower()

while game_std != "FINISH"
  game = input("Hello, would you like to play a game? YES or NO:  \n type 'FINISH' when you want to stop")
    if game.lower() != "yes":
        while game != "yes"
            print("Game Over! You lose the game")
    game = input("Would you like to try again? YES or NO: ")
    else: 
        print()
        print("You are walking through a dark forest and find two items: a MATCH and a FLASHLIGHT.")
        choice1 == input("Which one do you want to pick up?: ")
        choice1_std == choice1.lower()
        print(f"You chose the {choice1_std}! That could possible help.")
        
        if choice1_std == "match":
            choice2 = input("You pick up the match and strike it, and for an instant, the forest around you is illuminated. \n You see a large grizzly bear, and then the match burns out. \n Do you want to RUN, or HIDE behind a tree?: ")
            choice2_std == choice2.lower()
            
            if choice2_std == "run":
                choice3 == input("Which direction will you run? NORTH, SOUTH, WEST or EAST?: ")
                direction == choice3.lower()
    
                if direction == "north":
                    choice3_north = input("As you move deeper into the forest you see a small cabin, do you approach? YES or NO: ")
                    if choice3_north == "yes":
                        print("When you try to approach you step on a bear trap and the large grizzly catches up to you")
                        continue
                    else:    
                        print("You try to go around it and continue North but you step on a bear trap.")
                        continue
                elif direction == "south":
                    print("You've been running for an hour and are completly lost.")
                    choice3_south == input("Do you build a shelter for the night? Yes or No: ")
                        if choice3_south.lower() == "yes":
                            print("You are able to build a small shelter and are rescued the next day")
                            continue
                        else:
                            print("You continue to walk,\n and walk,\n and walk, \n and walk. The sun never goes down, you keep walking.")
                            continue
                elif direction == "east":
                        print()
                        print("You ran straight into the bear, what were you thinking?")
                        choice3_east == input("Do you punch the bear or curl up into fetal position?: PUNCH or CURL")
                            if choice3_east.lower() = "punch":
                                print("The bear tears you apart")
                                continue
                            else:
                                print("The bear decides to ignore you and lets you go.")
                                continue
                elif direction == "west":
                        print()
                        print("You come across a clearing where you can see the sky and sunlight shines into the area.")
                        choice3_west == input("Do you continue into the forest or go back home? CONTINUE or HOME: ")
                        if choice3_west.lower() = "continue":
                            print("Now you have a snake chasing you!")
                            continue
                        else:
                            print("You make it safely home!")   
                            continue
            else:
                print()
                choice2_hide = input("Where will you hide? BEHIND a tree or JUMP in the lake")
                if choice2_hide.lower() == "behind":
                    print("The bear follows you as you try to hide.")
                    continue
                else: 
                    print("The bear catches up to you quickly, he thinks you're drowning, and offers to help.")
                    continue
        else:
            if choice1_std == "flashlight":
                path2 == input("The flashlight keeps flickering, something weird is in the air. \n Do you want to explore, YES or NO?: ")
                path2_std = path2.lower()
    
                if path2_std == "yes":
                    direction_path2 == input("Do you go towards the sound of running WATER, towards SINGING, or towards the smell of FOOD?: ")
                    path3 = direction_path2.lower()
    
                    if path3 == "water":
                        print()
                        print("You come across a huge body of water. As far as the eye can see. \n Once you look back you realize the forest is gone.")
                        path3 = input("Now you have only a small patch of sand to stand on, do you try to SWIM or STAY there?: ")
                        path3_std = path3.lower()
                        if path3_std == "SWIM":
                            print()
                            print("You swim until you can no longer swim. You try to float to stay alive.")
                            path3_water = input("Do you stay AWAKE or drift to SLEEP while you float?: )
                                if path3_water.lower() == "awake":
                                    print("You had your eyes closed, but you knock your head into something hard, it's the edge of your pool. \n You have no idea how you got there.")
                                    continue
                                else:
                                    print("You drift for what feels like forever, you no longer feel the sun on your face. You hear someone call your name and open your eyes.")
                                    continue
                        else:
                            print()
                            print("You wait and wait and wait and wait. Eventually the sun sets and you fall asleep.")
                            dream_color = input("Is your dream BLUE or YELLOW?: ")
                            if dream_color.lower() == "blue":
                                print("You wake up with a falling sensation, you look around and are 100's of feet in the air flying.")
                                continue
                            else:
                                print("You wake up in a field of sunflowers near your home, you're safe but don't know how you got there.")
                                continue
                    elif path3 == "singing":
                        path3_movies = input("Have you read 'The Hobbit'? YES or NO: ")
                        if path3_movies.lower() == "yes":
                            print("You see the most beautiful woman imaginable, an ethereal other worldly person. \n Other people appear all looking the same way, they warmly greet you.")
                            continue
                        else:
                            print("You see the most beautiful woman imaginable, an ethereal other worldly person. \n As soon as they see you they start screeching and you black out unable to fight back.")
                            continue
                    else: 
                        print()
                        print("You have found the very real home of the Fae, now you can never go home.")
                        continue
                else:
                    print()
                    print("A bear runs at you and there is no escape!")
                    continue
    
    
                  
                
