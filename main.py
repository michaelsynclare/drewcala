
# Drewcala ###############################################

#intro
intro =("""
Welcome to Mandrewcala, a Mandrewish version of the classic Arabic game Mancala.

Clear your pits of their stones and score by dropping the last stone in an empty pit across from a full one or into your own goal to your right.
Move counter-clockwise. Scores earn another turn. Play until a row is empty. Leftover stones go to the player on that side. Higher score wins.

Mandrew awaits your challenge >:)
""")


#MANDREW ART (that little r keeps everything "as-is")
manDrewScoreArt =(r""" 
  __    __     __     _    _    ___     ___     ___ __            __
 /  \__/  \   /  \   / \  / \  | _ \   / _ \   /___\\ \          / /
|  /\__/\  | | __ | |   \ \  | || \ \  || \ | ||____ \ \        / /
|  \    /  | ||__|| |  |\\ \ | ||  | | ||_//  | ___/  \ \  /\  / /
|   |  |   | | __ | |  | \\_|| ||  | | | _ \  ||       \ \/  \/ /
|   |  |   | ||  || |  |  \  | ||_/ /  || \ \ ||____    \      /
 \_/    \_/  ||  ||  \/    \/  |___/   \/  \_\ \___/     \_/\_/  

__            __ ____    _    _     ___        _______
\ \          / //_  _\  / \  / \   / __\      /       \         ||
 \ \        / /   ||   |   \ \  |  \ \       / /_\ /_\ \        ||
  \ \  /\  / /    ||   |  |\\ \ |   \ \     |  _     _  |       ||
   \ \/  \/ /     ||   |  | \\_||    \ \    |  \\___//  |     /\||/\/\
    \      /    __||__ |  |  \  | /\_/ /     \  \|||/  /     |        |/\
     \_/\_/     \____/  \/    \/  \___/       \_______/      |_       __/
                                                               |     |

 """)




# border
b = "-" * 50

# starting amounts of stones within the indexes
Gs = 4  #0 
Hs = 4  #1
Is = 4  #2
Js = 4  #3
Ks = 4  #4
Ls = 4  #5

Fs = 4  #6
Es = 4  #7
Ds = 4  #8
Cs = 4  #9
Bs = 4  #10
As = 4  #11


#overwritten indexes
GsX = 99
HsX = 99
IsX = 99
JsX = 99
KsX = 99
LsX = 99

FsX = 99
EsX = 99
DsX = 99
CsX = 99
BsX = 99 
AsX = 99

# did i ever use these?
LPsX = 99 
RPsX = 99


# the scoring pits (indexes)
LPs = 0
RPs = 0



# stone values are carried inside this list of individial vars
global stonesPerPit
stonesPerPit = [Gs,Hs,Is,Js,Ks,Ls,RPs,Fs,Es,Ds,Cs,Bs,As,LPs,GsX,HsX,IsX,JsX,KsX,LsX,LPsX,FsX,EsX,DsX,CsX,BsX,AsX,RPsX] 

# using Python's built-in random library for when the bot can't apply any specific move logic
import random

# defining vars with empties and default values to avoid errors
playerTurnInput = " "
moveInputStones  = " "
chosenIndex = " "
startingIndex = " "
actualLastIndex = 1000
endingIndex = " "
botChoice = " "
allMovesSoFar = " "
stolenIndexAcross = " "
playerTurnRightNow = True #this default value makes player go first
addOneOrZero = 0
rightScoreOLD = 100
leftScoreOLD = 100 
doubleDigitSpacer = "x"
botMessages = [
"MANDREW SCORED! FEEL THE PAIN!",
"MANDREW IS NOT THE BEST! BUT HE DID JUST SCORE ON YOU.",
"BEHOLD THE POWER OF THE MANDREW, HE HAS SCORED!",
"PUNY MORTAL, MANDREW HAS SCORED AND HE LAUGHS AT YOUR SCORE!",
"M-A-N-D-R-E-W  S-C-O-R-E-S !!",
"MANDREW SCORED! SKIBIDI SIGMA MANDREW LIGMA!"
] 



# opening display of the board
def showBoard():
    
    # this is the fix for the goal horizontal alignment when the scores become double digit and start shifting to the right
    if stonesPerPit[13] > 9 or stonesPerPit[6] > 9 :
        doubleDigitSpacer = " "  # If either of the goals are double-digit, then reduce the spacer width.
    else:
        doubleDigitSpacer = "   "  # If the goals are single-digit, then increase the spacer width.
    
    print("\n\n",

    "  ","A B C D E F","\n",
    "  ","-----------","\n",
    "  ",stonesPerPit[12],stonesPerPit[11],stonesPerPit[10],stonesPerPit[9],stonesPerPit[8],stonesPerPit[7],"\n", 
    stonesPerPit[13],"    ",doubleDigitSpacer,"    ",stonesPerPit[6],"\n",
    "  ",stonesPerPit[0],stonesPerPit[1],stonesPerPit[2],stonesPerPit[3],stonesPerPit[4],stonesPerPit[5],"\n", 
    "  ","-----------","\n",
    "  ","G H I J K L","\n",

    )
    print(b,"\n")



# FUNCs #######################################################################

