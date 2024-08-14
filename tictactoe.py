import os
import time
import random


board = ["", " ", " ", " ", " ", " ", " ", " ", " ", " "]


def print_header():
    print("""
  ____   ____  
 / ___| |  _ \ 
| |  _  | | | |
| || | |  | | |
 \| |/ | |  | |
   -----------1
                
    """)


def print_board():
    print("   |   |   ")
    print(f" {board[1]} | {board[2]} | {board[3]} ")
    print("   |   |   ")
    print("---|---|---")
    print("   |   |   ")
    print(f" {board[4]} | {board[5]} | {board[6]} ")
    print("   |   |   ")
    print("---|---|---")
    print("   |   |   ")
    print(f" {board[7]} | {board[8]} | {board[9]} ")
    print("   |   |   ")


def is_winner(player):
    win_conditions = [
        (1, 2, 3), (4, 5, 6), (7, 8, 9),  
        (1, 4, 7), (2, 5, 8), (3, 6, 9),  
        (1, 5, 9), (3, 5, 7)              
    ]
    return any(board[a] == board[b] == board[c] == player for a, b, c in win_conditions)


def is_board_full():
    return " " not in board[1:]


def get_computer_move():
 
    if board[5] == " ":
        return 5

    empty_spaces = [i for i in range(1, 10) if board[i] == " "]
    return random.choice(empty_spaces) if empty_spaces else 5


while True:
    os.system("cls" if os.name == "nt" else "clear")
    print_header()
    print_board()

    
    try:
        player_move = int(input("Please choose an empty space for X: "))
        if 1 <= player_move <= 9 and board[player_move] == " ":
            board[player_move] = "X"
        else:
            print("Invalid move or space is occupied. Try again!")
            time.sleep(1)
            continue
    except ValueError:
        print("Choose an empty spcace:")
        time.sleep(1)
        continue

    if is_winner("X"):
        os.system("cls" if os.name == "nt" else "clear")
        print_header()
        print_board()
        print("YOU WIN! Congratulations!")
        break

    if is_board_full():
        os.system("cls" if os.name == "nt" else "clear")
        print_header()
        print_board()
        print("It's a tie!")
        break

    
    print("Player O is making a move...")
    time.sleep(1)
    computer_move = get_computer_move()
    board[computer_move] = "O"

    if is_winner("O"):
        os.system("cls" if os.name == "nt" else "clear")
        print_header()
        print_board()
        print("O wins! Better luck next time.")
        break

    if is_board_full():
        os.system("cls" if os.name == "nt" else "clear")
        print_header()
        print_board()
        print("It's a tie!")
        break
        