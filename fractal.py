import turtle
import math

t = turtle.Turtle()
t.shape('turtle')

#parameters

i = 10   #maximum number of branches
l = 100 #lenght of tree
s = 30  #angle (direction of the trunk)
w = 4   #width of the branches 'missing in function'

#setting the turtle up
t.lt(90)

#first branch
t.penup()
t.bk(l)
t.pendown()
t.width(4)
t.fd(l)
t.width(2)

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