# player turn 
def playerTakeTurn():
    
    # Always have to declare vars global so they can carry value outside the FUNC. 
    # Update: this is actually a bad habit that has to be broken :D, funcs should be independent and modular.
    global playerTurnInput,moveInputStones,chosenIndex,allMovesSoFar,startingIndex,endingIndex,actualLastIndex 

    # The confusion comes from the fact that, in this game, the amount of stones in the pit
    # happens to dictate the indexed positions of the player/bot move and resulting index locations.

    while True:             
        # While loops really just deal with bad input - not recursive turn-taking.
        playerTurnInput = input("Choose a letter (G-L) to move your stones. ").upper()
        print("\n")        
        
        if playerTurnInput == "G" and stonesPerPit[0] != 0:
            print(f"You chose {playerTurnInput}. Your stones are moving!")            
            moveInputStones = stonesPerPit[0]
            chosenIndex = 0
            break
        elif playerTurnInput == "H" and stonesPerPit[1] != 0:
            print(f"You chose {playerTurnInput}. Your stones are moving!")            
            moveInputStones = stonesPerPit[1]
            chosenIndex = 1
            break 
        elif playerTurnInput == "I" and stonesPerPit[2] != 0:
            print(f"You chose {playerTurnInput}. Your stones are moving!")            
            moveInputStones = stonesPerPit[2]
            chosenIndex = 2 
            break
        elif playerTurnInput == "J" and stonesPerPit[3] != 0:
            print(f"You chose {playerTurnInput}. Your stones are moving!")            
            moveInputStones = stonesPerPit[3]
            chosenIndex = 3 
            break
        elif playerTurnInput == "K" and stonesPerPit[4] != 0:
            print(f"You chose {playerTurnInput}. Your stones are moving!")            
            moveInputStones = stonesPerPit[4]
            chosenIndex = 4
            break
        elif playerTurnInput == "L" and stonesPerPit[5] != 0:
            print(f"You chose {playerTurnInput}. Your stones are moving!")            
            moveInputStones = stonesPerPit[5]
            chosenIndex = 5 
            break
        else:
            print("Poor choice,try again!")
    #print("Ok the loop has been broken. We are done.")


    # set indexes for a player move  X X X X X X X X X X X X X X X X X X X X X X X X X X X  
    startingIndex = chosenIndex + 1     
    endingIndex = chosenIndex + moveInputStones + 1 
    actualLastIndex = endingIndex - 1
 

    # pass the bot goal logic - PLAYER SKIPPING BOT   
    skipTheBotGoal()

    # zero out the amount of stones within the chosen index
    stonesPerPit[chosenIndex] = 0


    # all moves so far (diagnostic string)
    allMovesSoFar = allMovesSoFar + playerTurnInput
    #print("\n:: All Moves So Far (player last):",allMovesSoFar,"\n")


    #score check and magic code
    dropNewStoneAmounts()





