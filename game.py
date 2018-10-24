from board import Board
from player import Player

class Game:
    def __init__(self,players,board,turn):
        self.players = []
        self.board = Board(6,7)
        self.turn = 0
        
    def play_game(self):
        print("Welcome to Connect 4!")
        print("Get four of your pieces in a row to win!")
        
        self.players.append(Player('x'))
        self.players.append(Player('y'))
        self.board.disp_board()
        while True:
            try:   # while
                self.players[turn].get_choice(self.players[turn].name) # get_choice returns a value
                self.board.add_piece(choice,self.players[turn])
                self.board.disp_board()
                if self.board.is_full() == True:
                    raise ValueError("Board is full!")
                if self.board.is_full() == False: # unnecessary
                    continue # breaks your game
                if self.board.check_winner() == True:
                    print(f"{self.players[turn].name} has won the game!")
                    # game keeps going after winner is found
                turn = (turn + 1) % 2
                
                
            except:
                if self.board.is_full() == True:  
                    raise ValueError("Board is full!")  # ? 
                    
                
            
                
                    
                
                
                
            
                
            
            
            
    
    
    
def main():
    game = Game()
    game.Game()

        
    
if __name__== "__main__":
    main()
    