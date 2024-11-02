import turtle  
#set up the windowd required ot run the turtle program
wn = turtle.Screen()
#back ground color that is chosen
wn.bgcolor("light green")
#Title of the window
wn.title = ("Tess & Alex Special Guest")
#Tess turtle color & pensize
tess = turtle.Turtle()
tess.color("hotpink")
tess.pensize(5)
#Alex turtle color & pensize
alex = turtle.Turtle()
alex.color("blue")
alex.pensize(7)
#Richie is a turtle to test the "Tess.left(3645)" equation. 
richie = turtle.Turtle()
richie.color("yellow")
richie.pensize(9)
richie.left(3645)
#Special Guest turtle color and pen size
sg = turtle.Turtle()
sg.color("black")
sg.pensize(2)
#Special Guests movements
sg.forward(50)
sg.left(45)
sg.forward(50)
sg.left(45)
sg.forward(50)
sg.left(45)
sg.forward(50)
sg.left(45)
sg.forward(50)
sg.left(45)
sg.forward(50)
sg.left(45)
sg.forward(50)
sg.left(45)
sg.forward(50)
sg.left(45)

tess.forward(80)
tess.left(120)
tess.forward(80)
tess.left(120)
tess.forward(80)
tess.left(120)

tess.right(180)
tess.forward(80)

alex.forward(50)
alex.left(90)
alex.forward(50)
alex.left(90)
alex.forward(50)
alex.left(90)
alex.forward(50)
alex.left(90)

wn.mainloop()