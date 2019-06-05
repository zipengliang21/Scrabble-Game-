import random

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
MAX_LETTERS_IN_HAND = 15
LETTER_WEIGHTS = [
    ##  a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
]
WORDS_FILE = "words.txt"


def SetLetterWeights():
    global LETTER_WEIGHTS
    ## lets use the first few fibonacci numbers as weights for the letters at random
    fibSeries = [0, 1, 1, 2, 3, 5, 8, 13]
    for i in range(len(LETTER_WEIGHTS)):
        LETTER_WEIGHTS[i] = fibSeries[random.randint(0, len(fibSeries) - 1)]
    return


class ScrabbleWORDS(object):
    def __init__(self):
        """
        Initializes a Wordlist object. Assumes WORDS_FILE exists inside the same
        folder as this file and opens it and reads every line into a list as a string
        whose white spaces at the end are missing.
        """
        ## open up the words file
        inputFile = open(WORDS_FILE)
        ## initiate an empty list of words
        self.WORDS = []
        ## for each line in the input file
        for line in inputFile:
            ## remove new line character and all white spaces, change to lowercase
            line = line.strip().lower()
            ## if line contains only letters and nothing else like apostrophe or digits
            if line.isalpha():
                ## add it to our list
                self.WORDS.append(line)
        ## important to always close the file for future usage
        inputFile.close()

    def HasWord(self, word):
        """
        Test whether WORDS has word.
        word: The word to check (a string)
        returns True if word is in WORDS, False otherwise
        """
        ## use Pythons in keyword to do this
        return word in self.WORDS

    def GetWORDS(self):
        """
        returns the list of words
        """
        ## if anyone is interested in the list of words
        return self.WORDS


