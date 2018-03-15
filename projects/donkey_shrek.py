#! /usr/local/bin/python3

def simple_repetitions():
    repetitions = int(input("How many times?"))
    count = 0

    while (count < repetitions):
        print("Are we there yet?")
        count += 1

def complex_repetitions():
    repetitions = int(input("How many times?"))
    count = 0

    while (count < repetitions):
        print(count)
        if count % 5 == 0:
            print("No Donkey!")
        elif count % 7 == 0:
            print("You are really getting on my nerves Donkey!")
        else:
            print("Are we there yet?")
        count += 1


simple_repetitions()
print("\n\n\n\n")
complex_repetitions()
