"""
Tic Tac Toe Player
"""

import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    # to find the number of Xs and Os in the board
    countX = 0
    countO = 0
    countE = 0
    for i in range(0, len(board)):
        for j in range(0, len(board[i])):
            if board[i][j] == X:
                countX += 1
            elif board[i][j] == O:
                countO += 1
            else:
                countE += 1

    if countE == 9 or countO == countX:
        return X
    elif countX > countO:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions = []
    for i in range(0, len(board)):
        for j in range(0, len(board[i])):
            if board[i][j] == EMPTY:
                possible_actions.append((i, j))

    return possible_actions


def result(board, action):
    """
    Returns the board that res from making move (i, j) on the board.
    """
    i = int(action[0])
    j = int(action[1])
    if board[i][j] != EMPTY:
        raise Exception("Not a valid action!")

    resBoard = copy.deepcopy(board)
    resBoard[i][j] = player(board)
    return resBoard


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if ((board[0][0] != EMPTY) and (board[0][0] == board[0][1]) and (board[0][1] == board[0][2])) \
            or ((board[0][0] != EMPTY) and (board[0][0] == board[1][0]) and (board[1][0] == board[2][0])) \
            or ((board[0][0] != EMPTY) and (board[0][0] == board[1][1]) and (board[1][1] == board[2][2])):
        return board[0][0]
    elif ((board[1][0] != EMPTY) and (board[1][0] == board[1][1]) and (board[1][1] == board[1][2])) \
            or ((board[0][1] != EMPTY) and (board[0][1] == board[1][1]) and (board[1][1] == board[2][1])) \
            or ((board[0][2] != EMPTY) and (board[0][2] == board[1][1]) and (board[1][1] == board[2][0])):
        return board[1][1]
    elif ((board[2][0] != EMPTY) and (board[2][0] == board[2][1]) and (board[2][1] == board[2][2])) \
            or ((board[0][2] != EMPTY) and (board[0][2] == board[1][2]) and (board[1][2] == board[2][2])):
        return board[2][2]
    else:
        return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None:
        return True
    elif any(EMPTY in sublist for sublist in board) == False:
        return True
    else:
        return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    def maximize(board):
        if terminal(board):
            return utility(board)
        z = -99999
        for action in actions(board):
            z = max(z, minimize(result(board, action)))
        return z

    def minimize(board):
        if terminal(board):
            return utility(board)
        z = 99999
        for action in actions(board):
            z = min(z, maximize(result(board, action)))
        return z

    if player(board) == X:
        nextPlayer = O
    else:
        nextPlayer = X

    res = []
    possible_actions = []
    solution = ()
    if nextPlayer == X:
        for action in actions(board):
            v = minimize(result(board, action))
            res.append(v)
            possible_actions.append(actions)

        solution = possible_actions[min(res)]
    if nextPlayer == O:
        for action in actions(board):
            v = maximize(result(board, action))
            res.append(v)
            possible_actions.append(action)

        solution = possible_actions[max(res)]

    print(solution)
    return solution
