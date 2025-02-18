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
    
    SetP1 = 0
    SetP2 = 0
    
    scores = ["0","15","30","40","A"]

    while SetP1 < 3 and SetP2 < 3:
        GameP1 = 0
        GameP2 = 0

        while True: 
            ScoreP1 = 0
            ScoreP2 = 0
        
            while True:
                PointWinner = rd.randint(0,1)
                if PointWinner == 0:
                    ScoreP1 += 1
                else:
                    ScoreP2 += 1

                if ScoreP1 >= 4 and ScoreP1 - ScoreP2 >= 2:
                    print("P1 wins the game")
                    GameP1 += 1
                    break
                elif ScoreP2 >= 4 and ScoreP2 - ScoreP1 >= 2:
                    print("P2 wins the game")
                    GameP2 += 1
                    break
                elif ScoreP1 >= 3 and ScoreP2 >= 3:
                    if ScoreP1 == ScoreP2:
                        print("Deuce")
                    elif ScoreP1 > ScoreP2:
                        print("Ad P1")
                    else:
                        print("Ad P2")
                else:
                    print(f"{scores[ScoreP1]} - {scores[ScoreP2]}")
            print(f"{GameP1} - {GameP2}\n------- ")

            if GameP1 >= 6 and GameP1 - GameP2 >= 2:
                print("P1 wins the set")
                SetP1 += 1
                break
            elif GameP2 >= 6 and GameP2 - GameP1 >= 2:
                print("P2 wins the set")
                SetP2 += 1
                break
            elif GameP1 == 5 and GameP2 == 5:
                print("Set extends to 7 games max!")
            elif GameP1 == 7 or GameP2 == 7:
                if GameP1 - GameP2 >= 2:
                    print("Player 1 wins the set!")
                    break
                elif GameP2 - GameP1 >= 2:
                    print("Player 2 wins the set!")
                    break
            elif GameP1 == 6 and GameP2 == 6:
                print("Tie-Break !!")
                break
            
        print(f"{SetP1} - {SetP2}\n------- ")
    
    if SetP1 == 3:
        print("Player 1 wins the match!")
    else:
        print("Player 2 wins the match!")
            

    
    


ScoreEvol()









    

