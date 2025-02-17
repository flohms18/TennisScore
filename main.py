import random as rd

def intro():
   Serve = 0
   print("Hello ! Welcome to Tennis")
   ChoiceServe = rd.randint(1,2)
   if ChoiceServe == 1:
      
    SelectP1 = input("P1, Serve or Receive ? S/R: ")
      
    if SelectP1 == "R":
        "Fine, you will receive!"
        Serve == 1
        print("P2 to Serve! ")
    else:
        Serve == 2
        print("P1 to Serve! ")

   else:
      SelectP1 = input("P2, Serve or Receive ? S/R: ")
      if SelectP1 == "R":
         "Fine, you will receive!"
         Serve == 1
         print("P1 to Serve! ")
      else:
         Serve == 2
         print("P2 to Serve! ")

intro()

def Game():
   ScoreP1 = 0
   ScoreP2 = 0
   while ScoreP1 != 4 or ScoreP2 != 4: 
        Point = rd.randint(1,2)
        if Point == 1: 
            ScoreP1 += 1
        else :
           ScoreP2 += 1
        
        if ScoreP1 == 4 : 
            print("P1 wins the game!")
        elif ScoreP2 == 4:
            print("P2 wins the game!")
      


   