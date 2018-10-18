

class Player:
    def __init__(self,piece):
        self.piece = piece
        self.name = self.get_name()
        
    def get_name(self):
        name = input("What is the name of your player: ")
        return name
    def get_choice(self,name):
        choice = input(f"{name} pick a column")
    
        return choice
    
def main():
    pass

if __name__== "__main__":
    main()