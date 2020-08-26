# Game
from random import shuffle


def shuffle_list(my_list):
    shuffle(my_list)
    return my_list


def prepare_game(char):
    my_list = [char, ' ', ' ']
    return my_list


def check_luck(place, my_list, char):
    if my_list[place] == char:
        return 'You Won the Game...!!'
    else:
        return 'You lost the game better luck next time.!'


def player_guess():
    place = ''
    while place not in ['0', '1', '2']:
        place = input('Enter the guess for place (0/1/2) : ')
    return int(place)


def choose_char():
    char = ''
    while char not in ['o', '*', '$', '#', '@']:
        char = input('Enter the object you want to play with o/*/$/#/@ : ')
    return char


def main():
    print('\t\tHi Welcome to the Game..!!!')
    char = choose_char()
    my_list = prepare_game(char)
    my_list = shuffle_list(my_list)
    print('The game is set with the object you choose')
    choice = input('Do you wish to play game further (yes/no) : ')
    place = player_guess()
    print(check_luck(place, my_list, char))


flag = True
while flag:
    main()
    x = input('Do you want to play again (yes/no) : ')
    if x == 'yes':
        flag = True
    else:
        flag = False
        print('Good bye...!!')