def botTurn():
    
    global playerTurnInput,moveInputStones,chosenIndex,allMovesSoFar,startingIndex,endingIndex,actualLastIndex
    global botInputMessage,botChoice,chosenIndex,startingIndex,endingIndex,moveInputStones,allMovesSoFar,actualLastIndex
    
    import random       

    botTurnPossibleIndexes = ["A","B","C","D","E","F"]
    #botChoice = "B" # Hardwired diagnostic hardbot.

    while True: 
        botInputMessage = input("It's Drew's turn, press ENTER. ").upper()
        print("\n")
        
        if botInputMessage == "":  # This (two double-quotes "") is the equivalent on an ENTER input.
            break  # Break is like saying "escape the loop here".          
        
        elif (botInputMessage == "G" 
            or botInputMessage == "H" 
            or botInputMessage == "I" 
            or botInputMessage == "J" 
            or botInputMessage == "K" 
            or botInputMessage == "L"):
            pass  #Pass basically means restart the loop

        else:
            print("ERROR 1")
    

    #  Four strategic bot turn logic (stealing the A stones!)
    #  This strategic area can just keep getting built up if Drew needs to be smarter!
    if stonesPerPit[0] == 0 and stonesPerPit[11] == 3 and stonesPerPit[12] != 0: #if B has 3 and G is empty, then score on A

        moveInputStones = stonesPerPit[11]
        chosenIndex = 11
        botChoice = "B" 
        #print(":: STRATEGIC! botChoice is B")         
    
    elif stonesPerPit[0] == 0 and stonesPerPit[10] == 4 and stonesPerPit[12] != 0: #if C has 4 and G is empty, then score on A

        moveInputStones = stonesPerPit[10]
        chosenIndex = 10 
        botChoice = "C"
        #print(":: STRATEGIC! botChoice is C") 

    elif stonesPerPit[0] == 0 and stonesPerPit[9] == 5 and stonesPerPit[12] != 0: #if D has 5 and G is empty, then score on A

        moveInputStones = stonesPerPit[9]
        chosenIndex = 9
        botChoice = "D"       
        #print(":: STRATEGIC! botChoice is D") 

    elif stonesPerPit[0] == 0 and stonesPerPit[8] == 6 and stonesPerPit[12] != 0: #if E has 6 and G is empty, then score on A
        
        moveInputStones = stonesPerPit[8]
        chosenIndex = 8 
        botChoice = "E"
        #print(":: STRATEGIC! botChoice is E") 

    # more smarter attacks (stealing the C and B stones!)
    elif stonesPerPit[2] == 0 and stonesPerPit[12] == 4 and stonesPerPit[10] != 0: #if A has 4 and I is empty, then score on C

        moveInputStones = stonesPerPit[12]
        chosenIndex = 12
        botChoice = "A" 
        #print(":: STRATEGIC! botChoice is A") 

    elif stonesPerPit[2] == 0 and stonesPerPit[11] == 5 and stonesPerPit[10] != 0: #if B has 5 and I is empty, then score on C

        moveInputStones = stonesPerPit[11]
        chosenIndex = 11
        botChoice = "B" 
        #print(":: STRATEGIC! botChoice is B") 

    elif stonesPerPit[1] == 0 and stonesPerPit[10] == 5 and stonesPerPit[11] != 0: #if C has 5 and H is empty, then score on B

        moveInputStones = stonesPerPit[10]
        chosenIndex = 10
        botChoice = "C" 
        #print(":: STRATEGIC! botChoice is C") 

    elif stonesPerPit[1] == 0 and stonesPerPit[9] == 6 and stonesPerPit[11] != 0: #if D has 6 and H is empty, then score on B

        moveInputStones = stonesPerPit[9]
        chosenIndex = 9
        botChoice = "D" 
        #print(":: STRATEGIC! botChoice is D") 

    elif stonesPerPit[12] == 0 and stonesPerPit[11] == 1 and stonesPerPit[0] != 0: #if B has 1 and A is empty, then score on G

        moveInputStones = stonesPerPit[11]
        chosenIndex = 11
        botChoice = "B" 
        #print(":: STRATEGIC! botChoice is B") 

    elif stonesPerPit[12] == 0 and stonesPerPit[10] == 2 and stonesPerPit[0] != 0: #if C has 2 and A is empty, then score on G

        moveInputStones = stonesPerPit[10]
        chosenIndex = 10
        botChoice = "C" 
        #print(":: STRATEGIC! botChoice is C") 

    elif stonesPerPit[12] == 0 and stonesPerPit[10] == 2 and stonesPerPit[0] != 0: #if C has 2 and A is empty, then score on G

        moveInputStones = stonesPerPit[10]
        chosenIndex = 10
        botChoice = "C" 
        #print(":: STRATEGIC! botChoice is C") 

    elif stonesPerPit[11] == 0 and stonesPerPit[10] == 1 and stonesPerPit[1] != 0: #if C has 1 and B is empty, then score on H

        moveInputStones = stonesPerPit[10]
        chosenIndex = 10
        botChoice = "C" 
        #print(":: STRATEGIC! botChoice is C") 

    elif stonesPerPit[9] == 0 and stonesPerPit[8] == 1 and stonesPerPit[3] != 0: #if E has 1 and D is empty, then score on D

        moveInputStones = stonesPerPit[8]
        chosenIndex = 8
        botChoice = "E" 
        #print(":: STRATEGIC! botChoice is E") 

    elif stonesPerPit[9] == 0 and stonesPerPit[7] == 2 and stonesPerPit[3] != 0: #if F has 2 and D is empty, then score on D

        moveInputStones = stonesPerPit[7]
        chosenIndex = 7
        botChoice = "F" 
        #print(":: STRATEGIC! botChoice is F") 

    elif stonesPerPit[12] == 0 and stonesPerPit[7] == 5 and stonesPerPit[0] != 0: #if F has 5 and G is empty, then score on A

        moveInputStones = stonesPerPit[7]
        chosenIndex = 7
        botChoice = "F" 
        #print(":: STRATEGIC! botChoice is F") 

    elif stonesPerPit[4] == 0 and stonesPerPit[12] == 6 and stonesPerPit[8] != 0: #if A has 6 and K is empty, then score on E

        moveInputStones = stonesPerPit[12]
        chosenIndex = 12
        botChoice = "A" 
        #print(":: STRATEGIC! botChoice is A") 

    elif stonesPerPit[5] == 0 and stonesPerPit[11] == 8 and stonesPerPit[7] != 0: #if B has 8 and L is empty, then score on F

        moveInputStones = stonesPerPit[11]
        chosenIndex = 11
        botChoice = "B" 
        #print(":: STRATEGIC! botChoice is B") 



    # if any bot index is bigger than 9, choose that index as the bot choice
            
    elif stonesPerPit[7] >= 9:     #F
        moveInputStones = stonesPerPit[7] #set the values of things based on the current amount of slot stones 
        chosenIndex = 7
        botChoice = "F" 
        #print(":: BIGGERTHAN9 botChoice is F")                

    elif stonesPerPit[8] >= 9:   #E
        moveInputStones = stonesPerPit[8]
        chosenIndex = 8 
        botChoice = "E"
        #print(":: BIGGERTHAN9 botChoice is E")        

    elif stonesPerPit[9] >= 9:   #D
        moveInputStones = stonesPerPit[9]
        chosenIndex = 9 
        botChoice = "D"
        #print(":: BIGGERTHAN9 botChoice is D")        

    elif stonesPerPit[10] >= 9:   #C
        moveInputStones = stonesPerPit[10]
        chosenIndex = 10
        botChoice = "C"
        #print(":: BIGGERTHAN9 botChoice is C")        

    elif stonesPerPit[11] >= 9:  #B
        moveInputStones = stonesPerPit[11]
        chosenIndex = 11 
        botChoice = "B"
        #print(":: BIGGERTHAN9 botChoice is B")         

    elif stonesPerPit[12] >= 9:  #A
        moveInputStones = stonesPerPit[12]
        chosenIndex = 12
        botChoice = "A" 
        #print(":: BIGGERTHAN9 botChoice is A")         

    else:
        #print(":: Bot strategy and higher than 9 didnt work. Time for randos.")  # This works great!

        
        while True:
            botChoice = random.choice(botTurnPossibleIndexes)   # This recursive looping works correctly!
                   

            #  Regular rando turn taking.
            if botChoice == "F" and stonesPerPit[7] != 0:
                moveInputStones = stonesPerPit[7]
                chosenIndex = 7 # index 7                
                #print(":: RANDO botChoice is",botChoice) 
                break

            elif botChoice == "E" and stonesPerPit[8] != 0:
                moveInputStones = stonesPerPit[8]
                chosenIndex = 8 # index 8
                #print(":: RANDO botChoice is",botChoice) 
                break

            elif botChoice == "D" and stonesPerPit[9] != 0:
                moveInputStones = stonesPerPit[9]
                chosenIndex = 9 # index 9
                #print(":: RANDO botChoice is",botChoice) 
                break

            elif botChoice == "C" and stonesPerPit[10] != 0:
                moveInputStones = stonesPerPit[10]
                chosenIndex = 10 # index 10
                #print(":: RANDO botChoice is",botChoice) 
                break

            elif botChoice == "B" and stonesPerPit[11] != 0:
                moveInputStones = stonesPerPit[11]
                chosenIndex = 11 # index 11
                #print(":: RANDO botChoice is",botChoice) 
                break

            elif botChoice == "A" and stonesPerPit[12] != 0:
                moveInputStones = stonesPerPit[12]
                chosenIndex = 12 # index 12
                #print(":: RANDO botChoice is",botChoice) 
                break      

            else:
                pass
                #print(":: Bot can't find a valid turn so he's trying again.") # this works great!


    # Present Mandrew's choice.
    print(f"Mandrew chose {botChoice}.")

    # set indexes for a bot move  X X X X X X X X X X X X X X X X X X X X X X X X X X X
    startingIndex = chosenIndex + 1 
    endingIndex = chosenIndex + moveInputStones + 1 
    actualLastIndex = endingIndex - 1
    
    #pass your goal logic - BOT
    skipThePlayerGoal()

    # zero out the amount of stones within the chosen index
    stonesPerPit[chosenIndex] = 0 

    # all moves so far (diagnostic string)
    allMovesSoFar = allMovesSoFar + botChoice
    #print("\n:: All Moves So Far (bot last):",allMovesSoFar,"\n")

    #score check and magic code
    dropNewStoneAmounts()




