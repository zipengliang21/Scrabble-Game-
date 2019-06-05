from SimpleScrabbleGame.ScrabbleHand import *
import time
import random


class Player(object):
    def __init__(self, name, hand):
        """
        Initialize a player new player with a name, hand, score and time taken.

        name: string
        hand: An object of type Hand.
        """
        self.name = name
        self.hand = hand
        self.score = 0
        self.time = 0

    def AddToScore(self, points):
        """
        Add points to this player's total score.

        points: the number of points to add to this player's score
        """
        self.score += points

    def AddToTime(self, time):
        """
        Add time to this player's time taken.

        time: the amount of time to add to this player's total time taken
        """
        self.time += time

    def GetScore(self):
        """
        Return this player's total score.
        """
        return self.score

    def GetTime(self):
        """
        Return this player's total time taken.
        """
        return round(self.time, 2)

    def GetName(self):
        """
        Return this player's name
        """
        return self.name

    def GetHand(self):
        """
        Return this player's hand.

        returns: the Hand object associated with this player.
        """
        return self.hand

    def __gt__(self, other):
        """
        Compare players by their scores, check if this player has higher score than the other.

        returns: True if this player's score is greater than other player's score,
        false otherwise.
        """
        return (self.GetScore() > other.GetScore())

    def __eq__(self, other):
        """
        Compare players by their scores, check if this player is the same as the other.

        returns: True if this player's score is equal to the other player's score,
        false otherwise.
        """
        return (self.GetScore() == other.GetScore())

    def __str__(self):
        """
        Represent this player as a string

        returns: a string representation of this player
        """
        ## building a string with player name and score and time taken
        return ("Player " + self.GetName() + "\nScore: " +
                str(self.GetScore()) + "\nTime Taken: " + str(self.GetTime()) + " secs.")


class ComputerPlayer(Player):
    """
    Inherits everything from Player as well as has its own PlayHand method
    that this object uses to play a hand (different from a human player).
    """

    def PlayHand(self, words):
        """
        Play a hand by selecting the word that maximizes the points given the current hand.
        Stop when no more words can be generated or hand is empty.

        words: a ScrabbleWORDS type object
        """
        lst = words.GetWORDS()  ## create a new word list from the file
        t1 = time.time()
        while (True):
            maxScore = 0
            maxWord = ""
            if (self.hand.IsEmpty() == True):  ## if the hand is empty then stop
                break
            wordCounter = 0  ## check whether the hand contains at least word
            for i in lst:  ## go through the words list
                if (self.hand.HasLetters(i)):  ## the hand has at least one word
                    wordCounter += 1  ## found a word
                    if (self.hand.Update(i, False) >= maxScore):  ## compare with the max value
                        maxScore = self.hand.Update(i, False)  ## set the max score
                        maxWord = i  ## the word has max score
            if (wordCounter == 0):  ## if no word is found then stop
                break

            self.hand.Update(maxWord)
            self.AddToScore(maxScore)
            print("Word Accepted:", maxWord, ", Points for this word:", maxScore)
            print(self.hand)
        t2 = time.time()
        self.AddToTime(t2 - t1)


class HumanPlayer(Player):
    """
    Inherits everything from Player as well as has its own PlayHand method
    that this object uses to play a hand (different from a computer player).
    """

    def PlayHand(self, words):
        """
        Play a hand by asking player to input a string. Check if the input string is empty
        or contains non-alphabetic characters, if yes then ask for input again, three mistakes
        in a row and turns over (lets call this an exit counter).
        If the input has alphabetic characters then reset the exit counter and check if the
        player's hand contains letters to make up the word, if yes then check if the input
        word is a valid english word, otherwise show appropriate messages.
        If a valid word has been formed then update players points. Show the current hand
        as well after forming the word.
        Turn may also end when the player's hand is empty.

        words: a ScrabbleWORDS type object
        """
        emptyString = 3  ## exit counter
        t1 = time.time()
        while (self.hand.IsEmpty() is False):  ## play while the hand is not empty
            inputWord = input("Enter a word: ")  ## input a word
            if (len(inputWord) == 0):  ## if the input is empty
                emptyString -= 1  ## decrement exit counter by 1
                print("Empty strings left to enter to end turn:", emptyString)
                if (emptyString == 0):  ## if three empty string then exit
                    break
            else:  ## input string is not an empty string
                emptyString = 3  ## reset the exit counter
                if (inputWord.isalpha() == False):  ## contains non-alphabetic characters
                    print("Input cannot have non-alphabetic characters")
                else:  ## valid input format
                    if (self.hand.HasLetters(inputWord)):  ## if in the hand
                        if (words.HasWord(inputWord)):  ## if is a english word
                            print("Word Accepted:", inputWord, ", Points for this word:",
                                  self.hand.Update(inputWord, False))
                            self.AddToScore(self.hand.Update(inputWord))
                            print(self.hand)
                        else:  ## not a word
                            print("Invalid Letters Used")
                    else:  ## not in the hand
                        print("Invalid Letters Used")
        t2 = time.time()
        self.AddToTime(t2 - t1)

##SetLetterWeights()
##print(LETTER_WEIGHTS)
##hand1 = Hand("aaaah")
##human = HumanPlayer("human", hand1)
##sc = ScrabbleWORDS()
##human.PlayHand(sc)
##print(human)

##SetLetterWeights()
##print(LETTER_WEIGHTS)
##hand1 = Hand("oeuaezfkjlcyrtn")
##computer = ComputerPlayer("computer", hand1)
##sc = ScrabbleWORDS()
##computer.PlayHand(sc)
##print(computer)
##print(hand1)




