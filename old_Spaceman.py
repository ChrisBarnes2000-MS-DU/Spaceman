import random

def load_word():
    '''
    A function that reads a text file of words and randomly selects one to use as the secret word
        from the list.
    Returns: 
           string: The secret word to be used in the spaceman guessing game
    '''
    f = open('words.txt', 'r')
    words_list = f.readlines()
    f.close()

    words_list = words_list[0].split(' ')
    secret_word = random.choice(words_list)
    print("------Secret word is: " + secret_word + "------")
    return secret_word


def is_word_guessed(secret_word, letters_guessed):
    '''
    A function that checks if all the letters of the secret word have been guessed.
    Args:
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.
    Returns: 
        bool: True only if all the letters of secret_word are in letters_guessed, False otherwise
    '''
    # TODO: Loop through the letters in the secret_word and check if a letter is not in lettersGuessed
    for letter in secret_word:
        if letter not in letters_guessed:
            return True

def get_guessed_word(secret_word, letters_guessed):
    '''
    A function that is used to get a string showing the letters guessed so far in the secret word and underscores for letters that have not been guessed yet.
    Args: 
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.
    Returns: 
        string: letters and underscores.  For letters in the word that the user has guessed correctly, the string should contain the letter at the correct position.  For letters in the word that the user has not yet guessed, shown an _ (underscore) instead.
    '''

    #TODO: Loop through the letters in secret word and build a string that shows the letters that have been guessed correctly so far that are saved in letters_guessed and underscores for the letters that have not been guessed yet
    print("getting the guessed word: \n" + secret_word + ", " + str(letters_guessed))
    '''correct = ""
    dashes = ""
    for letters in secret_word:
        if guess in letters:
            correct += str(letters_guessed)
        num_dashes = len(secret_word) - len(letters_guessed)
    
    for i in range(len(secret_word)):
        dashes += "_"
    return correct + dashes
'''

def is_guess_in_word(guess, secret_word):
    '''
    A function to check if the guessed letter is in the secret word
    Args:
        guess (string): The letter the player guessed this round
        secret_word (string): The secret word
    Returns:
        bool: True if the guess is in the secret_word, False otherwise
    '''
    #TODO: check if the letter guess is in the secret word
    print("------Secret word is: " + secret_word + "------")
    print("Recent Guess was: "+ guess)

    if len(guess) == 1 and guess.isalpha():
        if is_guess_in_word(guess, secret_word):
            print("That was a corret guess, ")
            letters_guessed.append(guess)
            guess = get_letter()
        else:
            #TODO: show the guessed word so far
            print("{}, is not in the world, Try Again: " .format(guess))
            get_guessed_word(secret_word, letters_guessed)
            guess = get_letter()

    #print(str(letters_guessed))
    return guess in secret_word

def get_letter():
    letter = input("Guess the next letter: ")
    return letter

def spaceman(secret_word):
    '''
    A function that controls the game of spaceman. Will start spaceman in the command line.
    Args:
      secret_word (string): the secret word to guess.
    '''

    #TODO: show the player information about the game according to the project spec

    #TODO: Ask the player to guess one letter per round and check that it is only one letter
    guess = get_letter()
    is_guess_in_word(guess, secret_word)
    
    """
    playing = True
    while playing:
        print("out side of check")
        playing = False
        #TODO: check if the game has been won or lost
        #elif 
        #   playing = False;
        #   print("Congratulations")
        
        #TODO: Check if the guessed letter is in the secret or not and give the player feedback
"""

#These function calls that will start the game
letters_guessed = []
secret_word = load_word()
spaceman(secret_word)
