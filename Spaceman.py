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
        if(incorrect == len(secret_word)):
            playing = False
        elif is_word_guessed(secret_word, letters_guessed):
            print("YAY, You won!!!")
            playing = False
        else:
            print("\n------------------")
            guess = get_letter()
            if guess in letters_guessed:
                print("you already guessed that: ")
                guess = get_letter()
            #TODO: check if the letter guess is in the secret word
            elif guess in secret_word:
                print("You guessed correctly")
                letters_guessed.append(guess)
                for i, letter in enumerate(secret_word):
                    if letter in letters_guessed:
                        if display_attempt[i] == "_":
                            display_attempt[i] = guess
            else:
                print("your guess was incorrect")
                incorrect += 1
                letters_guessed.append(guess)

            print("guesses so far are: " + str(letters_guessed))
            print("You have " + str(len(secret_word) - incorrect) + " guesses left")
            print("Secret word is: " + secret_word)
            print("your progress is: " + ''.join(display_attempt))

    if (incorrect == len(secret_word)):
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
    print("You have " + str(len(secret_word)) + " chances to guess the word.")
    return secret_word

def get_letter():
    letter = input("Guess the next letter: ")
    while len(letter) != 1 or not letter.isalpha():
        letter = input("Guess is too long or a number, please try again: ")
    return letter

def is_word_guessed(secret_word, letters_guessed):
    '''A function that checks if all the letters of the secret word have been guessed.
    Args:
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.
    Returns: 
        bool: True only if all the letters of secret_word are in letters_guessed, False otherwise
    '''
    # TODO: Loop through the letters in the secret_word and check if a letter is not in lettersGuessed
    for letter in secret_word:
        if letter not in letters_guessed:
            return False
    return True

#These function calls that will start the game
secret_word = load_word()
spaceman(secret_word)