def magicCode():
    
    
    global chosenIndex,startingIndex,endingIndex
    

    # the MAGIC-CODE - that drops the new stone amounts in the indexes
    for i in range(startingIndex,endingIndex):
        stonesPerPit[i] = stonesPerPit[i] + 1
        #print(i,end=" ") #diagnostic. Also the end=" " makes the results print horizontally
    
    stonesPerPit[chosenIndex] = 0 # ALWAYS zero out the stones within the chosen index



def scoreCheckLogic():
  
    global playerTurnRightNow,actualLastIndex,stolenIndexAcross,chosenIndex,scoreAmount

    #  Steal-scoring logic 
    if actualLastIndex == 7:
        stolenIndexAcross = 5
    elif actualLastIndex == 8:
        stolenIndexAcross = 4
    elif actualLastIndex == 9:
        stolenIndexAcross = 3
    elif actualLastIndex == 10:
        stolenIndexAcross = 2
    elif actualLastIndex == 11:
        stolenIndexAcross = 1
    elif actualLastIndex == 12:
        stolenIndexAcross = 0

    elif actualLastIndex == 5:
        stolenIndexAcross = 7
    elif actualLastIndex == 4:
        stolenIndexAcross = 8
    elif actualLastIndex == 3:
        stolenIndexAcross = 9
    elif actualLastIndex == 2:
        stolenIndexAcross = 10
    elif actualLastIndex == 1:
        stolenIndexAcross = 11
    elif actualLastIndex == 0:
        stolenIndexAcross = 12

    elif actualLastIndex == 14:
        stolenIndexAcross = 12 
    elif actualLastIndex == 15:
        stolenIndexAcross = 11 
    elif actualLastIndex == 16:
        stolenIndexAcross = 10 
    elif actualLastIndex == 17:
        stolenIndexAcross = 9 
    elif actualLastIndex == 18:
        stolenIndexAcross = 8  
    elif actualLastIndex == 19:
        stolenIndexAcross = 7 

    elif actualLastIndex == 12:
        stolenIndexAcross = 0 
    elif actualLastIndex == 11:
        stolenIndexAcross = 1 
    elif actualLastIndex == 10:
        stolenIndexAcross = 2 
    elif actualLastIndex == 9:
        stolenIndexAcross = 3 
    elif actualLastIndex == 8:
        stolenIndexAcross = 4 
    elif actualLastIndex == 7:
        stolenIndexAcross = 5 




    elif actualLastIndex == 21:
        stolenIndexAcross = 5 
    elif actualLastIndex == 22:
        stolenIndexAcross = 4 
    elif actualLastIndex == 23:
        stolenIndexAcross = 3 
    elif actualLastIndex == 24:
        stolenIndexAcross = 2 
    elif actualLastIndex == 25:
        stolenIndexAcross = 1 
    elif actualLastIndex == 26:
        stolenIndexAcross = 0 

    elif actualLastIndex == 19:
        stolenIndexAcross = 7 
    elif actualLastIndex == 18:
        stolenIndexAcross = 8 
    elif actualLastIndex == 17:
        stolenIndexAcross = 9 
    elif actualLastIndex == 16:
        stolenIndexAcross = 10 
    elif actualLastIndex == 15:
        stolenIndexAcross = 11 
    elif actualLastIndex == 14:
        stolenIndexAcross = 12 


    else:
        print("ERROR 2")
    
  
    
# zzzz zzzz zzzz zzzz zzzz zzzz zzzz zzzz zzzz zzzz zzzz (Adding visual topography to my comments and code)

    # the actual scoring into goals (not magicCode)
    if chosenIndex == 0 or chosenIndex == 1 or chosenIndex == 2 or chosenIndex == 3 or chosenIndex == 4 or chosenIndex == 5: 
        stonesPerPit[6] = stonesPerPit[6] + stonesPerPit[stolenIndexAcross] + 1 # the stone that triggered the score is a point too
        #print(f"\n:: !!Score RP, actualLastIndex == {actualLastIndex}!!") # player score!      
        print(f"YOU SCORED +{stonesPerPit[6] - rightScoreOLD} STONES, GO AGAIN!")  # Player-score message.
        playerTurnRightNow = False

    else:
        stonesPerPit[13] = stonesPerPit[13] + stonesPerPit[stolenIndexAcross] + 1    
        #print(f"\n:: !!Score LP, actualLastIndex == {actualLastIndex}!!") # bot score!
        print(random.choice(botMessages),"+",stonesPerPit[13] - leftScoreOLD)  # Mandew score-message.
        playerTurnRightNow = True

# zzzz zzzz zzzz zzzz zzzz zzzz zzzz zzzz zzzz zzzz zzzz






