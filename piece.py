import random
import numpy as np
import pygame

pieces = [np.array([[0,1,1],[1,1,0]]),
          np.array([[1,1],[1,1]]),
          np.array([[1,1],[0,1],[0,1]]),
          np.array([[0,1,0],[1,1,1]]),
          np.array([[1],[1],[1],[1]])]

class Piece:
    def __init__(self,color):
        self.color = color
        self.matrix = np.rot90(pieces[random.randint(0,len(pieces)-1)],k=random.randint(0,3))
        self.dim = self.matrix.shape
    
    def __repr__(self) -> str:
        return str(self.matrix)
    
    def displayPiece(self,screen, pos,squareSize = 50):
        mat = self.matrix
        for i in range(self.dim[0]):
            for j in range(self.dim[1]):
                if mat[i,j] == 1:
                    squarePos = pygame.Vector2(pos[0] -squareSize*self.dim[0]/2 + i*squareSize ,pos[1] -squareSize*self.dim[1]/2 + j*squareSize)
                    pygame.draw.rect(screen,self.color,pygame.Rect(squarePos.x,squarePos.y,squareSize,squareSize))
                    pygame.draw.rect(screen,'black',pygame.Rect(squarePos.x,squarePos.y,squareSize,squareSize),width=3)
    
