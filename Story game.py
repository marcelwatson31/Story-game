import time

#classes would of easily helped produce results quicker and easier, next time this will be done.
#and enter pause points for display of the text.


starting_class = ""
Boss = ""
Move = ""

def story_game():
    print("\n Answer 'yes' or 'no' to this following question \n")
    game_decision = input("Do you want to play this story game!? ").lower()
    if game_decision == "yes":
        print("Then lets play a game \n")
        choice_1 = input("What job class do you want?\n School Teacher \n Clown \n Baker \n Or Magician?\n Enter the name of the job you would like or the beginning letter.").lower()
        
        if choice_1 == "school teacher" or "s":
            starting_class= "School Teacher"
            Boss = "Principal Skinner"
            Move = "It's Barts fault"

        if choice_1 == "clown" or "c":
            starting_class = "Clown"
            Boss = "Penny Wise"
            Move = "My names not Georgie anyways sir."

        if choice_1 == "baker" or "baker":
            starting_class="Baker"
            Boss = "Gordon Ramsey"
            Move = "Cooking is all perspective anyways... 'fades into the distance with cries falling and your creation still on your face'"


        elif choice_1 == "magician" or "m":
            starting_class= "Magician"
            Boss = "Voldemort"
            Move = "Leviosa"

        print(f"\n So you are a {starting_class}! That is great")
        time.sleep(4)

        print(f"\n As a {starting_class} you encounter your arch nemesis {Boss}! Quick you must do something! ")
        time.sleep(7)

        print(f"\n {Boss} moves closer to you and attacks you!")
        time.sleep(6)

        print(f"\n You retort {Move} ! \n And {Boss} leaves you alone this time! \n Good Job you win!")
        time.sleep(6)

        final_game = input("\n Do you want to play again write yes or no? \n")

        if final_game =="yes":
            story_game()
        elif final_game != "yes":
            print("\n Thank you for playing! I hope you had fun!")






    elif game_decision != "yes":
        print(" \n That's alright I didn't want to have you play the game anyways!")
story_game()