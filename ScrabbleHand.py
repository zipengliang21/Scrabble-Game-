from SimpleScrabbleGame.ScrabbleCONSTANTS import *


class Hand(object):
    def __init__(self, initialHand=None):
        """
        Constructor for the hand class. Initializes a hand with random letters
        unless the hand is passed in as a string (initialHand).
        """
        ## check if we are in default mode
        if initialHand is None:
            ## our hand
            handSize = MAX_LETTERS_IN_HAND
            initialHand = []
            ##33.33% vowels
            numVowels = handSize // 3
            for i in range(numVowels):
                ## add a random vowel
                initialHand.append(VOWELS[random.randint(0, len(VOWELS) - 1)])
            ##66.67% consonants
            for i in range(numVowels, handSize):
                ## add a random consonant
                initialHand.append(CONSONANTS[random.randint(0, len(CONSONANTS) - 1)])
        else:
            ## preset hand
            handSize = len(initialHand)
            initialHand = list(initialHand)
        ## update current hand
        self.handSize = handSize
        self.hand = initialHand
        self.handFrequency = self.GetFrequency(initialHand)

    def GetFrequency(self, hand):
        """
        Get the frequency of each letter in hand (a list of letters)

        hand: a list of single letters where each letter is from a to z
        """
        ## initiate a 26 element (a to z) array with all zeros
        frequencies = [0 for i in range(26)]
        ## go through each letter
        for letter in hand:
            ## update the frequency count of that letter
            frequencies[ord(letter) - ord('a')] += 1
        return frequencies[:]

    def Update(self, word, remove=True):
        """
        Remove letters in word from this hand if remove is True and return the score,
        otherwise just return the score i.e. characters are not removed.
        Updates frequency as well if we are removing characters.

        word: The word (a string) of characters to remove from this hand permanently
        and calculate the points,
        remove: (a boolean) whether to remove characters and calculate the points
        or just to calculate the points. Default is True so remove characters.

        returns points gained from the removal of characters (actual removal of
        characters depends on the value of the remove variable).
        """
        score = 0
        if (self.HasLetters(word) and remove is True):  ## to remove the word
            for i in word:
                self.handFrequency[ord(i) - ord('a')] -= 1  ## update frequency
                score += LETTER_WEIGHTS[ord(i) - ord('a')]  ## calculate the points
                self.hand.remove(i)
                self.handSize -= 1
            return score
        elif (self.HasLetters(word) and remove is False):  ## get the score only
            for i in word:
                score += LETTER_WEIGHTS[ord(i) - ord('a')]
            return score

    def HasLetters(self, letters):
        """
        Test if this hand has the characters required to make the input
        string (letters) by using handFrequency

        returns: True if the hand has the characters to make up letters,
        False otherwise
        """
        if (self.IsEmpty()):
            return False
        elif (len(letters) > self.handSize):
            return False
        else:
            counter = 0
            copy = self.handFrequency[:]
            for i in letters:
                if (copy[ord(i) - ord('a')] > 0):
                    counter += 1
                    copy[ord(i) - ord('a')] -= 1
            if (counter == len(letters)):
                return True
            else:
                return False

    def IsEmpty(self):
        """
        Test if there are any more letters left in this hand.

        returns: True if there are no letters remaining, False otherwise.
        """
        if (self.handSize == 0):
            return True
        else:
            return False

    def __str__(self):
        """
        Represent this hand as a string

        returns: a string representation of this hand
        """
        ## initiate an empty accumulator string
        string = 'Hand: '
        ## for each letter in hand
        for letter in self.hand:
            ## add the letter (and some formatting) to the string accumulator
            string += (letter + ", ")
        return string

##hand1 = Hand("carrr")
##print(hand1.GetFrequency("carrr"))
##if (hand1.HasLetters("car")):
##    print(hand1.Update("car",False))
