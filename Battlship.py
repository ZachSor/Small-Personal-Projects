import turtle

import random
import sys
global Sarr




def winningscreen():
    alex = turtle.Turtle()
    alex.pensize(10)
    wn = turtle.Screen()
    wn.screensize(600,400)
    wn.colormode(255)
    #The you
    alex.color("#000000")
    alex.right(180)
    alex.penup()
    alex.forward(450)
    alex.right(90)
    alex.forward(50)
    alex.pendown()
    alex.right(165)
    alex.forward(100)
    alex.left(145)
    alex.forward(100)
    alex.left(180)
    alex.forward(100)
    alex.left(20)
    alex.forward(50)
    alex.left(180)
    alex.forward(50)
    alex.right(90)
    alex.penup()
    alex.forward(30)
    alex.right(90)
    alex.forward(25)
    alex.pendown()
    alex.circle(30)
    alex.left(90)
    alex.penup()
    alex.forward(80)
    alex.left(90)
    alex.forward(20)
    alex.right(180)
    alex.pendown()
    alex.forward(30)
    alex.circle(20,180)
    alex.forward(30)
    alex.penup()
    alex.right(180)
    #The won
    wn.bgcolor("#FFD700")
    alex.forward(50)
    alex.left(90)
    for i in range(3):
        alex.penup()
        alex.forward(30)
        alex.pendown()
        alex.dot(10)
    alex.penup()
    alex.forward(50)
    alex.pensize(30)
    alex.left(105)
    alex.pendown()
    alex.forward(200)
    alex.right(180)
    alex.forward(200)
    alex.left(150)
    alex.forward(200)
    alex.right(150)
    alex.forward(200)
    alex.left(150)
    alex.forward(200)
    alex.right(180)
    alex.forward(40)
    alex.left(30)
    alex.penup()
    alex.forward(100)
    alex.pendown()
    alex.circle(100)
    alex.left(90)
    alex.penup()
    alex.forward(250)
    alex.pendown()
    alex.right(105)
    alex.forward(130)
    alex.left(180)
    alex.forward(180)
    alex.right(150)
    alex.forward(210)
    alex.left(150)
    alex.forward(190)

def losingscreen():
    alex = turtle.Turtle()
    alex.pensize(10)
    wn = turtle.Screen()
    wn.screensize(600,400)
    wn.colormode(255)
    alex.color("#000000")
    alex.right(180)
    alex.penup()
    alex.forward(400)
    alex.right(90)
    alex.forward(50)
    alex.pendown()
    alex.right(165)
    alex.forward(100)
    alex.left(145)
    alex.forward(100)
    alex.left(180)
    alex.forward(100)
    alex.left(20)
    alex.forward(50)
    alex.left(180)
    alex.forward(50)
    alex.right(90)
    alex.penup()
    alex.forward(30)
    alex.right(90)
    alex.forward(25)
    alex.pendown()
    alex.circle(30)
    alex.left(90)
    alex.penup()
    alex.forward(80)
    alex.left(90)
    alex.forward(20)
    alex.right(180)
    alex.pendown()
    alex.forward(30)
    alex.circle(20,180)
    alex.forward(30)
    alex.penup()
    alex.right(180)
    #The lost
    wn.bgcolor("#1E90FF")
    alex.forward(50)
    alex.left(90)
    for i in range(3):
        alex.penup()
        alex.forward(30)
        alex.pendown()
        alex.dot(10)
    alex.penup()
    alex.forward(50)
    alex.pensize(20)
    alex.pendown()
    alex.left(90)
    alex.forward(150)
    alex.left(180)
    alex.forward(150)
    alex.left(90)
    alex.forward(75)
    alex.penup()
    alex.forward(150)
    alex.left(90)
    alex.forward(75)
    alex.pendown()
    alex.circle(75)
    alex.right(90)
    alex.penup()
    alex.forward(80)
    alex.pendown()
    alex.circle(40,-240)
    alex.circle(40,240)
    alex.left(180)
    alex.circle(40,-240)
    alex.circle(40,240)
    alex.right(180)
    alex.penup()
    alex.forward(110)
    alex.pendown()
    alex.right(90)
    alex.forward(75)
    alex.left(180)
    alex.forward(150)
    alex.left(90)
    alex.forward(50)
    alex.right(180)
    alex.forward(100)

def setupArray():
    x = 0
    arr = []
    for i in range(8):
        row = []
        for j in range(7):
           row.append('~')
        arr.append(row)
    return arr
arr = setupArray()
def printArray(arr):
    line0 = "\t"
    for val in range(7):
        line0 += str(val+1)+"\t"
    print(line0)
    for val in range(7):
        line2 = str(val+1)+"\t"
        for val2 in range(7):
            line2 += (str(arr[val][val2])+"\t")
        print(line2)
Darr = setupArray()
Sarr = setupArray()
##printArray(arr) #this prints the first array which keeps track of what you hit
##print("") #this print statement is just to put a space in between the two arrays
##printArray(arr2) #this prints the second array where the boats are
#we only need one boat
def boats():
    global Sarr
    global Darr
    row = -1
    col = -1
    row2 = -1
    row3 = -1
    col2 = -1
    col3 = -1
    while(row-2 < 0 or row + 2 > 6):
        row = random.randint(1, 7)
    while(col-2 < 0 or col + 2 > 6):
        col = random.randint(1, 7)
    orientation = random.randint(1, 2)
    
    if(orientation == 1):
        row2 = row + 1
        row3 = row + 2
        col2 = col
        col3 = col
    else:
        row2 = row
        row3 = row
        col2 = col + 1
        col3 = col + 2
        
    Sarr[row][col] = '[]'
    Sarr[row2][col2] = '[]'
    Sarr[row3][col3] = '[]'
    printArray(Darr)
    print("")

boats()
printArray(Sarr)

maximumattempts = 7
attempt = 0   
correctguesses = 0
while attempt < 7:
    guessrow = int(input("Make a guess where you think the enemy boat is. Row: " ))-1
    guesscol = int(input("Column: "))-1
    if(Sarr[guessrow][guesscol] == '[]'):
        Darr[guessrow][guesscol] = '!'
        printArray(Darr)
        correctguesses += 1
        print(str("Guesses used: " + str(attempt) + "/7"))
        if correctguesses == 3: 
            print("You Win!")
            winningscreen()
            sys.exit()
    elif(Sarr[guessrow][guesscol] == '~'):
        Darr[guessrow][guesscol] = 'X'
        printArray(Darr)
        attempt += 1
        print(str("Guesses used: " + str(attempt) + "/7"))
print(correctguesses)

if correctguesses == 3: 
    print("You Win!")
    winningscreen()
elif correctguesses <= 3:
    if attempt%7 == 0:
        print("You Lose!")
        losingscreen()

wn.exitonclick() 
