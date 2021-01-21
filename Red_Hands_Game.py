#Source for import sys: https://stackoverflow.com/questions/19782075/how-to-stop-terminate-a-python-script-from-running/34029481
import random
import sys

def thegame():
    global alluserscore
    alluserscore = 0
    global allcomputerscore
    allcomputerscore = 0

#This is where the instructions of the game are given
    def instructions():
        print("Today you will be playing the Python adaptation of Red Hands")
        print("Your objectie in this game is to be the first person to get 10 points")
        print("You can get points through the two main parts of this game")
        print("There are two main parts to this game. There is an attacking and defending turn")
        print("In the attacking turn you can only get points by successfully hitting your opponent.")
        print("In the defending turn you can only get points by successfully dodging your opponent.")
        print("In the same way you can get points, those are the only way your opponent can get points")
        print("Turns will only switch when someone on the attacking turn MISSES and it will be the other person attacking after")
        print("If nobody gets a point the round will restart with the same person attacking/defending")
        print("Now that you know the rules lets play")
        print('\n')
    instructions()
    
#This is where functions needed for keeping score are defined and as the game nears its end give terms that will determine a winner
    def scorekeeping(roundwinner):
        if roundwinner == str("none"):
            print("nothing")
        elif roundwinner == str("user"):
            global  alluserscore
            alluserscore +=1
        elif roundwinner == str("computer"):
            global allcomputerscore
            allcomputerscore +=1
        else:
            print("confusion")

#This redefines global variables if the user wishes to play again
    def restart():
        global alluserscore
        alluserscore = 0
        global allcomputerscore
        allcomptuerscore = 0

#This allows there to be a condition in which the game will stop and a winner can be decided
    def howtowin(alluserscore,allcomputerscore):
        if int(alluserscore) == 10:
            print("YOU WIN!")
            print("Final score:" + '\n'+ "User:" + str(alluserscore) + " V. Opponent:" + str(allcomputerscore) + '\n')
            response = input("Do you want to play again? ")
            if response.lower() == str("yes"):
                restart()
                thegame()
            elif response.lower() == str("no"):
                print("Goodbye")
                sys.exit()

        elif int(allcomputerscore) == 10:
            print("YOUR OPPONENT WINS!")
            print("Final score:" + 'n'+ "User:" + str(alluserscore) + " V. Opponent:" + str(allcomputerscore) + '\n')
            response = input("Do you want to play again? ")
            if response.lower() == str("yes"):
                restart()
                thegame()
            elif response.lower() == str("no"):
                print("Goodbye")
                sys.exit()
        else:
            print("")


#This is where functions needed for when the user is attacking are defined and used to determine who gets a point
    def userattacks():
        def userattack():
            userattackinput = input("Would you like to swipe?(Yes or No) ")
            if userattackinput.lower() == str("yes"):
                print("You choose to swipe")
                attackaction = 1
                return attackaction
            elif userattackinput.lower() == str("no"):
                print("You stayed still")
                attackaction = 0
                return attackaction
            else:
                print("That is not an option")
                userattack()
        usermoveattack_action = userattack()

        def computerdefense():
            number = random.randint(1,2)
            if int(number) % 2 == 0:
                print("the computer stayed")
                action = 0
                return action
            else:
                print("the computer moved back")
                action = 1
                return action
        computerdefense_action = computerdefense()

        def theuserattacksoutcome():
            global userscore 
            global computerscore
            if usermoveattack_action == 1 and computerdefense_action == 0:
                print("You hit your opponent and got the point")
                roundwinner = str("user")
                scorekeeping(roundwinner)
                print("User:" + str(alluserscore) + " V. Opponent:" + str(allcomputerscore) + '\n')
                howtowin(alluserscore,allcomputerscore)
                userattacks()
            elif usermoveattack_action == 1 and computerdefense_action == 1:
                print("You missed! Your opponent gets the point and the chance to attack")
                roundwinner = str("computer")
                scorekeeping(roundwinner)
                print("User:" + str(alluserscore) + " V. Opponent:" + str(allcomputerscore) + '\n')
                howtowin(alluserscore,allcomputerscore)
                computerattacks()
            elif usermoveattack_action == 0 and computerdefense_action == 0:
                print("Nobody moved")
                roundwinner = str("none")
                scorekeeping(roundwinner)
                print("User:" + str(alluserscore) + " V. Opponent:" + str(allcomputerscore) + '\n')
                howtowin(alluserscore,allcomputerscore)
                userattacks()
            elif usermoveattack_action == 0 and computerdefense_action == 1:
                print("Only your opponent moved")
                roundwinner = str("none")
                scorekeeping(roundwinner)
                print("User:" + str(alluserscore) + " V. Opponent:" + str(allcomputerscore) + '\n')
                howtowin(alluserscore,allcomputerscore)
                userattacks()
            else:
                print("An error occured along the way")
                userattacks()
        theuserattacksoutcome()
    

#This is where functions needed for when the computer is attacking are defined and used to determine who gets a point
    def computerattacks():
        def userdefend():
            userdefenseinput = input("Would you like to retreat?(Yes or no) ")
            if userdefenseinput.lower() == str("yes"):
                print("You choose to retreat")
                defenseaction = 1
                return defenseaction
            elif userdefenseinput.lower() == str("no"):
                print("You stayed still")
                defenseaction = 0
                return defenseaction
            else:
                print("That is not an option")
                userdefend()
        usermovedefend_action = userdefend()

        def computerattack():
            number = random.randint(1,2)
            if int(number) % 2 == 0:
                print("Your opponent did not swipe")
                computeraction = 0
                return computeraction
            elif int(number) % 2 == 1:
                print("Your opponent swiped")
                computeraction = 1
                return computeraction
            else:
                print("Something has gone wrong")
                computerattack()
        computerattack_action = computerattack()

        def theuserdefendsoutcome():
            if usermovedefend_action == 1 and computerattack_action == 0:
                print("Only you moved")
                roundwinner = str("none")
                scorekeeping(roundwinner)
                print("User:" + str(alluserscore) + " V. Opponent:" + str(allcomputerscore) + '\n')
                howtowin(alluserscore,allcomputerscore)
                computerattacks()
            elif usermovedefend_action == 1 and computerattack_action == 1:
                print("Your opponent missed! YOU get the point and the chance to attack")
                roundwinner = str("user")
                scorekeeping(roundwinner)
                print("User:" + str(alluserscore) + " V. Opponent:" + str(allcomputerscore) + '\n')
                howtowin(alluserscore,allcomputerscore)
                userattacks()
            elif usermovedefend_action == 0 and computerattack_action == 0:
                print("Nobody moved")
                roundwinner = str("none")
                scorekeeping(roundwinner)
                print("User:" + str(alluserscore) + " V. Opponent:" + str(allcomputerscore) + '\n')
                howtowin(alluserscore,allcomputerscore)
                computerattacks()
            elif usermovedefend_action == 0 and computerattack_action == 1:
                print("Your opponent hit you and got the point")
                roundwinner = str("computer")
                scorekeeping(roundwinner)
                print("User:" + str(alluserscore) + " V. Opponent:" + str(allcomputerscore) + '\n')
                howtowin(alluserscore,allcomputerscore)
                computerattacks()
            else:
                print("An error occured along the way" + '\n')
                computerattacks()
        theuserdefendsoutcome()


    userattacks()
    
thegame()