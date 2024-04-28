from stage import Stage
from piece import Piece
import random as rd

stg = Stage()
 
if __name__ == "__main__":
    p = Piece()
    print(p)
    i = 0
    while True:
        if stg.getPossiblePos(p) != []:
            stg.play(p,rd.choice(stg.getPossiblePos(p)))
            i += 1
        else:
            break
    print(stg)
    print("Score = ",i)