def dropNewStoneAmounts():
 
    
    global endingIndex,chosenIndex,allMovesSoFar,playerTurnRightNow,actualLastIndex

    #CHECK FOR SCORE #################################################################


    # SPECIAL score check for second player turn (for dropping 1 on the player goal)
    if actualLastIndex == 6:   # (player goal)

        magicCode()
        # if chosen is a player index then give player the points
        if chosenIndex == 0 or chosenIndex == 1 or chosenIndex == 2 or chosenIndex == 3 or chosenIndex == 4 or chosenIndex == 5: 
            #print(":: Score RP just +1, goal index 6!!") # player score!
            print("YOU SCORED +1 STONE, GO AGAIN!")
            playerTurnRightNow = False

        # if chosen is a bot index then give bot the points
        else:
            actualLastIndex = 7
            #stonesPerPit[6] = stonesPerPit[6] - 1 # this creates the "skip" effect by removing the stone it just gave 
            #print(":: scorecheck: bot skipped player goal")
            playerTurnRightNow = True
        

    # SPECIAL score check for second bot turn (for dropping 1 on the bot goal)
    elif actualLastIndex == 13:   # (bot goal)

        magicCode()
        if chosenIndex == 7 or chosenIndex == 8 or chosenIndex == 9 or chosenIndex == 10 or chosenIndex == 11 or chosenIndex == 12: 
            #print(":: Score LP just +1, goal index 13!!") # bot score!
            print(random.choice(botMessages),"+1")
            playerTurnRightNow = True
        else:
            actualLastIndex = 14
            #stonesPerPit[13] = stonesPerPit[13] - 1 # this creates the "skip" effect by removing the stone it just gave 
            #print(":: scorecheck: player skipped bot goal") 
            playerTurnRightNow = False



    # STEALING FROM THE PLAYER ROW - GHIJKL - 0,1,2,3,4,5 (player row)    
    elif actualLastIndex == 12 and stonesPerPit[12] == 0 and stonesPerPit[0] != 0:  # STEAL FROM G (0)

        magicCode()
        scoreCheckLogic()

        stonesPerPit[0] = 0              # zero out the stolen pit - IF SCORE
        stonesPerPit[actualLastIndex] = 0  # zero out the stones within the actual last index - IF SCORE


    elif actualLastIndex == 11 and stonesPerPit[11] == 0 and stonesPerPit[1] != 0:  # STEAL FROM H (1)
     
        magicCode()
        scoreCheckLogic()  

        stonesPerPit[1] = 0
        stonesPerPit[actualLastIndex] = 0


    elif actualLastIndex == 10 and stonesPerPit[10] == 0 and stonesPerPit[2] != 0:  # STEAL FROM I (2)

        magicCode()
        scoreCheckLogic()  
              
        stonesPerPit[2] = 0
        stonesPerPit[actualLastIndex] = 0


    elif actualLastIndex == 9 and stonesPerPit[9] == 0 and stonesPerPit[3] != 0:    # STEAL FROM J (3)

        magicCode()
        scoreCheckLogic()  

        stonesPerPit[3] = 0
        stonesPerPit[actualLastIndex] = 0


    elif actualLastIndex == 8 and stonesPerPit[8] == 0 and stonesPerPit[4] != 0:    # STEAL FROM K (4)

        magicCode()
        scoreCheckLogic()  
                
        stonesPerPit[4] = 0
        stonesPerPit[actualLastIndex] = 0


    elif actualLastIndex == 7 and stonesPerPit[7] == 0 and stonesPerPit[5] != 0:   # STEAL FROM L (5)
              
        magicCode()
        scoreCheckLogic()  
                
        stonesPerPit[5] = 0  
        stonesPerPit[actualLastIndex] = 0


    # index 6 gets skipped cuz its a goal and we already addressed that scenario


    # STEALING FROM THE BOT ROW - FEDCBA - 7,8,9,10,11,12 (bot row)

    elif actualLastIndex == 5 and stonesPerPit[5] == 0 and stonesPerPit[7] != 0:    # STEAL FROM F (7)

        magicCode()
        scoreCheckLogic()  
        
        stonesPerPit[7] = 0
        stonesPerPit[actualLastIndex] = 0 
        

    elif actualLastIndex == 4 and stonesPerPit[4] == 0 and stonesPerPit[8] != 0:    # STEAL FROM E (8)

        magicCode()
        scoreCheckLogic()  
        
        stonesPerPit[8] = 0
        stonesPerPit[actualLastIndex] = 0

       
    elif actualLastIndex == 3 and stonesPerPit[3] == 0 and stonesPerPit[9] != 0:    # STEAL FROM D (9)

        magicCode()
        scoreCheckLogic()  
        
        stonesPerPit[9] = 0
        stonesPerPit[actualLastIndex] = 0     


    elif actualLastIndex == 2 and stonesPerPit[2] == 0 and stonesPerPit[10] != 0:   # STEAL FROM C (10)

        magicCode()
        scoreCheckLogic()  
        
        stonesPerPit[10] = 0
        stonesPerPit[actualLastIndex] = 0   


    elif actualLastIndex == 1 and stonesPerPit[1] == 0 and stonesPerPit[11] != 0:   # STEAL FROM B (11)

        magicCode()
        scoreCheckLogic()  
        
        stonesPerPit[11] = 0
        stonesPerPit[actualLastIndex] = 0 

   
    elif endingIndex == 0 and stonesPerPit[0] == 0 and stonesPerPit[12] != 0:   # STEAL FROM A (12)

        magicCode()
        scoreCheckLogic()  
        
        stonesPerPit[12] = 0
        stonesPerPit[actualLastIndex] = 0



    #we skip index 13 here because it's not a stealing-scoring pit


    # "after-12" indexes scoring logic - ACROSS THE STREET PAIRS

      
    # 14-15-16-17-18-19 
    # G--H--I--J--K--L

    # 26-25-24-23-22-21
    # A--B--C--D--E--F
    

    elif actualLastIndex == 26 and stonesPerPit[12] == 0 and stonesPerPit[0] != 0:  # STEAL FROM G

        magicCode()
        scoreCheckLogic()  
        
        stonesPerPit[12] = 0
        stonesPerPit[0] = 0 
        stonesPerPit[actualLastIndex] = 99

    elif actualLastIndex == 25 and stonesPerPit[11] == 0 and stonesPerPit[1] != 0:  # STEAL FROM H

        magicCode()
        scoreCheckLogic()  
        
        stonesPerPit[11] = 0
        stonesPerPit[1] = 0 
        stonesPerPit[actualLastIndex] = 99 

    elif actualLastIndex == 24 and stonesPerPit[10] == 0 and stonesPerPit[2] != 0:  # STEAL FROM I

        magicCode()
        scoreCheckLogic()  
        
        stonesPerPit[10] = 0
        stonesPerPit[2] = 0 
        stonesPerPit[actualLastIndex] = 99 

    elif actualLastIndex == 23 and stonesPerPit[9] == 0 and stonesPerPit[3] != 0:  # STEAL FROM J

        magicCode()
        scoreCheckLogic()  
        
        stonesPerPit[9] = 0
        stonesPerPit[3] = 0 
        stonesPerPit[actualLastIndex] = 99  

    elif actualLastIndex == 22 and stonesPerPit[8] == 0 and stonesPerPit[4] != 0:   # STEAL FROM K

        magicCode()
        scoreCheckLogic()  
        
        stonesPerPit[8] = 0
        stonesPerPit[4] = 0  
        stonesPerPit[actualLastIndex] = 99

    elif actualLastIndex == 21 and stonesPerPit[7] == 0 and stonesPerPit[5] != 0:   # STEAL FROM L

        magicCode()
        scoreCheckLogic()  
        
        stonesPerPit[7] = 0
        stonesPerPit[5] = 0  
        stonesPerPit[actualLastIndex] = 99
       
      

    
    # here is where scoring logic for 18-23  (actualLast: 14 to 19)


    elif actualLastIndex == 14 and stonesPerPit[0] == 0 and stonesPerPit[12] != 0:   # STEAL FROM A

        magicCode()
        scoreCheckLogic()

        stonesPerPit[0] = 0 # zero out the stolen pit - IF SCORE
        stonesPerPit[12] = 0
        stonesPerPit[actualLastIndex] = 99

    elif actualLastIndex == 15 and stonesPerPit[1] == 0 and stonesPerPit[11] != 0:   # STEAL FROM B

        magicCode()
        scoreCheckLogic()  
        
        stonesPerPit[1] = 0
        stonesPerPit[11] = 0 
        stonesPerPit[actualLastIndex] = 99

    elif actualLastIndex == 16 and stonesPerPit[2] == 0 and stonesPerPit[10] != 0:   # STEAL FROM C

        magicCode()
        scoreCheckLogic()  
        
        stonesPerPit[2] = 0
        stonesPerPit[10] = 0 
        stonesPerPit[actualLastIndex] = 99

    elif actualLastIndex == 17 and stonesPerPit[3] == 0 and stonesPerPit[9] != 0:   # STEAL FROM D

        magicCode()
        scoreCheckLogic()  
        
        stonesPerPit[3] = 0
        stonesPerPit[9] = 0  
        stonesPerPit[actualLastIndex] = 99

    elif actualLastIndex == 18 and stonesPerPit[4] == 0 and stonesPerPit[8] != 0:   # STEAL FROM E

        magicCode()
        scoreCheckLogic()  
        
        stonesPerPit[4] = 0
        stonesPerPit[8] = 0  
        stonesPerPit[actualLastIndex] = 99

    elif actualLastIndex == 19 and stonesPerPit[5] == 0 and stonesPerPit[7] != 0:   # STEAL FROM F

        magicCode()
        scoreCheckLogic()  
        
        stonesPerPit[5] = 0
        stonesPerPit[7] = 0 
        stonesPerPit[actualLastIndex] = 99

    else:
        #print(":: SCORE CHECK OVER")
        #print(":: No scores this round but the magic code is now running!")
        magicCode()


    reinsertionAndDisplay()





