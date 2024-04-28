import random as rd

from stage import Stage
from piece import Piece

class Player:
    def __init__(self) -> None:
        pass
    
    def getNextMove(self,stage:Stage,possiblePieces:list[Piece]):
        p = rd.choice(possiblePieces)
        pos = rd.choice(stage.getPossiblePos(p))
        return p,pos