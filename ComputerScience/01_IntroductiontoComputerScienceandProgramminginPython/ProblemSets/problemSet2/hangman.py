# Problem Set 2, hangman.py
# Name: Hung Tran Van and Dat Pham Tien 
# Collaborators:
# Time spent: 3 weeks

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print(len(wordlist), "words loaded.\n")
    return wordlist

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()

# Dat PT
def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    for letter in secret_word:
        if letter not in letters_guessed:
            return False
    return True

#hungtran: return any([True for ch in word_list if ch not in letters_guessed])

#  Dat PT
def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    guessed_word = ""
    for letter in secret_word:
        if letter in letters_guessed:
            guessed_word = guessed_word + letter
        else:
            guessed_word = guessed_word + '_ '

    return guessed_word


#  hungtran
def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    alphabet = string.ascii_lowercase
    available_letters = []

    for ch in alphabet:
        if ch not in letters_guessed:
            available_letters.append(ch)
    return "".join(available_letters)

#  hungtran and Dat PT
def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    Starts up an interactive game of Hangman.
    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses s/he starts with.
    * The user should start with 6 guesses
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.
    * After each guess, you should display to the user the
      partially guessed word so far.
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"   print("Welcome to the game Hangman!")
    letters_guessed = [] # to store correct letters which are guessed
    guesses_remaining = 6 # maximum number of guesses 
    warnings_remaining = 3 # accidents in typing    
    vowels = ('a', 'i', 'e', 'o', 'u')

    secret_letters = []
    for ch in secret_word:
        if ch not in secret_letters:
            secret_letters.append(ch)
    number_unique_letters = len(secret_letters)

    print("I am thinking of a word that is %d letters long."
          % len(secret_word))
    print("You have", warnings_remaining, "warnings left.\n-------------------------")
    # convert string into list of char
    word_list = []
    for ch in secret_word:
        word_list.append(ch)

    while guesses_remaining > 0 and not is_word_guessed(secret_word, letters_guessed):
        #print(letters_guessed)
        print("You have", guesses_remaining, "guesses left.")
        print("Available letters:", get_available_letters(letters_guessed))
        guess_letter = input("Please guess a leter: ") # note in python2 we use raw_input() function
        guess_letter = str.lower(guess_letter)
        while (not str.isalpha(guess_letter) or (guess_letter in letters_guessed)) and warnings_remaining >= 0:
            warnings_remaining -= 1
            if not str.isalpha(guess_letter):
                print("Oop! That is not a valid letter. You have %d warnings left:"
                       % warnings_remaining, get_guessed_word(secret_word, letters_guessed),
                       "\n--------------------")

            if guess_letter in letters_guessed and warnings_remaining >= 0:
                print("Oop! You've already guessed that letter. You now have %d warnings left."
                      % warnings_remaining, get_guessed_word(secret_word, letters_guessed),
                      '\n-----------------------')
            #TODO
            if warnings_remaining < 0:
                guesses_remaining -= 1
                print("Oop! You've already guessed that letter. You have no warnings left so you lose one guess:",
                    get_guessed_word(secret_word, letters_guessed), "\n--------------------")

            print("You have", guesses_remaining, "guesses left.")
            print("Available letters:", get_available_letters(letters_guessed))

            guess_letter = input("Please guess a leter: ")
            guess_letter = str.lower(guess_letter)
        if (guess_letter in vowels) and (guess_letter not in letters_guessed) and (guess_letter not in secret_word):
            guesses_remaining -= 1
        letters_guessed.append(guess_letter)
        if guess_letter in secret_word:
            print("Good guess! ", get_guessed_word(secret_word, letters_guessed),
                  "\n------------------------")
        else:
            print("Oops! That letter is not in my word: ",
                  get_guessed_word(secret_word, letters_guessed),
                  "\n------------------------")
            guesses_remaining -= 1
    # check the word is guessed or not
    if is_word_guessed(secret_word, letters_guessed):
        print("Congratulation, you won!")
    else:
        print("Sorry, you run out of guesses. The word was else.")
    print("Your total score for this game is: ", guesses_remaining*number_unique_letters)
    print(secret_word)

# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------


