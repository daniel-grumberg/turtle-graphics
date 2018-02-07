#! /usr/local/bin/python3
from turtle import *
from datetime import datetime

mode("logo")
speed(0)

seconds_turtle = Turtle()
minutes_turtle = Turtle()
hours_turtle = Turtle()
writer_turtle = Turtle()
old_day = -1

def draw_filled_triangle(hand, color, length):
    hand.fillcolor(color)
    hand.begin_fill()
    hand.right(90)
    hand.forward(length / 2)
    hand.left(120)
    hand.forward(length)
    hand.left(120)
    hand.forward(length)
    hand.left(120)
    hand.forward(length / 2)
    hand.end_fill()

def draw_hand_shape(hand, head_color, length, head_length):
    hand.pensize(3)
    hand.forward(length)
    draw_filled_triangle(hand, head_color, head_length)


def display_clockface(radius):
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
    hideturtle()

def get_day_of_week_str(now):
    weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    return weekdays[now.weekday()]

def get_date_str(now):
    months = [ "Jan.", "Feb.", "Mar.", "Apr", "May", "Jun.", "Jul.", "Aug", "Sep.", "Oct.", "Nov.", "Dec."]
    return months[now.month - 1] + " " + str(now.day) + " " + str(now.year)

def display_date(now):
    global old_day
    writer_turtle.penup()
    writer_turtle.forward(65)
    day_of_week = get_day_of_week_str(now)
    date_str = get_date_str(now)
    if now.day != old_day:
        writer_turtle.clear()
        writer_turtle.write(day_of_week, align='center', font=('Courier', 14, 'bold'))
    writer_turtle.back(150)
    if now.day != old_day:
        writer_turtle.write(date_str, align='center', font=('Courier', 14, 'bold'))
    writer_turtle.forward(85)
    old_day = now.day

def tick():
    now = datetime.today()
    seconds = now.second
    minutes = now.minute + seconds / 60
    hours = now.hour + minutes / 60
    for turtle in seconds_turtle, minutes_turtle, hours_turtle:
        turtle.reset()

    display_date(now)
    seconds_turtle.setheading(6 * seconds)
    draw_hand_shape(seconds_turtle, 'red', 135, 25)
    minutes_turtle.setheading(6 * minutes)
    draw_hand_shape(minutes_turtle, 'blue', 125, 25)
    hours_turtle.setheading(30 * hours)
    draw_hand_shape(hours_turtle, 'green', 90, 25)
    tracer(False)
    ontimer(tick, 200)

display_clockface(160)
tick()

done()
