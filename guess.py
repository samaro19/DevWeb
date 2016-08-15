import random
x = input("set boundaries for number. For example 50 for 1 to 50: ")
y = random.randint(1, x)
z = input("what is your guess: ")
while 1 == 1:
    if z == y:
        print("Correct!")
        cs = input("would you like to play again?: ")
        if cs == "yes":
            x = input("set boundaries for number. For example 50 for 1 to 50: ")
            y = random.randint(1, x)
            z = input("what is your guess: ")
        else:
            break
    elif z > y:
        b = random.randint(1, 3)
        if b == 1:
            print("Try a bit lower")
        elif b == 2:
            print("Go lower")
        else:
            print("Lower")
    else:
        b = random.randint(1, 3)
        if b == 1:
            print("Try a bit higher")
        elif b == 2:
            print("Go higher")
        else:
            print("Higher")
    z = input("what is your guess: ")
