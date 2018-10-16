

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
    
            
    
    def disp_board(self):
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
    
    def is_full(self):
        for i in range(self.width):
            for j in range (self.height):
                if self.board[i][j] == '1':
                    break
            else:
                raise ValueError("Board is full. Tie!")
                    
                    
    def check_winner(self):
        pass
        
        
def main():
    b=Board(5,5)
    b.add_piece(2,'*')
    b.disp_board()
    b.is_full()
    b.disp_board()

if __name__ == "__main__":
    main()
    
    
    
    
    
    
    
    
    
    