#  This inserts the updated list values (post-12 only?) back into the under-12 indexes for proper display.
def reinsertionAndDisplay():
    
    global playerTurnRightNow,leftScoreOLD,rightScoreOLD
    

    #this is the code that fixes the overwriting problem that occurs when an index is impacted twice

    #player row - GHIJKL
    if stonesPerPit[14] == 99: #GsX
        stonesPerPit[0] = stonesPerPit[0]   #if the default 99s haven't been touched, then dont change anything
    elif stonesPerPit[14] != 99:            #but if the 99s HAVE been touched, then trasfer their values to the lower index
        stonesPerPit[0] = stonesPerPit[0] + (stonesPerPit[14] - 99)         
    else:
        print("ERROR 3")
        
    if stonesPerPit[15] == 99: #HsX
        stonesPerPit[1] = stonesPerPit[1]
    elif stonesPerPit[15] != 99:
        stonesPerPit[1] = stonesPerPit[1] + (stonesPerPit[15] - 99)   
    else:
        print("ERROR 4")

    if stonesPerPit[16] == 99: #IsX
        stonesPerPit[2] = stonesPerPit[2]
    elif stonesPerPit[16] != 99:
        stonesPerPit[2] = stonesPerPit[2] + (stonesPerPit[16] - 99)         
    else:
        print("ERROR 5")

    if stonesPerPit[17] == 99: #JsX
        stonesPerPit[3] = stonesPerPit[3]
    elif stonesPerPit[17] != 99:
        stonesPerPit[3] = stonesPerPit[3] + (stonesPerPit[17] - 99)         
    else:
        print("ERROR 6")

    if stonesPerPit[18] == 99: #KsX
        stonesPerPit[4] = stonesPerPit[4]
    elif stonesPerPit[18] != 99:
        stonesPerPit[4] = stonesPerPit[4] + (stonesPerPit[18] - 99)         
    else:
        print("ERROR 7")

    if stonesPerPit[19] == 99: #LsX
        stonesPerPit[5] = stonesPerPit[5]
    elif stonesPerPit[19] != 99:
        stonesPerPit[5] = stonesPerPit[5] + (stonesPerPit[19] - 99)         
    else:
        print("ERROR 8")

    if stonesPerPit[20] == 99: #LsX
        stonesPerPit[6] = stonesPerPit[6]
    elif stonesPerPit[20] != 99:
        stonesPerPit[6] = stonesPerPit[6] + (stonesPerPit[19] - 99)         
    else:
        print("ERROR 9")

    #index 20 (aka 6) would go here



    # bot row - FEDCBA
    if stonesPerPit[21] == 99: #FsX
        stonesPerPit[7] = stonesPerPit[7]
    elif stonesPerPit[21] != 99:
        stonesPerPit[7] = stonesPerPit[7] + (stonesPerPit[21] - 99)         
    else:
        print("ERROR 10")

    if stonesPerPit[22] == 99: #EsX
        stonesPerPit[8] = stonesPerPit[8]
    elif stonesPerPit[22] != 99:
        stonesPerPit[8] = stonesPerPit[8] + (stonesPerPit[22] - 99)         
    else:
        print("ERROR 11")

    if stonesPerPit[23] == 99: #DsX
        stonesPerPit[9] = stonesPerPit[9]
    elif stonesPerPit[23] != 99:
        stonesPerPit[9] = stonesPerPit[9] + (stonesPerPit[23] - 99)         
    else:
        print("ERROR 12")

    if stonesPerPit[24] == 99: #CsX
        stonesPerPit[10] = stonesPerPit[10]
    elif stonesPerPit[24] != 99:
        stonesPerPit[10] = stonesPerPit[10] + (stonesPerPit[24] - 99)         
    else:
        print("ERROR 13")

    if stonesPerPit[25] == 99: #BsX
        stonesPerPit[11] = stonesPerPit[11]
    elif stonesPerPit[25] != 99:
        stonesPerPit[11] = stonesPerPit[11] + (stonesPerPit[25] - 99)         
    else:
        print("ERROR 14")

    if stonesPerPit[26] == 99: #AsX
        stonesPerPit[12] = stonesPerPit[12]
    elif stonesPerPit[26] != 99:
        stonesPerPit[12] = stonesPerPit[12] + (stonesPerPit[26] - 99)   
    else:
        print("ERROR 15")


    if stonesPerPit[27] == 99: #LsX
        stonesPerPit[13] = stonesPerPit[13]
    elif stonesPerPit[27] != 99:
        stonesPerPit[13] = stonesPerPit[13] + (stonesPerPit[19] - 99)         
 
    else:
        print("ERROR 16")


    # Put current scores into a set of "recent memory" variables used later to calculate scoring notification. 
    leftScoreOLD = stonesPerPit[13]
    rightScoreOLD = stonesPerPit[6]


    # This resets the 14-26 indexes back to 99 to avoid messing up calculations after multiple turns.
    for i in range(14,26):        
        stonesPerPit[i] = 99



    # Resinsertion display.
    showBoard()
    
    # Check if game is over.
    isGameOver()

    # Whose turn is it?
    whoseTurnIsIt()

        



