class Player:
    def __init__(self, name, token):
        self.name = name
        self.token = token
# The Game class has the following properties:
# board = your representation of the board
class Game:
    def __init__(self,):
        self.win_conditions = ((0,1,2),(3,4,5),(6,7,8),(0,4,8),(2,4,6),(0,3,6),(1,4,7),(2,5,8))
        self.board =  [0, 1, 2, 3, 4, 5, 6, 7, 8]
    # __repr__() Returns a pretty string representation of the game board
    def __repr__(self):
        print('')
        print(self.board[0], self.board[1], self.board[2])
        print(self.board[3], self.board[4], self.board[5])
        print(self.board[6], self.board[7], self.board[8])
        print('')
        # 0 1 2
        # 3 4 5
        # 6 7 8
    # move(x, y, player) Place a player's token character string at a given coordinate (top-left is 0, 0), x is horizontal position, y is vertical position.
    def move(self, player):
        player_pick = int(input(f'{player.name}, Make your move: '))
        
        if self.board[player_pick] != 'X' or self.board[player_pick] != 'O':
            self.board[player_pick] = player.token
            return player_pick
        else:
            print('Spot is taken, Try another!')
            self.move(player)
    
    # calc_winner() What token character string has won or None if no one has.
    def calc_winner(self,):
    #    self.win_conditions = ((0,1,2),(3,4,5),(6,7,8),(0,4,8),(2,4,6),(0,3,6),(1,4,7),(2,5,8))
        for a in self.win_conditions:
            if self.board[a[0]] == self.board[a[1]] == self.board[a[2]] == "X":
                print("PLAYER X WINS")
                return True
            if self.board[a[0]] == self.board[a[1]] == self.board[a[2]] == "O":
                print("PLAYER O WINS")
                return True
    
    # is_full() Returns true if the game board is full.
    def is_full(self):
        for i in self.board:
            if i in [0,1,2,3,4,5,6,7,8]:
                return False
        return True
    # is_game_over() Returns true if the game board is full or a player has won.
    def is_game_over(self):
        pass
def main():
    player1 = Player('Bob', "X")
    player2 = Player('Jill', 'O')
    board = Game()
  
    while True:
        board.__repr__()
        board.move(player1)
        if board.calc_winner():
            board.__repr__()
            break
        if board.is_full():
            print("board is full tie-game")
            break
        board.__repr__()
        board.move(player2)
        if board.calc_winner():
            board.__repr__()
            break
        if board.is_full():
            print("board is full tie-game")
            break
        board.__repr__()
main()
