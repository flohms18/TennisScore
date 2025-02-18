import random as rd

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


    
intro()

def ScoreEvol():
    scores = ["0","15","30","40","A"]
    ScoreP1 = 0
    ScoreP2 = 0

    while True:
        PointWinner = rd.randint(0,1)
        if PointWinner == 0:
            ScoreP1 +=1
        else:
            ScoreP2 +=2

        if ScoreP1 >= 4 and ScoreP1 - ScoreP2 >= 2:
            print("P1 wins the game!")

        elif ScoreP2 >= 4 and ScoreP2 - ScoreP1 >= 2:
            print("P2 wins the game!")
        elif ScoreP1 >= 3 and ScoreP2 >= 3:
            if ScoreP1 == ScoreP2:
                print("Deuce")
            elif ScoreP1 > ScoreP1:
                print("Avantage P1")
            else:
                print("Avantage P2")
        else:
            print(f"Score P1 - {scores[ScoreP1]} Score P2 - {scores[ScoreP2]}")

        

    
ScoreEvol()

