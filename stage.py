import numpy as np
import pygame
from piece import Piece
from deck import Deck

class Stage:
    score = 0
    def __init__(self,dim=8):
        self.dim = dim
        self.matrix = np.zeros((dim,dim))
        self.rewards = [10,20,60,120,200]
        self.deck = Deck()
    
    def play(self,piece :Piece, position:tuple):
        self.matrix[position[0]:position[0]+piece.dim[0],position[1]:position[1]+piece.dim[1]] += piece.matrix
        self.score += piece.matrix.sum()
        self.deck.remove(piece)
        self.update()
    
    def getPossiblePos(self,piece) -> list[tuple]:
        possiblePos = []
        for i in range(self.dim-piece.dim[0]+1):
            for j in range(self.dim-piece.dim[1]+1):
                newZone = self.matrix[i:i+piece.dim[0],j:j+piece.dim[1]] + piece.matrix
                if newZone.max() == 1:
                    possiblePos.append((i,j))
        return possiblePos
    
    def getPossiblePieces(self):
        possiblePieces = []
        for p in self.deck.pieces:
            if self.getPossiblePos(p) != []:
                possiblePieces.append(p)
        return possiblePieces
    
    def update(self):
        cols = []
        rows = []
        for i in range(self.dim):
            if self.matrix[i].sum() == self.dim:
                rows.append(i)
            if self.matrix[:,i].sum() == self.dim:
                cols.append(i)
        for col in cols:
            self.matrix[:,col] *= 0
        for row in rows:
            self.matrix[row] *= 0
        if len(cols)+len(rows) != 0:
            self.score += self.deck.multiplier*self.rewards[len(cols)+len(rows)-1]
            self.deck.combo = True
        
            
    def displayStage(self,screen,pos,squareSize=50,defaultColor='cadetblue2',fillColor = 'blue3'):
        mat = self.matrix
        for i in range(self.dim):
            for j in range(self.dim):
                if mat[i,j] == 1:
                    color = defaultColor
                else:
                    color = fillColor
                squarePos = pygame.Vector2(pos[0] -squareSize*self.dim/2 + i*squareSize ,pos[1] -squareSize*self.dim/2 + j*squareSize)
                pygame.draw.rect(screen,color,pygame.Rect(squarePos.x,squarePos.y,squareSize,squareSize))
                pygame.draw.rect(screen,'black',pygame.Rect(squarePos.x,squarePos.y,squareSize,squareSize),width=3)
        
        self.deck.displayDeck(screen,(screen.get_width() / 2, screen.get_height() / 2+6*squareSize))
        
        font = pygame.font.SysFont('Arial', 40)
        text_surface = font.render('Score: '+str(self.score), True, 'white')
        screen.blit(text_surface, (0,0))

    
    def __repr__(self) -> str:
        return str(self.matrix)
