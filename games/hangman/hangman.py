# Hangman against computer with random words chosen from a file

import random


def generate_word(file_path):
    """ First thing we do is open the file and save it as a variable 'file_object'.
        We store each line of the file in a LIST called "word_list", 
        with the .readlines() method.
        From that list we've just generated, choose randomly an element (word)
    """

    with open(file_path) as file_object:
        word_list = file_object.readlines()
        random_word = random.choice(word_list).strip()
        return random_word


def play_game(random_word, used_letters, MAX, alphabet):
    """ As we play the game,
        first we gotta choose a letter from the available alphabet options.
        Then, the algorithm checks with 'correct_letters' function if the letter is in random_word
    """
    print("\nChoose a letter from alphabet, the available letters are:\n", ' '.join(alphabet))
    letter = input("Letter: ").lower()
    word = correct_letters(letter, random_word, used_letters, MAX)
    alphabet = available_letters(letter, alphabet)
    gamesLeft = games_left(used_letters, MAX)
    if random_word == word and gamesLeft >= 0:
        print("You just won!!")
        return False
    elif random_word != word and gamesLeft > 0:
        print(f"You have {games_left(used_letters, MAX)} rounds left to win")
        play_game(random_word, used_letters, MAX, alphabet)
    else:
        print("You lost noobie!")
        print(f"The word was {random_word}")
        return False


def correct_letters(letter, random_word, used_letters, MAX):
    """ If the letter chosen by the user is:
        1. Correct, we add it to chosen_letters list and update the printable word.
        2. Incorrect, we missed a round.
        3. Correct but repeated, nothing happens.
        4. Incorrect but repeated, nothing happens.
        """
    if letter in random_word and letter not in used_letters:
        used_letters += letter
        user_word = print_word(random_word, used_letters)
        print("\nTHAT LETTER IS CORRECT!")
        print(f"The word is...:  {user_word}")
        
    elif letter not in random_word and letter not in used_letters:
        used_letters += letter
        user_word = print_word(random_word, used_letters)
        print("\nTHAT LETTER ISN'T IN THE WORD!")
        print(f"The word is...:  {user_word}")

    elif letter in random_word and letter in used_letters:
        user_word = print_word(random_word, used_letters)
        print("That letter is correct but it has been chosen before, so choose another letter please\n")

    elif letter not in random_word and letter in used_letters:
        user_word = print_word(random_word, used_letters)
        print("That letter ISN'T correct but it has been chosen before, so choose another letter please\n")

    return user_word


def print_word(random_word, used_letters):
    """ Update the printable word, so the user knows
        hows the game going
    """
    word = ''
    for i in range(len(random_word)):
        if random_word[i] in used_letters:
            word += random_word[i]
        else:
            word += "-"
    return word


def available_letters(letter, alphabet):
    """ Update alphabet for the user to know, which letters are left"""
    if letter in alphabet:
        pos = alphabet.index(letter)
        alphabet.pop(pos)
    return alphabet


def games_left(used_letters, MAX):
    gamesLeft = MAX - len(used_letters)
    return gamesLeft


if __name__ == '__main__':
    """ 
        1. Initialize maximum (MAX) rounds to play,
        2. the chosen letters at the beginning is an empty list,
        3. the alphabet is a list of chars,
        4. we generate a random word (explained in function),
        5. create a loop to play
    """

    MAX = 15
    file_path = '/Users/your_user/Documents/GitHub/english-words/words_alpha.txt'
    used_letters = []
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'k', 'l', 'm', 'n', 'o', 'p', \
        'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    play = True
    
    random_word = generate_word(file_path)
    
    print("WELCOME TO THE HANGMAN GAME!")
    
    while play == True:
        answer = input("WANNA PLAY?(yes or no)\n")
        if answer == "no":
            play = False
            break
        else:
            play = play_game(random_word, used_letters, MAX, alphabet)