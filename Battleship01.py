 import random

board = []

for x in range(0,5):
  board.append(["O"] * 5)

def print_board(board):
  for row in board:
    print " ".join(row)

print_board(board)

def random_row(board):
  return random.randint(0,len(board)-1)

def random_col(board):
    return random.randint(0,len(board[0])-1)

ship_row = random_row(board)
ship_col = random_col(board)
guess_row = input("Guess Row:")
guess_col = input("Guess Col:")

if guess_row == ship_row and guess_col == ship_col:
    print "Congratulations! You sank my battleship!"

elif guess_row < 0 or guess_row > 5 or guess_col < 0 or guess_col > 5:
    print "Oops, that's not even in the ocean."

else:
    board[guess_col][guess_row] = "X"
    print "You missed my battleship!"
    print_board(board)
