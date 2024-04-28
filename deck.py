from piece import *

class Deck:
    def __init__(self,numberOfPieces=3,colors=['brown1','chocolate1','darkgoldenrod1','deeppink2']):
        self.numberOfPieces = numberOfPieces
        self.colors = colors
        self.initializeDeck()
    
    def displayDeck(self,screen,pos,squareSize=50):
        space = screen.get_width()/(self.numberOfPieces+1)
        for i in range(1,len(self.pieces)+1):
            self.pieces[i-1].displayPiece(screen,(i*space,pos[1]))
    
    def initializeDeck(self):
        self.pieces = []
        for i in range(self.numberOfPieces):
            color = random.choice(self.colors)
            p = Piece(color)
            self.pieces.append(p)
    
    def remove(self,piece:Piece):
        self.pieces.remove(piece)
        if len(self.pieces) == 0:
            self.initializeDeck()
        
    def __repr__(self) -> str:
        return "\n\n".join([str(p) for p in self.pieces])
    
if __name__ =="__main__":
    d = Deck()
    print(d)