from termcolor import colored

board = list(range(1,10))
#A tuple containing the winning moves on the game board indexed by the board list numbers.
winners = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
#Smart Moves for PC
moves = ((1, 7, 3, 9), (5,), (2, 4, 6, 8))


#Making a game board
def print_board():
   """
   Every time three houses are built, if it is divisible by 3,
   it goes to the next line so that the game board becomes three
   rows of three.
   """
   line = 1
   for i in board:
      end = ' '
      if line % 3 == 0 :
         end ='\n\n'
      if i == 'X':
         print(colored(f"[{i}]","red"),end=end)
      elif i == 'O' :
         print(colored(f"[{i}]","blue"),end=end)
      else :
         print(colored(f"[{i}]","dark_grey"),end=end)
      line += 1


def has_empty_space():
    """
    If the number of moves is equal to 9, 
    it means that there is no empty house left
    """
    return board.count("x") + board.count("o") != 9

def computer_move():
    mv = -1
    #Can the computer win or not?
    for i in range(1, 10):
        if make_move(board, computer, i, True)[1]:
            mv = i
            break
    # If the user can win, stop her
    if mv == -1:
        for j in range(1, 10):
            if make_move(board, player, j, True)[1]:
                mv = j
                break
    # move
    if mv == -1:
        for tup in moves:
            for m in tup:
                if mv == -1 and can_move(board, m):
                    mv = m
                    break
    return make_move(board, computer, mv)           


def make_move(brd,ply,mve,undo=False):
   if can_move(mve,brd):
      brd[mve-1] = ply
      win = is_winner(brd,ply)
      if undo:
         brd[mve-1] = mve
      return True,win
   return False,False
   

def can_move(mve,brd):
   """
   If the number entered by the user is correct and 
   there is a number in that field, the player can move.
   """
   if mve in range(1,10) and isinstance(brd[mve-1],int) :
      return True


def is_winner(brd,ply) :
   """
   To check if the player is a winner, if the player's symbol 
   in the game is equal to the winning moves, the player is a winner.
   """
   win = True
   for tup in winners :
      win = True
      for i in tup:
         if brd[i] != ply:
            win = False
            break
      if win:
         break
   return win 

player, computer = 'X','O'
print(f"player : {player} \ncomputer : {computer}\n")

while has_empty_space():
   print(print_board())
   move = int(input('choose your move among (1:9) : '))
   """
   response to the player's move, has he won?
   Either the move is wrong or the game continues
   """
   moved , won = make_move(board,player,move)
   if not moved:
      print("try again")
      continue
   if won:
      print(colored('you won !!!','green'))
      break
   elif computer_move()[1]:
       print(colored('you lose and computer won !!!','yellow'))

print(print_board())