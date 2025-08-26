import copy

class tictactoe:
    def __init__(self) -> None:
        self.board = [[0 for _ in range(3)] for _ in range(3)]
        self.winner = None
        self.turn = 1

    
    def make_move(self, row, col):
        if self.board[row][col] == 0:
            self.board[row][col] = self.turn
            if self.turn == 1:
                self.turn = -1
            else:
                self.turn = 1
        else:
            pass
    def check_winner(self):
        for row in range(3):
            temp = 0
            for col in range(3):
                temp += self.board[row][col]
            if temp == 3 or temp == -3:
                return temp//3
            
        for col in range(3):
            temp = 0
            for row in range(3):
                temp += self.board[row][col]
                
            if temp == 3 or temp == -3:
                return temp//3

        temp = self.board[0][0] + self.board[1][1] + self.board[2][2]
        if temp == 3 or temp == -3:
                return temp//3
        temp = self.board[2][0] + self.board[1][1] + self.board[0][2]
        if temp == 3 or temp == -3:
                return temp//3

        for row in range(3):
            for col in range(3):
                if self.board[row][col] == 0:
                    return None
        return "draw"
    
    def possible_moves(self):
        final = []
        for row in range(3):
            for col in range(3):
                if self.board[row][col] == 0:
                    final.append((row,col))
        return final
        
    
    def show_board(self):
        for row in self.board:
            print(row)

def minmax(board: tictactoe, player, depth):
    assert board.turn == player
    #base case: the game ends
    state = board.check_winner()
    if state == 1:
        return (2, None)
    elif state == -1:
        return (-2, None)
    elif state == "draw":
        return (0, None)
    
    #if the game is undecided
    #if curr player is 1, we maximize
    if player == 1:
        #the best score is supposed to be -infinity at start
        #the goal here is to minimize the score as the opponent,
        #so we get their optimal move
        best_score = -100
        best_move = None
        #test out player1's moves
        for move in board.possible_moves():
            new = copy.deepcopy(board)
            #play the given move on a copy of the board
            new.make_move(move[0],move[1])
            #recursively call minmax to get the score for the current state
            score = minmax(new, -player, depth+1)[0]
            #if the current board state score is better than the previous, update
            if score > best_score:
                best_score = score
                best_move = move
        return (best_score, best_move)
    else: #same thing but minimizing
        best_score = 100
        best_move = None
        for move in board.possible_moves():
            new = copy.deepcopy(board)
            new.make_move(move[0],move[1])
            score = minmax(new, -player, depth+1)[0]
            # print(move, score, depth)
            if score < best_score:
                best_score = score
                best_move = move
        return (best_score, best_move)


# board = tictactoe()
# board.make_move(1,1)
# board.make_move(0,0)
# board.make_move(0,1)
# board.show_board()
# print(board.check_winner())
# print(minmax(board, -1, 0))

         
# board = tictactoe()
# board.make_move(1,1)
# board.make_move(0,0)
# board.make_move(0,1)
# board.make_move(2,1)
# board.make_move(0,2)
# board.make_move(1,0)
# board.make_move(2,0)
# board.show_board()
# print(board.check_winner())
            
# board = tictactoe()
# board.make_move(1,1)
# board.make_move(0,0)
# board.make_move(0,1)
# print(minmax(board, -1))
# board.show_board()
# print(board.check_winner())
    
# board = tictactoe()
# board.make_move(1,1)
# board.make_move(0,0)
# board.make_move(0,1)
# board.make_move(2,1)
# board.make_move(0,2)
# board.make_move(2,0)
# board.make_move(1,1)
# board.make_move(1,0)
# board.make_move(2,2)
# print(board.check_winner())


def play():
    board = tictactoe()
    turn = 1
    while board.check_winner() == None:
        print("\n")
        board.show_board()
        print("\n")
        if turn == 1:
            move = input("enter a move in the format row,col: ")
            move = move.strip().split(",")
            # print(move)
            board.make_move(int(move[0]), int(move[1]))
        else:
            move = minmax(board, turn, 0)[1]
            board.make_move(move[0], move[1])
        
        turn *= -1
    board.show_board()

play()