# Dat Pham Tien
def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise:
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    my_word = my_word.replace(' ', '')
    if len(my_word) != len(other_word):
        return False
    else:
        for i in range(len(my_word)):
            if my_word[i] != '_' and (
                my_word[i] != other_word[i] \
                or my_word.count(my_word[i]) != other_word.count(my_word[i]) \
            ):
                return False
        return True

    # hungtran solution
    """
    new_word = ""
    tmp = ""
    for ch in my_word:
        if ch != ' ':
            new_word += ch
    if len(new_word) == len(other_word):
        for i in range(len(other_word)):
            if new_word[i] != '_':
                tmp += other_word[i]
            else:
                tmp += '_'
        if tmp == new_word:
            return True
        else:
            return False
    else:
        return False
    """

# Dat PT
def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    words_list = open(WORDLIST_FILENAME, 'r').readline().split()
    possible_matches = []
    for other_word in words_list:
        if match_with_gaps(my_word, other_word):
            possible_matches.append(other_word)
    if len(possible_matches) != 0:
        print("Possible word matches are: ",' '.join(possible_matches))
    else:
        print("No match found")


# hungtran and Dat PT
def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    Starts up an interactive game of Hangman.
    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses s/he starts with.
    * The user should start with 6 guesses
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.
    * After each guess, you should display to the user the
      partially guessed word so far.
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word.
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    letters_guessed = [] # to store correct letters which are guessed
    guesses_remaining = 6 # maximum number of guesses 
    warnings_remaining = 3 # accidents in typing    
    vowels = ('a', 'i', 'e', 'o', 'u')

    secret_letters = []
    for ch in secret_word:
        if ch not in secret_letters:
            secret_letters.append(ch)
    number_unique_letters = len(secret_letters)

    print("I am thinking of a word that is %d letters long."
          % len(secret_word))
    print("You have", warnings_remaining, "warnings left.\n-------------------------")
    # convert string into list of char
    word_list = []
    for ch in secret_word:
        word_list.append(ch)

    while guesses_remaining > 0 and not is_word_guessed(secret_word, letters_guessed):
        #print(letters_guessed)
        print("You have", guesses_remaining, "guesses left.")
        print("Available letters:", get_available_letters(letters_guessed))
        guess_letter = input("Please guess a leter: ") # note in python2 we use raw_input() function
        guess_letter = str.lower(guess_letter)
        if guess_letter == '*':
            show_possible_matches(get_guessed_word(secret_word, letters_guessed))
        else:
            while (not str.isalpha(guess_letter) or (guess_letter in letters_guessed)) and warnings_remaining >= 0:
                warnings_remaining -= 1
                if not str.isalpha(guess_letter):
                    print("Oop! That is not a valid letter. You have %d warnings left:"
                           % warnings_remaining, get_guessed_word(secret_word, letters_guessed),
                           "\n--------------------")

                if guess_letter in letters_guessed and warnings_remaining >= 0:
                    print("Oop! You've already guessed that letter. You now have %d warnings left."                          % warnings_remaining, get_guessed_word(secret_word, letters_guessed),
                          '\n-----------------------')
                #TODO
                if warnings_remaining < 0:
                    guesses_remaining -= 1
                    print("Oop! You've already guessed that letter. You have no warnings left so you lose one guess:",
                          get_guessed_word(secret_word, letters_guessed), "\n--------------------")

                print("You have", guesses_remaining, "guesses left.")
                print("Available letters:", get_available_letters(letters_guessed))

                guess_letter = input("Please guess a leter: ")
                if guess_letter == '*':
                    show_possible_matches(get_guessed_word(secret_word, letters_guessed))
                    guesses_remaining += 1
                    guess_letter = input("Please guess a leter: ")
                else:
                    guess_letter = str.lower(guess_letter)
        if (guess_letter in vowels) and (guess_letter not in letters_guessed) and (guess_letter not in secret_word):
            guesses_remaining -= 1
        letters_guessed.append(guess_letter)
        if guess_letter != '*':
            if guess_letter in secret_word:
                print("Good guess! ", get_guessed_word(secret_word, letters_guessed),
                      "\n------------------------")
            else:
                print("Oops! That letter is not in my word: ",
                      get_guessed_word(secret_word, letters_guessed),
                      "\n------------------------")
                guesses_remaining -= 1
    # check the word is guessed or not
    if is_word_guessed(secret_word, letters_guessed):
        print("Congratulation, you won!")
    else:
        print("Sorry, you run out of guesses. The word was else.")
    print("Your total score for this game is: ", guesses_remaining*number_unique_letters)
    print(secret_word)

# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    secret_word = choose_word(wordlist)
    secret_word = 'apple' # for test
    #hangman(secret_word)

###############
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    #secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
