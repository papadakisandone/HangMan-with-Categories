import random
import os
from colorama import Fore, Back, Style, init

# choices
menucountries = 1
menuwords = 2
menuanimals = 3
menurand_diction = 4
exit = "x"

# listes
letters_in_use = []  # letters that i have already used
words = []
countries = []
animals = []
randomtxt = []
lista = []


def draw_man(lifes):
    hangman_draw = ['''
 +---+
 |
 |
 |
===''', '''
 +---+
 |   O
 |
 |
===''', '''
 +---+
 |   O
 |   |
 |
===''', '''
 +---+
 |   O
 |  /|
 |   
===''', '''
 +---+
 |   O   
 |  /|\  
 |
===''', '''
 +---+
 |   O   
 |  /|\  
 |  /    
===''', '''
 +---+
 |   O   
 |  /|\  
 |  / \  
===''']

    if lifes == 6:
        return str(hangman_draw[0])
    elif lifes == 5:
        return str(hangman_draw[1])
    elif lifes == 4:
        return str(hangman_draw[2])
    elif lifes == 3:
        return str(hangman_draw[3])
    elif lifes == 2:
        return str(hangman_draw[4])
    elif lifes == 1:
        return str(hangman_draw[5])
    elif lifes == 0:
        return str(hangman_draw[6])


def file_txt(choice):
    if choice == menucountries:
        f = open('.\dictionaries\countries.txt', 'r')
        for line in f:
            lista.append(line.strip().upper())
        return lista
    elif choice == menuwords:
        f = open('.\dictionaries\words.txt', 'r')
        for line in f:
            lista.append(line.strip().upper())
        return lista
    elif choice == menuanimals:
        f = open('./dictionaries/animals.txt', 'r')
        for line in f:
            lista.append(line.strip().upper())
        return lista
    elif choice == menurand_diction:
        txt = random.choice(os.listdir('./dictionaries/'))  # pick random file from that folder
        # print(txt)
        f = open('./dictionaries/' + txt, 'r')
        for line in f:
            lista.append(line.strip().upper())
        return lista
    lista.clear()


def dictionary_words(choice):

    if choice == menucountries:
        return_file = file_txt(choice)
        rand_word = random.choice(return_file)  # pick random element from list
        split_word = list(rand_word)  # slit the word in to chars
        find_word = "_".split() * len(split_word)  # put ___ as many chars is the word, in that list
    elif choice == menuwords:
        return_file = file_txt(choice)
        rand_word = random.choice(return_file)  # pick random element from list
        split_word = list(rand_word)  # slit the word in to chars
        find_word = "_".split() * len(split_word)  # put ___ as many chars is the word, in that list
    elif choice == menuanimals:
        return_file = file_txt(choice)
        rand_word = random.choice(return_file)  # pick random element from list
        split_word = list(rand_word)  # slit the word in to chars
        find_word = "_".split() * len(split_word)  # put ___ as many chars is the word, in that list
    elif choice == menurand_diction:
        return_file = file_txt(choice)
        rand_word = random.choice(return_file)  # pick random element from list
        split_word = list(rand_word)  # slit the word in to chars
        find_word = "_".split() * len(split_word)  # put ___ as many chars is the word, in that list

    return split_word, find_word


def menu():
    init()
    print(Fore.CYAN + f"\nWelcome to HangMan, try to find the word!!!" + Fore.RESET)
    print(Fore.BLUE + """
Select category

1. Countries
2. Words
3. Animals
4. Random Dicrionary
X. Exit
""" + Fore.RESET)
    choice = input(Fore.CYAN + "Choose category: " + Fore.RESET).lower()
    if str(choice) != "x":
        split_word, find_word = dictionary_words(int(choice))
    elif str(choice) == "x":
        exit(0)
    else:
        print("try again your choice")

    main(split_word, find_word)


def main(split_word, find_word):
    lifes = 6
    while True:
        lifes_draw = draw_man(lifes)
        print(Fore.MAGENTA+lifes_draw+Fore.RESET)
        print("You have " + Fore.GREEN+str(lifes) + " Lifes"+Fore.RESET)
        print("\n" + " ".join(find_word))
        print(Fore.MAGENTA+"Letters that you have used: " + ",".join(letters_in_use)+Fore.RESET)
        letter = input("Choose letter: ").upper()

        if letter in letters_in_use:
            print("\nYou have used that letter, try other")
            continue

        if letter in split_word:  # if the letter exist in word
            letters_in_use.append(letter)  # add it
            for pos in range(len(split_word)):  # find which potion is that letter
                if split_word[pos] == letter:
                    find_word[pos] = letter  # add letter in to the unknown word list

            if "_" not in find_word:
                print("Well Done, You Won!!!\n" * 3)
                print(f"\nThe word it was {''.join(split_word)}")  # show the word)
                break
        else:
            letters_in_use.append(letter)  # add it
            lifes -= 1
            print("That letter does not exist into that word.\n")
            if lifes == 0:
                print(Fore.MAGENTA+draw_man(0)+Fore.RESET)
                # print("You have " + str(lifes) + " lifes")
                print(f"The word it was {Fore.GREEN+''.join(split_word)}"+Fore.RESET)  # show the word
                print(Fore.RED+"***Game Over***"+Fore.RESET)
                break
    input()


menu()
