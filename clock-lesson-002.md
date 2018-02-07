# Procedures and code reuse

## Learning objectives

1. Understand the concept of a function
2. Extracting common code from duplicated sequences
3. Knowing the syntax for function declaration in Python
3. (Optional) API/ABI concepts, consistency in conventions between calls

## Motivation

Start the practical as the beginning of the lesson. Ask the pupils to know design the minutes and hours hand of the clock. Ideally, the pupils will notice the tediousness an error prone process of code duplication. Otherwise, once returned to their seats, ask them what they would do if they needed to get the turtle to draw out 100 clock hands. This should, motivate the idea of code reuse. Talk about time savings complexity and error reduction associated with code reuse.

## Simple procedures

Introduce the python syntax for defining a function, that is:
```python
def func(arg0, arg1, ...):
    body...
    return expr # optional component


# Associated call
func(2, "Hello")
```

Expect some resistance when it comes to arguments and their value? Make the analogy with a chef de cuisine and labelled
boxes of ingredients.

This is a good time to introduce the importance of naming functions, their arguments and variables if the pupils know
about them.

## Practical sample code

The first practical element is to provide a function to draw a filled equilateral triangle. The students need to extract
their old code for the triangle and call it at the call site. Now is a good time to introduce the `fillcolor()`,
`begin_fill()` and `end_fill()` primitives to the class. The second step consists in abstracting away the clock hand
drawing routine. This is more involved as it requires multiple nested function calls, but it shows the benefits of
compositional thinking. A sample solution is:

```python
def draw_filled_triangle(color, length):
    fillcolor(color)
    begin_fill()
    right(90)
    forward(length / 2)
    left(120)
    forward(length)
    left(120)
    forward(length)
    left(120)
    forward(length / 2)
    end_fill()

def draw_hand_shape(head_color, length, head_length):
    pensize(3)
    forward(length)
    draw_filled_triangle(head_color, head_length)
```
