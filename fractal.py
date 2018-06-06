import turtle
import math

t = turtle.Turtle()
t.shape('turtle')

#parameters

i = 10   #maximum number of branches
l = 120 #lenght of tree
s = 30  #angle (direction of the trunk)
w = 6   #width of the branches

#setting the turtle up
t.lt(90)

#first branch
t.penup()
t.bk(l)
t.pendown()
t.width(6)
t.fd(l)
t.width(4)

#main function
def draw_tree(l, level):
    l = 0.8*l
    t.lt(s)
    t.fd(l)
    level +=1
    if level<i:
        draw_tree(l, level)   
    t.bk(l)
    t.rt(2*s)
    t.fd(l)
    if level<=i:
        draw_tree(l, level)
    t.bk(l)
    t.lt(s)
    level -=1
    
t.speed(100)
draw_tree(l,3)
