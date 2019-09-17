import random, os, time
#http://www.ascii-art.de/ascii/ab/astronaut.txt
filenames = ["head.txt", "body.txt", "left_arm.txt", "right_arm.txt", "hips.txt", "left_leg.txt", "right_leg.txt", "ground.txt", "flag_pole.txt", "top_flag.txt", "full.txt"]
frames = []

for name in filenames:
    with open(name, "r", encoding="utf8") as f:
        frames.append(f.readlines())

def spaceman(secret_word):
    '''A function that controls the game of spaceman. Will start spaceman in the command line.
        Args:
          secret_word (string): the secret word to guess.
    '''
    #TODO: Ask the player to guess one letter per round and check that it is only one letter
    letters_guessed = []
    display_attempt = []
    incorrect = 0
    for i in range(len(secret_word)):
        display_attempt.append("_")
    playing = True
    while(playing):
        if(incorrect == len(secret_word)):
            """Check if the user has ran out of guesses and go into ending the game"""
            print("\n------------------")
            print("Game over, You failed")
            print("The word was: " + secret_word)
            print("\n------------------")
            time.sleep(0.3)
            return
        elif is_word_guessed(secret_word, letters_guessed):
            """If they still have guesses, check if the word is guessed correctly"""
            animate(10)
            print("YAY, You won!!!")
            time.sleep(0.3)
            return
        else:
            """If the words not guessed and they still have guesses, play the game"""
            print("\n------------------")
            guess = get_letter()
            if guess in letters_guessed:
                """If they already guessed a letter prompt that they did and get a new input"""
                print("\nyou already guessed that: ")
                guess = get_letter()
            #TODO: check if the letter guess is in the secret word
            elif guess in secret_word:
                """If the input is a new letter check if its part of the secret word and append it to the proper lists"""
                print("\nYou guessed correctly")
                letters_guessed.append(guess)
                for i, letter in enumerate(secret_word):
                    if letter in letters_guessed:
                        if display_attempt[i] == "_":
                            display_attempt[i] = guess
            else:
                """If guess not in secret word increment number of incorrect and add the letter to guessed letters"""
                print("\nyour guess was incorrect \n")
                incorrect += 1
                letters_guessed.append(guess)
                animate(incorrect)

            #TODO: show the player information about the game according to the project spec
            """Prompts to display during game play"""
            print("You have " + str(len(secret_word) - incorrect) + " guesses left")
            print("guesses so far are: " + str(letters_guessed))
            #print("Secret word is: " + secret_word)
            print("your progress is: " + ''.join(display_attempt))

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
    return letter.lower()

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

#animation provied by https://www.youtube.com/watch?v=JavJqJHLo_M
def animate(incorrect):
    display_frame = frames[0: incorrect]
    for frame in display_frame:
        os.system('clear')
        print ("".join(frame))
        time.sleep(0.3)
    print("")

#These function calls that will start the game
if __name__ == "__main__":
    play = input("Press enter/return to start otherwise press (Q) to quit.  ")
    while(play.upper() != "Q"):
        secret_word = load_word()
        spaceman(secret_word)
        play = input("If you'd like to play again press any key otherwise press (Q) to quit.  ")
    print("you quit the game")

def test_is_word_guessed():
    assert(is_word_guessed("secret", ['s','e','c','r','e','t'])) == True, "word guessed function doesn't works correctly"

def test_print():
    assert not (print("this is a print statement")), "testing a print statement"

def test_animate():
    assert not (animate(10)), "animate testing didn't work"
