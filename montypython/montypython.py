#!/usr/bin/env python3

round = 0

while round < 3:
    print('Finish the movie title, "Monty Python\'s The Life of ______"')
    answer = input()
    answerlower = answer.lower()
    answerupper = answer.upper()
    round = round + 1
    if (answer == "Brian" or answerlower == "brian" or answerupper == "BRIAN" ):
        print("Correct!")
        break
    elif (round == 3):
        print("Sorry, the answer was Brian") 
    elif (answer == "shruberry"):
        print("You gave the super secret answer")
        exit()
    else:
        print('Sorry. Try again!')
