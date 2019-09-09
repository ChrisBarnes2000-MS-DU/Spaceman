import random
letters_guessed = []
display_attempt = []

def spaceman(secret_word):
    '''A function that controls the game of spaceman. Will start spaceman in the command line.
        Args:
          secret_word (string): the secret word to guess.
    '''
    #TODO: show the player information about the game according to the project spec

    #TODO: Ask the player to guess one letter per round and check that it is only one letter
    incorrect = 0
    for i in range(len(secret_word)):
        display_attempt.append("_")
    playing = True
    while(playing):
        if(incorrect == 7):
            playing = False
        else:
            guess = get_letter()
            letters_guessed.append(guess)
            is_word_guessed(secret_word, letters_guessed)
            #TODO: check if the letter guess is in the secret word
            print("\n")
            print("------Secret word is: " + secret_word + "------")
            print("------Recent Guess was: " + guess + "------")
            print(letters_guessed)
            print("------Incorrect Number: " + str(incorrect))

            #for letters in secret_word:
            if guess in secret_word:
                print("Correct")
                display_attempt.append(guess)
            else:
                print("incorrect")
                incorrect += 1
            print(''.join(display_attempt))
    print("Game over, You failed")

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
    print("initial show of secret: " + secret_word)
    return secret_word

def get_letter():
    letter = input("Guess the next letter: ")
    if len(letter) != 1 or not letter.isalpha():
        letter = input("Guess is too long or a number, please try again: ")
    return letter

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

#These function calls that will start the game
secret_word = load_word()
spaceman(secret_word)
