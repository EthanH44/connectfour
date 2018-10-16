

class Board:
    


    def __init__(self,width,height):
        self.width = width
        self.height = height
        self.board = [['1']*self.width for i in range(self.height)]
        
        
        
        
    def add_piece(self,col,piece):
        for i in range(self.width):
            col-1 = piece
            
        
                                                         
        pass
        
    def empty_board(self):
        print(self.board)
    
            
    
    def disp_board(self):
        for i in range(self.width):
            for j in range (self.height):
                print(self.board[i][j], end=' ')
            print()
    
    def is_full(self):
        for i in range(self.width):
            for j in range (self.height):
                if self.board[i][j] == ' ':
                    break
        else:
            raise ValueError("Board is full. Tie!")
                    
                    
    def check_winner(self):
        pass
        
        
def main():
    b=Board(5,5)
    b.disp_board()
    b.add_piece

if __name__ == "__main__":
    main()
    
    
    
    
    
    
    
    
    
    