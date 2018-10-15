from board import Board

class Player:
    def __init__(self,piece):
        self.name = self.get_name()
        self.piece = piece
        
    def get_name(self):
        name = input("What is the name of your player: ")
    
    def get_choice(self, board):
        choice = input("What column would you like to place your piece: ")
        return choice
    
def main():
    E = Player()
    E.get_name()
 
if __name__== "__main__":
    main()