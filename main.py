from board import Board
    
while True:
    try:
        size = int(input("Enter size of game board: "))
    except ValueError:
        print("Size must be a positive integer!")
        continue
    if (size < 4):
        print("Size must be at least 4!")
    else:
        break

game_board = Board(size)
game_board.print_board()

while True:
    while True:
        try:
            column = int(input("Player 1, pick a Column: "))
        except ValueError:
            print("Invalid Entry!")
            continue
        if column > size or column < 1:
            print("Invalid entry!")
            continue
        if game_board.place_tile(column - 1, 'O'):
            break
        else:
            print("Column is full! try again!")
    game_board.print_board()
    if game_board.check_win('O'):
        print("Victory for Player 1!")
        break
    if game_board.check_full():
        print("It's a draw!")
        break

    while True:
        try:
            column = int(input("Player 2, pick a Column: "))
        except ValueError:
            print("Invalid entry!")
            continue
        if column > size or column < 1:
            print("Invalid entry!")
            continue
        if game_board.place_tile(column - 1, 'X'):
            break
        else:
            print("Column is full! try again!")
    game_board.print_board()
    if game_board.check_win('X'):
        print("Victory for Player 2!")
        break
    if game_board.check_full():
        print("It's a draw!")
        break