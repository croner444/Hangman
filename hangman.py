
import random


HANGMAN_ASCII_ART = """
_           _    _                              _            _   _               _    
\ \   __   / /__| | ___ ___  _ __ ___   ___    | |_ ___     | |_| |__   ___     | |__   __ _ _ __   __ _ _ __ ___   __ _ _ __        __ _  __ _ _ __ ___   ___
 \ \ /  \ / / _ \ |/ __/ _ \| '_ ` _ \ / _ \   | __/ _ \    | __| '_ \ / _ \    | '_ \ / _' | '_ \ / _' | '_ ' _ \ / _' | '_ \      / _` |/ _` | '_ ` _ \ / _ \  
  \ V /\ V /  __/ | (_| (_) | | | | | |  __/   | || (_) |   | |_| | | |  __/    | | | | (_| | | | | (_| | | | | | | (_| | | | |    | (_| | (_| | | | | | |  __/
   \_/  \_/ \___|_|\___\___/|_| |_| |_|\___|    \__\___/     \__|_| |_|\___|    |_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|     \__, |\__,_|_| |_| |_|\___|
                                                                                                   |___/                           |___/"""
win = """
                            _       ___
                 _        _(_)_ __  \ /
                 \ \ /\ / /| | '_ \ | |
                  \ V  V / | | | | ||_|
                   \_/\_/  |_|_| |_|(_)"""
lose = """
                 _  
                | | ___  ___  ___
                | |/ _ \/ __|/ _ \  
                | |_(_) \__ \  __/ _ _ _
                |____|_/|___/\___|(_)_)_)"""

MAX_TRIES = 7
print(HANGMAN_ASCII_ART, "\n", MAX_TRIES)


old_letter_guessed = []

def check_valid_input(letter_guessed, old_letters_guessed):
    letter_guessed = letter_guessed.lower()
    global old_letter_guessed
    if len(letter_guessed) > 1:
        print("X")
        print(" -> ".join(sorted(old_letter_guessed)))
        return False
       
    elif not(letter_guessed in "abcdefghijklmnopqrstuvwxyz"):
        print("X")
        print(" -> ".join(sorted(old_letter_guessed)))
        return False
       
    elif letter_guessed in old_letter_guessed:
        print("X")
        print(" -> ".join(sorted(old_letter_guessed)))
        return False
       
    else:
        old_letter_guessed += letter_guessed
        return True


def show_hidden_word(secret_word, old_letter_guessed):
    for char in secret_word:
        if char in old_letter_guessed:
            print(char, end =" ")
        else:
            print("_ ", end ="")


def check_win(secret_word, old_letter_guessed):
    for char in secret_word:
        if char not in old_letter_guessed:
            return False
    return True


HANGMAN_PHOTOS = {0: """   x-------x""", 1: """   x-------x
    |
    |
    |
    |
    |""", 2: """   x-------x
    |       |
    |       0
    |
    |
    |""", 3: """   x-------x
    |       |
    |       0
    |       |
    |
    |""", 4: """   x-------x
    |       |
    |       0
    |      /|
    |
    |""", 5: """   x-------x
    |       |
    |       0
    |      /|\  
    |
    |""", 6: """   x-------x
    |       |
    |       0
    |      /|\  
    |      /
    |""", 7: """   x-------x
    |       |
    |       0
    |      /|\  
    |      / \  
    |"""}

def print_hangman(num_of_tries):
    return HANGMAN_PHOTOS[num_of_tries]

num_of_tries = 0

file_path = "Anti Dark Lord Harry program point did begin to cover it Harry wondered what the Sorting Hat would say now if he could put it on his head\
No wonder Professor Quirrell had accused Harry of heading down the path of a Dark Lord Harry had been too slow on the uptake he should have seen the parallel right away\
Understand that the Dark Lord did not win that day His goal was to learn martial arts and yet he left without a single lesson\
Harry had entered the Potions class with the intent to learn Potions He left without a single lesson"
file_path = file_path.lower()

def choose_word(file_path, index):
    L = []
    L_file_path = file_path.split(" ")
   
    for i in L_file_path:
        if i not in L:
            L.append(i)
    count = len(L)
    return (count , L_file_path[(index-1) % len(L_file_path)])


index = random.randint(1, 100)
num_of_tries = 0
count, secret_word = choose_word(file_path, index)

print("\n")
print(print_hangman(num_of_tries))
num_of_tries += 1

print("\n")
show_hidden_word(secret_word, old_letter_guessed)

print("\n")
for i in range(1000):
    letter_guessed = input("Enter a char: ")
    booli = check_valid_input(letter_guessed, old_letter_guessed)
    if booli == True:
        if letter_guessed in secret_word:
            show_hidden_word(secret_word, old_letter_guessed)
            print("\n")
            if check_win(secret_word, old_letter_guessed) == True:
                print(win)
                break
        else:
            print(")-:")
            print(print_hangman(num_of_tries))
            print("You have just", 7-num_of_tries, "tries" )
            num_of_tries += 1
            show_hidden_word(secret_word, old_letter_guessed)
            print("\n")
            if num_of_tries == 8:
                print(lose)
                break






