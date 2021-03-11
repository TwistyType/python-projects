import random

HANGMANPICS = ['''

    +---+
    |   |
        |
        |
        |
        |
===========''', '''

    +---+
    |   |
    O   |
        |
        |
        |
===========''', '''

    +---+
    |   |
    O   |
    |   |
        |
        |
===========''', '''

    +---+
    |   |
    O   |
   /|   |
        |
        |
===========''', '''

    +---+
    |   |
    O   |
   /|\  |
        |
        |
===========''', '''

    +---+
    |   |
    O   |
   /|\  |
   /    |
        |
===========''', '''

    +---+
    |   |
    O   |
   /|\  |
   / \  |
        |
===========''']

words = 'apple orange lemon lime pear watermelon grape grapefruit cherry banana cantaloupe mango strawberry tomato'.split()

def get_random_word(word_list):
    #This function returns a random string from thr passed list of strings
    word_index = random.randint(0, len(word_list)-1)
    return word_list[word_index]

def display_board(HANGMANPICS, missed_letters, correct_letters, secret_word):
    print(HANGMANPICS[len(missed_letters)])
    print()

    print('Missed letters:', end = ' ')
    for letter in missed_letters:
        print(letter, end=' ')
    print()

    blanks = '_'*len(secret_word)

    for i in range(len(secret_word)): #replace blanks with correctly guessed letters
        if secret_word[i] in correct_letters:
            blanks = blanks[:i] + secret_word[i] + blanks[i+1:]

    for letter in blanks: #show the secret word with spaces in between each letter
        print(letter, end=' ')
    print()

def get_guess(already_guessed):
    #Returns the letter the player entered. This function makes sure the player entered a single letter, and not something else.

    while True:
        print('Guess a letter: ')
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print('Please enter a single letter. ')
        elif guess in already_guessed:
            print('You have already guessed that letter. Choose again. ')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Please enter a LETTER. ')
        else:
            return guess

def play_again():
    #This function returns True if the player wants to play again, otherwise it returns False.
    print('Do you want to play again? (yes/no)')
    return input().lower().startswith('y')

#---------------------------------------------------------------------------------------------------------------------------------------------------

print('H A N G M A N')
missed_letters = ''
correct_letters = ''
secret_word = get_random_word(words)
game_is_done = False

while True:     # main loop of program
    display_board(HANGMANPICS, missed_letters, correct_letters, secret_word)

    #Let the player type in a letter
    guess = get_guess(missed_letters + correct_letters)

    if guess in secret_word:
        correct_letters = correct_letters + guess

        #Check if the player has won
        found_all_letters = True
        for i in range(len(secret_word)):
            if secret_word[i] not in correct_letters:
                found_all_letters = False
                break
        if found_all_letters:
            print('Yeah!, The secret word is "' + secret_word + '"! You have won!')
            game_is_done = True

    else:
        missed_letters = missed_letters + guess

        #Check if player has guessed too many times and lost
        if len(missed_letters) == len(HANGMANPICS)-1:
            display_board(HANGMANPICS, missed_letters, correct_letters, secret_word)
            print('You have run out of guesses!\nAfter ' + str(len(missed_letters)) + ' missed guesses and ' + str(len(correct_letters)) + ' correct guesses, the word was "' + secret_word + '"')
            game_is_done = True

    if game_is_done:
        if play_again():
            missed_letters = ''
            correct_letters = ''
            game_is_done = False
            secret_word = get_random_word(words)
        else:
            break
    


