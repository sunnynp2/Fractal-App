# -*- coding: utf-8 -*-
"""
Created on Tue Aug  3 18:39:25 2021

@author: patel
"""
import numpy as np
import tkinter
from tkinter import *
from turtle import TurtleScreen, RawTurtle, tracer

window = tkinter.Tk()
window.title("Fractal App")

canvas = tkinter.Canvas(master = window, width=500, height = 500,)
canvas.grid(padx=2, pady=2, row=0, column=0, rowspan=10, columnspan=10)

def runTree(ang, iter):
    window2 = tkinter.Toplevel(window)
    window2.title("Tree output")
    canvas2 = tkinter.Canvas(master = window2, width=1000, height = 1000,)
    canvas2.grid(padx=2, pady=2, row=0, column=0, rowspan=10, columnspan=10)
    closeWindow = Button(window2, text='close window', width=30,
             height=5, bd='10', command=window2.destroy)
    
    closeWindow.place(x=150, y=510)
    
    
    tScreen = TurtleScreen(canvas2)
    tScreen.tracer(0)
    draw = RawTurtle(tScreen)
    
    draw.speed(0)   
    angle = ang
    finalIter = iter
    size = 80
    
    draw.ht()
    def drawV(x, y, orient, iteration, length):
        i = iteration
        
        draw.penup()
        draw.goto(x,y)
        draw.setheading(orient)
        
        draw.pendown()
        draw.left(angle / 2)
        draw.forward(length)
        #draw.dot(5,"black")
        draw.penup()
        
        leftx = draw.xcor()
        lefty = draw.ycor()
        leftheading = draw.heading()
        
        draw.goto(x,y)
        
        draw.pendown()
        draw.right(angle)
        draw.forward(length)
        #draw.dot(5,"black")
        draw.penup()
        
        rightx = draw.xcor()
        righty = draw.ycor()
        rightheading = draw.heading()
        
        
        if (i != finalIter and int(length * 0.8) > 3):
            i += 1
            
            drawV(leftx, lefty, leftheading, i, int(length * 0.85))
            drawV(rightx, righty, rightheading, i, int(length * 0.85)) 
    
    drawV(0,0,90,1,size)
    window2.mainloop()

def TreeMenu():
    window2 = tkinter.Toplevel(window)
    window2.title("Tree menu")
    canvas2 = tkinter.Canvas(master = window2, width=500, height = 500,)
    canvas2.grid(padx=2, pady=2, row=0, column=0, rowspan=10, columnspan=10)
    closeWindow = Button(window2, text='close window', width=30,
             height=5, bd='10', command=window2.destroy)
    
    closeWindow.place(x=0, y=100)
    
    angleSlider = Scale(window2, from_=0, to=90,orient=HORIZONTAL)
    angleSlider.place(x=0, y = 210)
    angleSlider.set(20)
    
    iterSlider = Scale(window2, from_=0, to=14,orient=HORIZONTAL)
    iterSlider.place(x=0, y = 250)
    iterSlider.set(12)
    
    def makeTreeButton():
        runTree(angleSlider.get(), iterSlider.get())
    
    makeTree = Button(window2, text='Make Tree', width=30,
              height=5, bd='10', command=makeTreeButton)
    makeTree.place(x=0, y=0)

def runDragon(iter):
    window2 = tkinter.Toplevel(window)
    window2.title("Dragon Curve")
    canvas2 = tkinter.Canvas(master = window2, width=1000, height = 1000,)
    canvas2.grid(padx=2, pady=2, row=0, column=0, rowspan=10, columnspan=10)
    closeWindow = Button(window2, text='close window', width=30,
             height=5, bd='10', command=window2.destroy)
    
    closeWindow.place(x=780, y=590)
    
    length = 3
    startx = 0
    starty = 100
    tScreen = TurtleScreen(canvas2)
    tScreen.tracer(0)
    draw = RawTurtle(tScreen)
    draw.ht()
    draw.speed(0)
    draw.penup()
    draw.goto(startx,starty)
    draw.pendown()
    draw.setheading(90)
    draw.pencolor("green")
    draw.forward(length)
    
    directions = np.array([1])
    iterations = iter
    def fold(array, count):
        if (count < iterations):
            count += 1
            toAppend = fold(array,count)
            return np.concatenate([toAppend, [1], -1 * toAppend[::-1]])
        else:
            #print(array)
            return np.array(array)

    final = fold(directions, 1)
    
    
    for i in final:
        if (i == -1):
            draw.right(90)
            draw.forward(length)
        if (i == 1):
            draw.left(90)
            draw.forward(length)
        tScreen.update()
    
    draw.penup()
    draw.goto(startx,starty)
    draw.pendown()
    draw.setheading(0)
    draw.pencolor("blue")
    draw.forward(length)
    
    
    for i in final:
        if (i == -1):
            draw.right(90)
            draw.forward(length)
        if (i == 1):
            draw.left(90)
            draw.forward(length)
        tScreen.update()       
    draw.penup()     
    draw.goto(startx,starty)
    draw.pendown()
    draw.setheading(270)
    draw.pencolor("purple")
    draw.forward(length)
    
    
    for i in final:
        if (i == -1):
            draw.right(90)
            draw.forward(length)
        if (i == 1):
            draw.left(90)
            draw.forward(length)
        tScreen.update()
    draw.penup()      
    draw.goto(startx,starty)
    draw.pendown()
    draw.setheading(180)
    draw.pencolor("orange")
    draw.forward(length)
    
    for i in final:
        if (i == -1):
            draw.right(90)
            draw.forward(length)
        if (i == 1):
            draw.left(90)
            draw.forward(length)
        tScreen.update()
           
def DragonMenu():
    window2 = tkinter.Toplevel(window)
    window2.title("Dragon menu")
    canvas2 = tkinter.Canvas(master = window2, width=500, height = 500,)
    canvas2.grid(padx=2, pady=2, row=0, column=0, rowspan=10, columnspan=10)
    closeWindow = Button(window2, text='close window', width=30,
             height=5, bd='10', command=window2.destroy)
    
    closeWindow.place(x=0, y=100)
    
    iterSlider = Scale(window2, from_=0, to=16,orient=HORIZONTAL)
    iterSlider.place(x=0, y = 200)
    iterSlider.set(8)
    
    def makeDragonButton():
        runDragon(iterSlider.get())
    
    makeDragon = Button(window2, text='Make Dragon', width=30,
              height=5, bd='10', command=makeDragonButton)
    makeDragon.place(x=0, y=0)

FracTree = Button(window, text='Create a Fractal Tree', width=30,
              height=5, bd='10', command=TreeMenu)
FracTree.place(x=0,y=0)

DragCurve = Button(window, text='Create a Dragon Curve', width=30,
             height=5, bd='10', command=DragonMenu)
DragCurve.place(x=0,y=100)

closeWindow = Button(window, text='Close Window', width=30,
             height=5, bd='10', command=window.destroy)
closeWindow.place(x=0,y=200)





window.mainloop()
