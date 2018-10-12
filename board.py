

class Board:
    


    def __init__(self,width,height):
        self.width = width
        self.height = height
        self.board = [[' ']*self.width for i in range(self.height)]
        
        
        
        
    def add_piece(self,column,piece):
        pass
        
        
    def empty_board(self):
        print(self.board)
    
            
    
    def disp_board(self):
        for i in range(self.width):
            for j in range (self.height):
                print(tdl[i][j], end=' ')
            print()
    
    def is_full(self):
        pass
        
        
def main():
    b=Board(5,5)
    b.disp_board()

if __name__ == "__main__":
    main()
    
    
    
    
    
    
    
    
    
    