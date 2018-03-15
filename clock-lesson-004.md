# Using loops and conditionals

## Learning objectives

1. Learn about a simple while loop
2. Learn about the modulus operator
3. Refresh on the use of functions
4. (Optional) More powerful iteration concepts such as range based for loops

## Motivation

Code repetition through iteration is useful in providing terseness and abstraction. Say for example we want to write a
program that repeats Shrek's Donkey ("Are we there yet?") phrase as many times as the user requests. Such a program
might look as follows:

```python
repetitions = int(input("How many times?"))

if repetitions == 0:
    pass
elif repetitions == 1:
    print("Are we there yet?")
elif repetitions == 2:
    print("Are we there yet?")
    print("Are we there yet?")
elif repetitions == 3:
    print("Are we there yet?")
    print("Are we there yet?")
    print("Are we there yet?")
...
```

To issues arise from this style of programming, it is tedious and cumbersome, but more importantly we cannot support an
arbitrary number of repetitions (code is finite, numbers are not). How can we express this kind pattern in code?

## The `while` loop

What we really want here is to be able to repeat an operation a specified number of times, the simplest way of
achieving this purpose is through the use of a looping primitive, the `while` loop. The while loop repeats a sequence of
statements until a user-specified condition is met. We can use this to simplify the previous snippet as follows:

```python
repetitions = int(input("How many times?"))
count = 0

while (count < repetitions):
    print("Are we there yet?")
    count += 1
```

Beyond the obvious advantage in length of code, we can now support an arbitrary number of repetitions. Let's now assume
we want to simulate a dialogue with Shrek and every fifth response and seventh response needs to be "No Donkey!" and
"You are really getting on my nerves Donkey!" respectively. We can achieve this using a conditionals we have previously
learned about and a new operator, modulus `%`, that tells us the remainder of long division between two numbers. The
code would now look as follows:

```python
repetitions = int(input("How many times?"))
count = 0

while (count < repetitions):
    if count % 5 == 0:
        print("No Donkey!")
    elif count % 7 == 0:
        print("You are really getting on my nerves Donkey!")
    else:
        print("Are we there yet?")
    count += 1
```

## Practical sample code

It is interesting to put all the previously learnt concepts together in designing a method that will draw a clock face
in the turtle graphics language. To do this we can use the previous concepts as follows:

```python
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
```
