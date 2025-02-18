import random as rd
import keyboard



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

    
    
    PointWinner = rd.randint(0,1)
    print(PointWinner)
    ScoreP1 = 0
    ScoreP2 = 0
    GameP1 = 0
    GameP2 = 0
    scores = ["0","15","30","40","A"]

    
    
    if PointWinner == 0:
        ScoreP1 += 1
        print("I lose!")
    else:
        ScoreP2 += 1
        print("I won!")

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
    else:
            print(f"{scores[ScoreP1]} - {scores[ScoreP2]}")

ScoreEvol()



    
    


        




# ScoreEvol
# GameEvol
# TiBreakEvol
# SetEvol
# Serve var to display in the right order 









    

