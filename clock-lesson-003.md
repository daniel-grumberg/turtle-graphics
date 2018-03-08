# Variables and conditionals

## Learning objectives

1. Learn about variables
2. Learn about conditionals
3. Learn about comparators and boolean logic
4. Learn about standard in and standard out
5. Express simple decision algorithms

## Motivation

Computer systems need to make decisions based on user input. For example, Facebook requires people to be at least 13
years old to register, suppose we are making such a system.

## Variables and I/O

Introduce variables as a way of remembering values. Storing data in a variable is like writing it down on a piece of
paper and putting it in a labelled folder. When we want to _refer_ to it we can just look for the right folder.
Otherwise, how do we know where we put it.

You can now introduce the concept of input. To get information from the user, you can do the following:
```python
age = input("How old are you?")
```

To output the data back out the print builtin function is useful: `print(age)`, it also performs argument casting. Now
is a good time to introduce the concept of string concatenation using the `+` operator. At this point it also good to
talk about the `float`, `int`, and `str` types, type casting needs to be mentioned i.e. using the types constructor as
follows: `"You are " + str(age) + " years old!"`.

## Conditionals and boolean logic

Conditionals can now be introduced. The Python syntax is as follows:

```python
if age < 13:
    print("Sorry you can not register")
elif age >= 25:
    print("Sorry you can not register")
else:
    print("You can now register")
```

Tell them about the comparators that can be used, namely `<`, `<=`, `>`, `>=`, `==`, and `!=`. Code duplication is bad
and we would like to merge disjoint conditions. To this end introduce boolean logic with `not`, `and`, and `or`. We can
now merge two conditions together:

```python
if age < 13 and age >= 25:
    print("Sorry you can not register")
```

## Practical sample code

The students should come up with a script along the following lines:

```python
age = input("How old are you? ")

if age < 13 or age >= 25:
    print("Sorry you are to young to register")
else:
    print("You can now register")
```

The more code-reuse conscious pupils that are adept to use functions as a means of code reuse, could extract the
_predicate_ to its own function:
```python
def can_register(age):
    return age >= 13 and age < 25
```
