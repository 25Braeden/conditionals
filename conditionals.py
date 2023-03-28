def conditional(x, y):
    """
    This function checks the values of x and y and returns a string based on the conditions met.
    """
    if x in [3, 4] and y in [1, 2]:
        return "Here"
    elif x in [1, 2]:
        return "Everywhere"
    elif x in [3, 4] and y in [3, 4]:
        return "There"
    
NUMBERS = [1, 2, 3, 4]

a = ()
while a not in NUMBERS:
    try:
        a = int(input("Enter a whole number from 1-4: "))
        if a not in NUMBERS:
            print("Invalid input. Enter a number from 1 and 4")
    except ValueError:
        print("Invalid input. Enter a number between 1 and 4")
b = ()
while b not in NUMBERS:
    try:
        b = int(input("Enter a whole number from 1-4: "))
        if b not in NUMBERS:
            print("Invalid input. Enter a number between 1 and 4")
    except ValueError:
        print("Invalid input. Enter a number between 1 and 4")

print(conditional(a, b))
