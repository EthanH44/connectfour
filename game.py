from board import Board
from player import Player

class Game:
    def __init__(self,players,board,turn):
        self.players = []
        self.board = Board(7,6)
        self.turn = 0
        
    def play_game(self):
        
        self.players.append(Player('x'))
        self.players.append(Player('y'))
        self.board.disp_board()
        while True:
            try:
                self.players[turn].get_choice(self.players[turn].name)
                self.board.add_piece(choice,self.players[turn])
                self.board.disp_board()
                if self.board.is_full() == True:
                    raise ValueError("Board is full!")
                else:
                    
                self.board.check_winner()
            except:
                raise ValueError("Did not input correct value.")
                
                
            
                
            
            
            
    
    
    
def main():
    Game().play_game()


        
    
if __name__== "__main__":
    main()
    