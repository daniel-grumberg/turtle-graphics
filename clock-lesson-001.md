# Introduction to Turtle graphics

## Learning objectives

1. Get familiar with the turtle environment
2. Design a simple sequence of instructions
3. Express a simple sequence using Python

## Motivation

To motivate the pupils to learn Python, mention that YouTube is largely programmed in Python. If they are still not
motivated, get the pupils to compute the Fibonacci number sequence by hand for a minute or so. Then figure out who
managed the get the furthest in the sequence, if the class is bad at focusing provide a reward for the top 5. Quickly
enter the code for the sequence and run it. They should realise that manual labour is hopeless against a program.

Introduce the final aim of the project, creating your own analogue clock display!

## Turtles

If the pupils are familiar with Cartesian coordinate systems, present the turtle world as the x-y plane. Otherwise,
present the notion with a grid system.

For now introduce simple commands:
- `penup()` and `pendown()` as a means of controlling whether lines are drawn upon turtle movement or not.
- `forward(dist)` and `back(dist)` as a means to move turtle in the current heading.
- `left(angle)` and `right(angle)` as a means to turn clockwise or anticlockwise.

For the more adventurous pupils wanting to fill in the arrow head like the sample solution:
- `fillcolor(col)` to set the fill colour of the turtle.
- `begin_fill()` and `end_fill()` as markers for polygon markers for filling.
- `pensize(sz)` as a means to change the size of the turtles pen.

## Practical sample code

Get the students to start thinking about the clock and practice problem solving. The aim of this sessions exercise is to
provide a sequence of turtle instructions to draw out the hand of a clock. The key idea linking back to geometry is to
remember that an equilateral triangle has equal angles of 60 degrees.

Below is complete sample solution used in the provided demo program.
```python
pensize(3)
forward(135)
fillcolor(head_color)
begin_fill()
right(90)
forward(25 / 2)
left(120)
forward(25)
left(120)
forward(25)
left(120)
forward(25 / 2)
end_fill()
```
