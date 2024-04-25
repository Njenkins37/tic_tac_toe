def create_board(game_list):
    top_row = f'   {game_list[0]}  |   {game_list[1]}   |  {game_list[2]}  \n'
    filler = '------|-------|-----\n'
    middle_row = f'   {game_list[3]}  |   {game_list[4]}   |  {game_list[5]}  \n'
    bottom_row = f'   {game_list[6]}  |   {game_list[7]}   |  {game_list[8]}  '
    board = top_row + filler + middle_row + filler + bottom_row
    return board


def check_winner(game_list):
    if ((game_list[0] == 'X' and game_list[1] == 'X' and game_list[2] == 'X') or
            (game_list[3] == 'X' and game_list[4] == 'X' and game_list[5] == 'X') or
            (game_list[6] == 'X' and game_list[7] == 'X' and game_list[8] == 'X') or
            (game_list[0] == 'X' and game_list[3] == 'X' and game_list[6] == 'X') or
            (game_list[1] == 'X' and game_list[4] == 'X' and game_list[7] == 'X') or
            (game_list[2] == 'X' and game_list[5] == 'X' and game_list[8] == 'X') or
            (game_list[0] == 'X' and game_list[4] == 'X' and game_list[8] == 'X') or
            (game_list[2] == 'X' and game_list[4] == 'X' and game_list[6] == 'X')):
        print('Player 1 won!')
        return False
    elif ((game_list[0] == 'O' and game_list[1] == 'O' and game_list[2] == 'O') or
            (game_list[3] == 'O' and game_list[4] == 'O' and game_list[5] == 'O') or
            (game_list[6] == 'O' and game_list[7] == 'O' and game_list[8] == 'O') or
            (game_list[0] == 'O' and game_list[3] == 'O' and game_list[6] == 'O') or
            (game_list[1] == 'O' and game_list[4] == 'O' and game_list[7] == 'O') or
            (game_list[2] == 'O' and game_list[5] == 'O' and game_list[8] == 'O') or
            (game_list[0] == 'O' and game_list[4] == 'O' and game_list[8] == 'O') or
            (game_list[2] == 'O' and game_list[4] == 'O' and game_list[6] == 'O')):
        print('Player 2 won!')
        return False
    return True


game_is_on = True
game_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
turn = 1

while game_is_on:
    print(create_board(game_list))

    if turn % 2 == 1:
        answer = input(f"It is Player {turn % 2}'s turn\n")
    else:
        answer = input(f"It is Player {turn % 2 + 2}'s turn\n")

    for index, item in enumerate(game_list):
        if item == str(answer) and turn % 2 == 1:
            game_list[index] = 'X'
        elif item == str(answer) and turn % 2 == 0:
            game_list[index] = 'O'
    game_is_on = check_winner(game_list)
    turn += 1
    if turn == 10:
        game_is_on = False
        print("Cat's Game")
