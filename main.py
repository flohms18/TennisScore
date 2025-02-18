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

def score():
    ScoreP1 = 0
    ScoreP2 = 0
    PointWinner = rd.randint(0,1)
    if PointWinner == 0:
        print("P1 wins the point")
        ScoreP1 += 1
        
    else:
        print("P2 wins the point")
        ScoreP2 += 1
    print(f"{ScoreP1}-{ScoreP2}")
       

score()


