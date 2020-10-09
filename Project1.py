#Game between computer and User
import random as rnd #import random library

msg = "Welcome to the ROCK PAPER SCISSORS Game"     #welcome msg to the game
print("\n", "/" * (len(msg)+3),  msg, "/" * (len(msg)+3) )
rule = "Win rule: **The ROCK smashes the SCISSORS**  **SCISSORS cuts PAPER**  **PAPER wraps ROCK**"
print("_" * (len(rule)+3), " \n"*2,rule, "\n", "_" * (len(rule)+2), "\n")

def choice(c):
  if c == 1:    
    return "Rock"   
  elif c == 2:
    return "Paper"
  else:
    return "Scissors"

g = int(input("How many Round of games should be played?: ")) #User input for number of games to play
Draws = 0  #initiate Draws, COmputer Wins, User Wins to zero
ComputerWins = 0
UserWins = 0

for i in range(0,g):  #run each game round untill total number of games played
  r = rnd.randint(1,3) # computer selects a number among 1 ,2 , 3
  CompChoice = choice(r)  #Assigns computer choice based on randon number generated
  print("\nRound", i+1, end = ' ')    #prints round of the game
  UserChoice = int(input(" -> Enter 1 for rock, 2 for paper, 3 for scissors: ")) #Ask for user input
  
  if UserChoice in range(1,4):  #checks userchoice and assigns string from choice function
    uc = choice(UserChoice) 
    print("Computer Choice:", CompChoice, ", User Choice:", uc)   #prints computer choice and users choice
  else:
    print("\nBad input: Enter only 1 2 or 3. Your input:", UserChoice, '\n')
    quit()    #quits game if user gives bad input

  if UserChoice == r: #when same choice is choosed by Computer and user
    print("Game DRAW") #game draws
    Draws = Draws + 1   #increment draws by 1  

  elif (UserChoice == 2 and r == 1) or (UserChoice == 3 and r==2) or (UserChoice == 1 and r==3):
    if (UserChoice == 2 and r == 1): #assigns wins based on win rules
      print("** PAPER wraps ROCK ** YOU WON ")
    elif  UserChoice == 3 and r == 2:
      print("** SCISSORS cuts PAPER ** YOU WON ")
    else:
      print("** The ROCK smashes the SCISSORS ** YOU WON ")

    UserWins = UserWins +1 #increments user wins by 1
  
  #elif (UserChoice ==1 and r == 2) or (UserChoice == 2 and r==3) or (UserChoice ==3 and r == 1):  

  else:
    if (UserChoice == 1 and r == 2): #assigns wins based on win rules
      print("** PAPER wraps ROCK ** COMPUTER WON ")
    elif  UserChoice == 2 and r == 3:
      print("** SCISSORS cuts PAPER ** COMPUTER WON ")
    else:
      print("** The ROCK smashes the SCISSORS ** COMPUTER WON ")
    
    ComputerWins = ComputerWins +1 #increments Computer wins by 1
  #end of game or for loop

print("\nComputer Wins: ", ComputerWins)  #prints Computer wins
print("User Wins: ", UserWins)   #prints User wins
print("Draws: ", Draws)   #prints Draws

print("\n", "/" * (len(msg)+3), "End of the GAME", "/" * (len(msg)+3), "\n"  )
