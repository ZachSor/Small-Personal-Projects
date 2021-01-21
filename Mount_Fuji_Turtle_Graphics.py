import turtle

import random


alex = turtle.Turtle()
wn = turtle.Screen()
wn.screensize(800,600)


wn.colormode(255)
alex.pensize(3)
wn.bgcolor(124,104,238)

#Components for single shapes
def Triangle(length):
    alex.fillcolor("#000000")
    alex.begin_fill()
    for i in range(3):
        alex.forward(length)
        alex.left(120)
    alex.end_fill()

#Single shapes
def drawMountFuji(xpos, ypos):
    alex.pendown()
    alex.color("#000000")
    alex.fillcolor("#4169E1")
    alex.begin_fill()
    alex.pensize(5)
    alex.left(180)
    alex.forward(400)
    alex.right(180)
    alex.left(15)
    alex.forward(414)
    alex.right(30)
    alex.forward(414)
    alex.right(165)
    alex.forward(400)
    alex.end_fill()
    #Making the snowcap
    alex.penup()
    alex.setpos(0,106.75)
    alex.fillcolor("#FFFFFF")
    alex.begin_fill()
    alex.pendown()
    alex.right(195)
    alex.forward(100)
    alex.right(165)
    alex.forward(190)
    alex.right(165)
    alex.forward(100)
    alex.end_fill()

def drawHorizon():
    alex.color("#000000")
    alex.setpos(0,0)
    alex.pendown()
    alex.left(180)
    alex.forward(500)
    alex.right(180)
    alex.forward(1000)
    alex.left(180)
    alex.forward(500)
    alex.right(180)
    
def drawTree(xpos):
    alex.color("#000000")
    alex.penup()
    alex.setpos(xpos,-200)
    alex.pendown()
    Triangle(20)
    distance = 2.5
    length = 20
    for i in range(20):
        alex.left(180)
        alex.penup()
        alex.forward(distance)
        alex.left(90)
        alex.forward(10)
        alex.left(90)
        alex.pendown()
        length = length + 5
        Triangle(length)

def drawshootingstar(xpos,ypos,length):
    alex.penup()
    alex.setpos(xpos,ypos)
    alex.pendown()
    alex.seth(90)
    alex.color("#FFFFFF")
    alex.pensize(3)
    alex.right(90)
    alex.right(165)
    alex.forward(length)

def drawstars(xpos,ypos):
    alex.penup()
    alex.setpos(xpos,ypos)
    alex.pendown()
    alex.color("#FFFFFF")
    alex.pendown
    alex.pensize(4)
    for i in range(5):
        alex.forward(10)
        alex.right(144)

def drawdarkcloud(xpos,ypos,size):
    alex.color("#A9A9A9")
    alex.penup()
    alex.setpos(xpos,ypos)
    alex.penup
    alex.dot(size)

def drawmedcloud(xpos,ypos,size):
    alex.color("#D3D3D3")
    alex.penup()
    alex.setpos(xpos,ypos)
    alex.penup
    alex.dot(size)

def drawlitecloud(xpos,ypos,size):
    alex.color("#FFFFFF")
    alex.penup()
    alex.setpos(xpos,ypos)
    alex.pendown()
    alex.dot(size)
    alex.penup()
    
#Multiple shapes in respective groups
def drawAllTrees(NTrees):
    for i in range(NTrees):
        xpos = random.randint(-450,450)
        drawTree(xpos)

def drawAllshootingstar(NSstars):
    for i in range(NSstars):
        xpos = random.randint(-400,400)
        ypos = random.randint(375,400)
        length = random.randint(90,120)
        drawshootingstar(xpos,ypos,length)
    alex.penup()

def drawAllstars(nstars):
    for i in range(nstars):
        xpos = random.randint(-400,400)
        ypos = random.randint(150,400)
        drawstars(xpos,ypos)

def drawAlldarkclouds(nclouds):
    for i in range(nclouds):
        xpos = random.randint(-450,450)
        ypos = random.randint(-400,-250)
        size = random.randint(90,100)
        drawdarkcloud(xpos,ypos,size)

def drawAllmedclouds(nclouds):
    for i in range(nclouds):
        xpos = random.randint(-450,450)
        ypos = random.randint(-300,-150)
        size = random.randint(90,100)
        drawmedcloud(xpos,ypos,size)

def drawAllliteclouds(nclouds):
    for i in range(nclouds):
        xpos = random.randint(-450,450)
        ypos = random.randint(-250,-100)
        size = random.randint(90,100)
        drawlitecloud(xpos,ypos,size)


#The entire drawing
drawAlldarkclouds(80)

drawAllmedclouds(45)

drawAllliteclouds(30)

drawHorizon()

drawMountFuji(0,0)
        
drawAllstars(15)

drawAllshootingstar(10)

alex.left(165)

drawAllTrees(7)


wn.exitonclick() 

