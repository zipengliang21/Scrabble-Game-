## get all necessary modules
from SimpleScrabbleGame import ScrabbleCONSTANTS
from SimpleScrabbleGame.ScrabblePlayer import *
import tkinter as tk
from tkinter import simpledialog, messagebox
import threading

root = tk.Tk()
w = 0 # width for the Tk root
h = 0 # height for the Tk root

# calculate x and y coordinates for the Tk root window
x = 300
y = 300

# set the dimensions of the screen
# and where it is placed
root.geometry('%dx%d+%d+%d' % (w, h, x, y))

# root.iconify()
root.withdraw()
## start the game
print("~~~Welcome to my SCRABBLE game~~~\n\n\n")
## get the number of rounds to play
numRounds = simpledialog.askinteger("Input", "How many rounds(> 0)?")
## get the type of game we are going to play
# root.deiconify()
numPlayers = simpledialog.askinteger("Input", "How many players(0[vs Computer],1[1 player mode],2[2 player mode])?")

# root.iconify()

## initiate the random letter weights and display them
ScrabbleCONSTANTS.SetLetterWeights()
print("LETTER WEIGHTS:")
letterWeights = ""
for i in range(len(ScrabbleCONSTANTS.LETTER_WEIGHTS)):
    letterWeights +=  chr(ord('a') + i) + ": " + str(ScrabbleCONSTANTS.LETTER_WEIGHTS[i]) + ", \t"
    if (i + 1) % 7 == 0:
        letterWeights += "\n"
messagebox.showinfo("Letter's weighting Information", letterWeights)
    # print(chr(ord('a') + i) + ": " + str(ScrabbleCONSTANTS.LETTER_WEIGHTS[i]), end=", \t")
    # if (i + 1) % 7 == 0:
    #     print()
# print("\n")

## get the list of words as a ScrabbleWORDS object
w = ScrabbleCONSTANTS.ScrabbleWORDS()

validRound = True
validPlayers = True
if (numRounds <= 0):
    messagebox.showerror("Error", "Invalid Round number!")
    validRound = False
if (numPlayers < 0 or numPlayers > 2):
    messagebox.showerror("Error", "Invalid Players number!")

    validPlayers = False

if (numPlayers == 0 and validRound == True and validPlayers == True):  ## vs Computer
    print("HUMAN players MUST enter 3 consecutive empty strings to end round.\n")
    print(":::VS COMPUTER MODE:::\n")
    hand1 = Hand("")
    human = HumanPlayer("human", hand1)
    hand2 = Hand("")
    computer = ComputerPlayer("computer", hand2)
    for i in range(numRounds):
        print("***** ROUND " + str(i + 1) + " *****")

        human.hand = Hand()
        print(human)
        print(human.hand)
        human.PlayHand(w)
        print(human)
        if (human.hand.IsEmpty()):
            print("Turn Ended! Hand is empty.")
        else:
            print("Turn Ended! Too many empty strings.")
        computer.hand = Hand()
        print(computer)
        print(computer.hand)
        computer.PlayHand(w)
        print(computer)
        if (human.hand.IsEmpty()):
            print("Turn Ended! Hand is empty.")
        else:
            print("Turn Ended! Cannot generate any more words.")

        if (human.__eq__(computer) is True):
            print("Round Result: Draw")
        elif (human.__gt__(computer) is True):
            print("Round Result: human wins!")
        else:
            print("Round Result: computer wins!")
        print("*** END OF ROUND ***\n")
    print("\n")
    print("~~~~~FINAL RESULT~~~~~")
    print(str(human.GetName()) + "\n" + "Total Score: " + str(human.GetScore()) +
          "\nTotal Time Taken: " + str(human.GetTime()) + "\n" + str(computer.GetName()) +
          "\n" + "Total Score: " + str(computer.GetScore()) + "\nTotal Time Taken:" +
          str(computer.GetTime()) + "\n~~~~~~~~~~~~~~~~~~~~~~\n\n\nThank you for playing.")
elif (numPlayers == 1 and validRound == True and validPlayers == True):  ## 1 player mode
    print("HUMAN players MUST enter 3 consecutive empty strings to end round.\n")
    print(":::SINGLE PLAYER MODE:::")
    hand1 = Hand("")
    human = HumanPlayer("human", hand1)
    for i in range(numRounds):
        print("***** ROUND " + str(i + 1) + " *****")
        human.hand = Hand()
        print(human)
        print(human.hand)
        human.PlayHand(w)
        print(human)
        if (human.hand.IsEmpty()):
            print("Turn Ended! Hand is empty.")
        else:
            print("Turn Ended! Too many empty strings.\n")
    print("*** END OF ROUND ***\n\nThank you for playing.")
elif (numPlayers == 2 and validRound == True and validPlayers == True):  ## 2 player mode
    print("HUMAN players MUST enter 3 consecutive empty strings to end round.\n")
    print(":::TWO PLAYER MODE:::")
    hand1 = Hand("")
    human1 = HumanPlayer("human1", hand1)
    hand2 = Hand("")
    human2 = HumanPlayer("human2", hand2)
    for i in range(numRounds):
        print("***** ROUND " + str(i + 1) + " *****")
        human1.hand = Hand()
        print(human1)
        print(human1.hand)
        human1.PlayHand(w)
        print(human1)
        if (human1.hand.IsEmpty()):
            print("Turn Ended! Hand is empty.")
        else:
            print("Turn Ended! Too many empty strings.\n")
        human2.hand = Hand()
        print(human2)
        print(human2.hand)
        human2.PlayHand(w)
        print(human2)
        if (human2.hand.IsEmpty()):
            print("Turn Ended! Hand is empty.")
        else:
            print("Turn Ended! Too many empty strings.\n")

        if (human1.__eq__(human2) is True):
            print("Round Result: Draw")
        elif (human1.__gt__(human2) is True):
            print("Round Result: human1 wins!")
        else:
            print("Round Result: human2 wins!")

        print("*** END OF ROUND ***\n")
    print("\n")
    print("~~~~~FINAL RESULT~~~~~")
    print(str(human1.GetName()) + "\n" + "Total Score: " + str(human1.GetScore()) +
          "\nTotal Time Taken: " + str(human1.GetTime()) + "\n" + str(human2.GetName()) +
          "\n" + "Total Score: " + str(human2.GetScore()) + "\nTotal Time Taken:" +
          str(human2.GetTime()) + "\n~~~~~~~~~~~~~~~~~~~~~~\n\n\nThank you for playing.")