def skipTheBotGoal():
    
    global endingIndex,actualLastIndex
    
    # ++++++ ++++++ ++++++ ++++++ ++++++ ++++++ ++++++ ++++++ ++++++ ++++++ ++++++ ++++++
    if stonesPerPit[5] >= 8 and chosenIndex == 5: 
        stonesPerPit[13] = stonesPerPit[13] - 1  # this subtracting one creates a SKIP effect

        # This extends the move of the turn by one so that magic code works correctly.
        endingIndex = endingIndex + 1  
        actualLastIndex - actualLastIndex + 1
        #print(":: skipTheBotGoal logic triggered! (L)")
    #else:
        #print("goal passing logic not triggered :(")


    elif stonesPerPit[4] >= 9 and chosenIndex == 4: 
        stonesPerPit[13] = stonesPerPit[13] - 1
        endingIndex = endingIndex + 1
        actualLastIndex = actualLastIndex + 1
        #print(":: skipTheBotGoal logic triggered! (K)")

    elif stonesPerPit[3] >= 10 and chosenIndex == 3: 
        stonesPerPit[13] = stonesPerPit[13] - 1
        endingIndex = endingIndex + 1
        actualLastIndex = actualLastIndex + 1
        #print(":: skipTheBotGoal logic triggered! (J)")

    elif stonesPerPit[2] >= 11 and chosenIndex == 2: 
        stonesPerPit[13] = stonesPerPit[13] - 1
        endingIndex = endingIndex + 1
        actualLastIndex = actualLastIndex + 1
        #print(":: skipTheBotGoal logic triggered! (I)")

    elif stonesPerPit[1] >= 12 and chosenIndex == 1: 
        stonesPerPit[13] = stonesPerPit[13] - 1
        endingIndex = endingIndex + 1
        actualLastIndex = actualLastIndex + 1
        #print(":: skipTheBotGoal logic triggered! (H)")

    elif stonesPerPit[0] >= 13 and chosenIndex == 0: 
        stonesPerPit[13] = stonesPerPit[13] - 1
        endingIndex = endingIndex + 1
        actualLastIndex = actualLastIndex + 1
        #print(":: skipTheBotGoal logic triggered! (G)")


    else:
        pass
        #print("skipTheBotGoal logic not triggered :(")







