import numpy as np 
from collections import Counter

class TicTacToe():

    def main(self):
        board = self.get_board()
        while True:
            count = 0
            player = input('X or O: ').upper()
            row = input('Which row (0,1,2): ')
            element = input('Which element in the row (0,1,2): ')
            if player == 'X' or player == 'O':
                if row in ['0','1','2'] and element in ['0','1','2']:
                    row = int(row)
                    element = int(element)
                    if board[row][element] == 'X' or board[row][element] == 'O':
                        print('Place somewhere else')
                    else: 
                        board[row][element] = player
                else: 
                    print('Please choose a row and column between 0-2')
            else:
                print('Choose X or O (can be undercase)')
            print(board)

            for (i,j) in enumerate(board[:][:]):
                if '*' not in j:
                    count = count + 1
                    # horizontal (can change 3 to be length of rows)
                    if 3 in Counter(j).values(): 
                        print('Player %s Wins!'%player)
                        return True
                if i == 0 or count == 3:
                    if player in board[0] and player in board[1] and player in board[2]:
                        # indices of where each row contains the player
                        p1 = np.where(board[0] == player)[0]
                        p2 = np.where(board[1] == player)[0]
                        p3 = np.where(board[2] == player)[0]
                        # vertical
                        if p1 in p2 and p1 in p3 and p2 in p3:
                            print('Player %s Wins!'%player)
                            return True
                        # left to right diagonal
                        if 0 in p1 and 1 in p2 and 2 in p3:
                            print('Player %s Wins!'%player)
                            return True
                        # right to left diagonal
                        if 2 in p1 and 1 in p2 and 0 in p3: 
                            print('Player %s Wins!'%player)
                            return True
                    if count == 3:
                        print("Cat's Game. No Winner")
                        return True

    def get_board(self):
        board_list = ['*']*9
        board = np.array(board_list).reshape(3,3)
        return board

if __name__ == "__main__":
    TicTacToe().main()
