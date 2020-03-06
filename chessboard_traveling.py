"""Count the number of ways to travel from a position to another on a 8x8 chess board

Given a function `ChessboardTraveling(str)` where `str` will be a string consisting of the location 
of a space on a standard 8x8 chess board with no pieces on the board along with another space on the chess board.
The structure of `str` will be the following:
  - `(x y)(a b)` where `(x y)` represents the position you are currently on with `x` and `y` ranging from 1 to 8
  - `(a b)` represents some other space on the chess board with `a` and `b` also ranging from 1 to 8 where `a` > `x` and `b` > `y`. 
Your program should determine how many ways there are of traveling from `(x y)` on the board to `(a b)` moving only up and to the right. 
For example: if `str` is `(1 1)(2 2)` then your program should output `2` because there are only two possible ways to travel from space 
`(1 1)` on a chessboard to space `(2 2)` while making only moves up and to the right. 
"""


def move_right(start):
    x = start[0]
    y = start[1]
    if x < 8:
        return x + 1, y
    return None


def move_up(start):
    x = start[0]
    y = start[1]
    if y < 8:
        return x, y + 1
    return None


def count_paths(start, destination):
    if start == destination:
        return 1
    up_paths = count_paths(move_up(start), destination) if move_up(start) else 0
    right_paths = count_paths(move_right(start), destination) if move_right(start) else 0
    return up_paths + right_paths


def chessboard_traveling(str):
    start = (int(str[1]), int(str[3]))
    destination = (int(str[6]), int(str[8]))
    return count_paths(start, destination)


# keep this function call here
print(chessboard_traveling("(1 1)(2 2)"))
