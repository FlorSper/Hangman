# Hangman game
# -----------------------------------

import random
import string

WORDLIST_FILENAME = "C:/Users/Florian/Documents/Programming Material/Hangman/words.txt"

def loadWords():
    
    #Returns a list of valid words. Words are strings of lowercase letters.
    
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
    False otherwise
    '''
    
    new = ''
    for n in secretWord:
        if n in lettersGuessed:
            new += n
            if new == secretWord:
                return True
        else:
            return False

# ----------------------------------------

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    
    userWord = list(secretWord)
    for i in userWord:
        if i not in lettersGuessed:
            userWord[userWord.index(i)] = ' _ '
    transtring = ''.join(userWord)
    return transtring

# ------------------------------------------------

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    
    import string
    letters = string.ascii_lowercase
    availableLetters = list(letters)
    for i in lettersGuessed:
        if i in availableLetters:
           availableLetters.remove(i)
    transtring = ''.join(availableLetters)
    return transtring
    
# ------------------------------------------------

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    initializes the game.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

   
    '''
    
    print "Prepare to guess for your life!"
    print "I am thinking of a word that has " + str(len(secretWord)) + " letters"
    print '-' * 11
    guesses = 8      # No. of guesses
    lettersGuessed = []   # Creating empty list
    Alletters = string.ascii_lowercase    # String containing all the lowercase letters
    while guesses > 0 or not isWordGuessed(secretWord, lettersGuessed):    # Game starts
        print "You have " + str(guesses) + " guesses left!"
        print "Your options: " + str(Alletters)
        letters = raw_input("Choose a letter, fool!: ")
        if type(letters) != str:
            print "Trying to cheat eh?! Pick ONE letter!"
        else:
            letterslower = letters.lower()     # Transfering input into lowercase
            lettersGuessed.append(letterslower)  # Inserting inputs into a list
            if letterslower not in Alletters:
                print "Muahaha! you've tried that one already, imbicile!: " + getGuessedWord(secretWord, lettersGuessed)
            else:
                if isWordGuessed(secretWord, lettersGuessed) == "True":
                    print "Curse you! you have defeated me!"
                else:
                    print "So far, so lucky: " + getGuessedWord(secretWord, lettersGuessed)
                    print '-' * 11
                    guesses -= 1
                    Alletters = getAvailableLetters(lettersGuessed)
    print "Bahaha! You're hung!. The word was " + str(secretWord) 





# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
