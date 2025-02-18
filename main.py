import random as rd

ScoreP1 = 0
ScoreP2 = 0

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


# ScoreEvol
# GameEvol
# TiBreakEvol









    

