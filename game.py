from board import Board
from player import Player

class Game:
    def __init__(self,players,board,turn):
        self.players = []
        self.board = Board()
        self.turn = 0
        
    def play_game(self):
        p1 = Player().get_name()
        self.players.append(p1)
        p2 = Player().get_name()
        self.players.append(p2)
        Board().disp_board()
        while True:
            try:
                Player().get_choice(name)
                Board().add_piece(choice)
                Board().disp_board()
                Board().is_full()
                Board().check_winner()
                
            
                
            
            
            
    
    
    
def main():
    play_game()


        
    
if __name__== "__main__":
    main()
    