def skipThePlayerGoal():
 
    global endingIndex,actualLastIndex    


    # ++++++ ++++++ ++++++ ++++++ ++++++ ++++++ ++++++ ++++++ ++++++ ++++++ ++++++ ++++++
    if stonesPerPit[12] >= 8 and chosenIndex == 12: 
        stonesPerPit[6] = stonesPerPit[6] - 1
        endingIndex = endingIndex + 1
        actualLastIndex = actualLastIndex + 1
        #print(":: skipThePlayerGoal logic triggered! (A)")


    elif stonesPerPit[11] >= 9 and chosenIndex == 11: 
        stonesPerPit[6] = stonesPerPit[6] - 1
        endingIndex = endingIndex + 1
        actualLastIndex = actualLastIndex + 1
        #print(":: skipThePlayerGoal logic triggered! (B)")

    elif stonesPerPit[10] >= 10 and chosenIndex == 10: 
        stonesPerPit[6] = stonesPerPit[6] - 1
        endingIndex = endingIndex + 1
        actualLastIndex = actualLastIndex + 1
        #print(":: skipThePlayerGoal logic triggered! (C)")

    elif stonesPerPit[9] >= 11 and chosenIndex == 9: 
        stonesPerPit[6] = stonesPerPit[6] - 1
        endingIndex = endingIndex + 1
        actualLastIndex = actualLastIndex + 1
        #print(":: skipThePlayerGoal logic triggered! (D)")

    elif stonesPerPit[8] >= 12 and chosenIndex == 8: 
        stonesPerPit[6] = stonesPerPit[6] - 1
        endingIndex = endingIndex + 1
        actualLastIndex = actualLastIndex + 1
        #print(":: skipThePlayerGoal logic triggered! (E)")

    elif stonesPerPit[7] >= 13 and chosenIndex == 7: 
        stonesPerPit[6] = stonesPerPit[6] - 1
        endingIndex = endingIndex + 1
        actualLastIndex = actualLastIndex + 1
        #print(":: skipThePlayerGoal logic triggered! (F)")


    else:
        pass
        #print("skipThePlayerGoal logic not triggered :(")
  
    
    

# CHECK IF THE GAME IS OVER
def isGameOver():
    
    # If all of the 6 bot indexes are zeroes, then game over!
    if (stonesPerPit[7] == 0
        and stonesPerPit[8] == 0
        and stonesPerPit[9] == 0 
        and stonesPerPit[10] == 0 
        and stonesPerPit[11] == 0 
        and stonesPerPit[12] == 0):

        #player gets all the leftover stones added to their score
        stonesPerPit[6] = (
        stonesPerPit[6] 
        + stonesPerPit[0] 
        + stonesPerPit[1] 
        + stonesPerPit[2] 
        + stonesPerPit[3] 
        + stonesPerPit[4] 
        + stonesPerPit[5]) 
          
        #clear the player row
        stonesPerPit[0] = 0
        stonesPerPit[1] = 0 
        stonesPerPit[2] = 0
        stonesPerPit[3] = 0
        stonesPerPit[4] = 0
        stonesPerPit[5] = 0     

        gameOver()

    # If all of the 6 player indexes are zeroes, then game over!
    elif (stonesPerPit[0] == 0
        and stonesPerPit[1] == 0 
        and stonesPerPit[2] == 0 
        and stonesPerPit[3] == 0 
        and stonesPerPit[4] == 0 
        and stonesPerPit[5] == 0):

        #player gets all the leftover stones added to their score
        stonesPerPit[13] = (
        stonesPerPit[13] 
        + stonesPerPit[7] 
        + stonesPerPit[8] 
        + stonesPerPit[9] 
        + stonesPerPit[10] 
        + stonesPerPit[11] 
        + stonesPerPit[12])
        
        #clear the bot row
        stonesPerPit[12] = 0
        stonesPerPit[11] = 0 
        stonesPerPit[10] = 0
        stonesPerPit[9] = 0
        stonesPerPit[8] = 0
        stonesPerPit[7] = 0 

        gameOver()

    else:
        pass
        #print("::No winners yet!")


def whoseTurnIsIt():
    
    global playerTurnRightNow

    if playerTurnRightNow == True:
        #print(":: Ok now it's the bot's turn!!")
        playerTurnRightNow = False
        botTurn()
        
    elif playerTurnRightNow == False:
        #print(":: Ok now it's the player's turn!!")        
        playerTurnRightNow = True
        playerTakeTurn()
    else:
        print(":: ERROR - PlayerTurnRightNow seems broken:",playerTurnRightNow) 


def gameOver():
    
    print("A row has been cleared, and now the opposing row stones go to that player as scores...")
    showBoard()
    
    winner = " "

    if stonesPerPit[13] < stonesPerPit[6]:
        winner = "you have"
        print(f"Game over, {winner} won by {stonesPerPit[6] - stonesPerPit[13]} stones. But Mandrew will have his revenge!")
    elif stonesPerPit[13] > stonesPerPit[6]:
        winner = "Mandrew"
        print(f"Game over, {winner} won by {stonesPerPit[13] - stonesPerPit[6]} stones!\n")
        print(manDrewScoreArt)
    else:
       print("Wait, is this a tie?")
        #print(":: Something is broken cuz no body won!")
    
    

    # Pause execution for 5 seconds
    import time

    print(".")    
    time.sleep(10)
    print("..")
    time.sleep(10)
    print("...program will exit in 30 secs...") 
    time.sleep(30) 

    exit() #exit game




# BEGIN ++++++++++++++++++++++++++++++++++++++++++++++++++++


#intro
print(intro,b)

# FUNC
showBoard()

# FUNC
playerTakeTurn()  







"""
"""























