

class Board:
    


    def __init__(self,width,height):
        self.width = width
        self.height = height
        self.board = [['1']*self.width for i in range(self.height)]
        
        
        
        
    def add_piece(self,col,piece):
        for row in range(self.height -1,-1,-1):
            if self.board[row][col-1]== '1':
                self.board[row][col-1] = piece
                break
        else:
            raise ValueError('column full')
                
        
    def empty_board(self):
        self.board = [['1']*self.width for i in range(self.height)]
    
            
    
    def disp_board(self): # crashes when a non-square board is used
        c=[]
        for x in range(self.width):
            c.append(x+1)
        for y in range(len(c)):
            print(c[y],end =' ')
        print(' ')
            
    
        for i in range(self.width):
            for j in range (self.height):
                print(self.board[i][j], end=' ')
            print()
    
    def is_full(self): # should return True or False
        for i in range(self.width):
            for j in range (self.height):
                if self.board[i][j] == '1':
                    break
            else:
                raise ValueError("Board is full. Tie!")
                    
                    
    def check_winner(self): # method is supposed to be check_win()
        for i in range(self.height):
            for j in range(self.width-3):
                if self.board[i][j] == self.board[i][j+1]:
                    if self.board[i][j+2] == self.board[i][j+3]:
                        if self.board[i][j] != "1":
                            return True
                
                
        for i in range(self.height-3):
            for j in range(self.width):
                if self.board[i][j] == self.board[i+1][j]:
                    if self.board[i+2][j] == self.board[i+3][j]:
                        if self.board[i][j] != "1":
                            return True
        else:
            return False
        
                
        
                    
                        
            
        
def main():
    b=Board(6,7)
    
    b.disp_board()
    print(b.check_winner())

if __name__ == "__main__":
    main()
    
    
    
    
    
    
    
    
    
    