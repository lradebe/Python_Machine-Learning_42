'''This program checks if a number is odd, even or zero.
The program will accept only one parameter, an integer.'''
def whois(integer):

    num = int(integer)

    if num == 0:
        print("I'm zero.")
    elif num % 2 == 0:
        print("I'm even.")
    elif num % 2 != 0:
        print("I'm odd.")

