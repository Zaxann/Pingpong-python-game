import turtle
import time
wn = turtle.Screen()
wn.title("Pong by @Belcea Laurentiu")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)
#2 Obiect pt joc
#Jucator 1
jucator_1=turtle.Turtle()
jucator_1.speed(0)
jucator_1.shape("square")
jucator_1.color("blue")
jucator_1.shapesize(stretch_wid=5,stretch_len=1)
jucator_1.penup()
jucator_1.goto(-350, 0)




#Jucator 2
jucator_2=turtle.Turtle()
jucator_2.speed(0)
jucator_2.shape("square")
jucator_2.color("red")
jucator_2.shapesize(stretch_wid=5,stretch_len=1)
jucator_2.penup()
jucator_2.goto(+350, 0)

#Scor metoda
scorjucator_1 = 0
scorjucator_2 = 0

#Minge
minge=turtle.Turtle()
minge.speed(0)
minge.shape("turtle")
minge.color("green")
minge.penup()
minge.goto(0, 0)
minge.dx =0.1
minge.dy = 0.1


#Scor afisaj
scor = turtle.Turtle()
scor.speed(0)
scor.color("white")
scor.penup()
scor.hideturtle()
scor.goto(0, 260)
scor.write("Jucator 1: 0    Jucator 2: 0", align="center", font=("Courier", 24, "normal"))


#Functii

def jucator_1_sus():
    y = jucator_1.ycor()
    y += 20
    jucator_1.sety(y)

def jucator_1_jos():
    y = jucator_1.ycor()
    y -= 20
    jucator_1.sety(y)

def jucator_2_sus():
    y = jucator_2.ycor()
    y += 20
    jucator_2.sety(y)

def jucator_2_jos():
    y = jucator_2.ycor()
    y -= 20
    jucator_2.sety(y)
#Keyboard bind
wn.listen() # asculta de keyboard input
wn.onkeypress(jucator_1_sus, "w")
wn.onkeypress(jucator_1_jos, "s")
wn.onkeypress(jucator_2_sus, "i")
wn.onkeypress(jucator_2_jos, "k")


#Main game loop
while True:
    wn.update() # de fiecare data cand merge loop-ul reseteaza ecranul 

    #Miscam mingea
    minge.setx(minge.xcor() + minge.dx)
    minge.sety(minge.ycor() + minge.dy)

    #Border check
    if minge.ycor() > 290:
        minge.sety(290)
        minge.dy *=-1  # schimbam directia mingi odata ce atinge border-ul de sus
    if minge.ycor() < -290:
        minge.sety(-290)
        minge.dy *=-1  # schimbam directia mingi odata ce atinge border-ul de sus
    if minge.xcor() > 390:
        minge.goto(0, 0)
        minge.dx *=-1  # schimbam directia mingi odata ce atinge border-ul de sus
        scorjucator_1 +=1
        scor.clear()
        scor.write("Jucator 1: {}    Jucator 2: {}".format(scorjucator_1, scorjucator_2), align="center", font=("Courier", 24, "normal"))
    
    if minge.xcor() < -390:
        minge.goto(0, 0)
        minge.dx *=-1  # schimbam directia mingi odata ce atinge border-ul de sus
        scorjucator_2 +=1
        scor.clear()
        scor.write("Jucator 1: {}    Jucator 2: {}".format(scorjucator_1, scorjucator_2), align="center", font=("Courier", 24, "normal"))
            
    #Coliziune jucator 1 si minge
    if (minge.xcor() > 340 and minge.xcor() <350) and (minge.ycor() < jucator_2.ycor()  + 40 and minge.ycor() > jucator_2.ycor() -50):
        minge.setx(340)
        minge.dx *= -1

    if (minge.xcor() < -340 and minge.xcor() >-350) and (minge.ycor() < jucator_1.ycor()  + 40 and minge.ycor() > jucator_1.ycor() -50):
        minge.setx(-340)
        minge.dx *= -1
    if scorjucator_1>=5:
        scor.clear()
        scor.write("Jucator 1 a castigat!", align="center", font=("Courier", 24, "normal"))
        time.sleep(3)
        break
    if scorjucator_2>=5:
        scor.clear()
        scor.write("Jucator 2 a castigat!", align="center", font=("Courier", 24, "normal"))
        time.sleep(3)
        break   