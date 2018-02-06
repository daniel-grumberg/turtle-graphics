#! /usr/local/bin/python3
from turtle import *
from datetime import datetime

mode("logo")
seconds_turtle = Turtle()
seconds_turtle.hideturtle()
minutes_turtle = Turtle()
minutes_turtle.hideturtle()
hours_turtle = Turtle()
hours_turtle.hideturtle()

def draw_hand_shape(hand, head_color, length, head_length):
    hand.forward(length)
    hand.fillcolor(head_color)
    hand.begin_fill()
    hand.right(90)
    hand.forward(head_length / 2)
    hand.left(120)
    hand.forward(head_length)
    hand.left(120)
    hand.forward(head_length)
    hand.left(120)
    hand.forward(head_length / 2)
    hand.end_fill()

def display_clockface(radius):
    tracer(False)
    pensize(7)
    for i in range(60):
        penup()
        forward(radius)
        pendown()
        if i % 5 == 0:
            forward(25)
            back(25)
        else:
            dot(3)
        penup()
        back(radius)
        pendown()
        right(6)

def tick():
    now = datetime.today()
    seconds = now.second + now.microsecond * 0.000001
    minutes = now.minute + seconds / 60
    hours = now.hour + minutes / 60
    for hand in seconds_turtle, minutes_turtle, hours_turtle:
        hand.reset()
    seconds_turtle.setheading(6 * seconds)
    draw_hand_shape(seconds_turtle, 'red', 135, 25)
    minutes_turtle.setheading(6 * minutes)
    draw_hand_shape(minutes_turtle, 'blue', 125, 25)
    hours_turtle.setheading(30 * hours)
    draw_hand_shape(hours_turtle, 'green', 90, 25)
    ontimer(tick, 100)


display_clockface(160)
tick()

done()

