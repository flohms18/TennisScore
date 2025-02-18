import random as rd
import keyboard

ScoreP1 = 0
ScoreP2 = 0
GameP1 = 0
GameP2 = 0

def intro():
    Serve = rd.randint(0,1)
    if Serve == 0:
        Choice = input("P1 won ! Servce or Receive? S/R ")
        if Choice == "R":
            print("P2 to Serve")
        else:
            print("P1 to Serve")

    else:
        Choice = input("P2 won ! Servce or Receive? S/R ")
        if Choice == "R":
            print("P1 to Serve")
        else:
            print("P2 to Serve")
    print("Picture done")
    print("Warm-up completed")
    print("The match is about to start...")


    
intro()

def ScoreEvol():
    PointWinner = rd.randint(1,2)
    scores = ["0","15","30","40","A"]
    if keyboard.is_pressed("space"):
        if PointWinner == 1:
            ScoreP1 += 1
        else:
            ScoreP2 += 1
    if ScoreP1 >= 4 and ScoreP1 - ScoreP2 >= 2:
        print("P1 wins the game")
        GameP1 += 1
    elif ScoreP2 >= 4 and ScoreP2 - ScoreP1 >= 2:
        print("P2 wins the game")
        GameP2 += 1
    elif ScoreP1 >= 3 and ScoreP2 >= 3:
        if ScoreP1 == ScoreP2:
            print("Deuce")
        elif ScoreP1 > ScoreP2:
            print("Ad P1")
        else:
            print("Ad P2")



def GameEvol():
    if GameP1 == 6 and GameP1 - GameP2 >= 2:
        print("P1 wins the set ")
    elif GameP2 == 6 and GameP2 - GameP1 >= 2:
        
    


        




# ScoreEvol
# GameEvol
# TiBreakEvol









    

