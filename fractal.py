import turtle
import math

t = turtle.Turtle()
t.shape('turtle')

#parameters

i = 10  #maximum number of branches in section
l = 100 #lenght of first branch
s = 30  #angle (direction of the branch)
w = 4   #width of the branches

#setting the turtle up
t.lt(90)

#first branch
t.penup()
t.bk(l)
t.pendown()
t.width(5)
t.fd(l)
t.width(5)

#main function
def draw_tree(l, ite, w):
    l = 0.8*l
    w = 0.9*w
    t.lt(s)
    t.fd(l)
    t.width(w)
    ite +=1
    if ite<i:
        draw_tree(l, ite, w)
    t.width(w)
    t.bk(l)
    t.rt(2*s)
    t.fd(l)
    if ite<=i:
        draw_tree(l, ite, w)
    t.width(w)
    t.bk(l)
    t.lt(s)
    
t.speed(10)
draw_tree(l, 2, w)
