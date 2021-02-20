'''This programme prints the results of the four elementary mathematical operations
of arithmetic (addition, subtraction, multiplication, division) and the modulo operation. This should be
accomplished by writing a function that takes 2 numbers as parameters and returns 5 values'''

def operations(number1, number2):

    num1, num2 = int(number1), int(number2)



    if num2 == 0:

        add = num1 + num2
        minus = num1 - num2
        times = num1 * num2


        print("Sum:                     ", add)
        print("Product:                 ", times)
        print("Difference:              ", minus)
        print("Quotient:                ", "ERROR (div by zero)")
        print("Remainder:               ", "ERROR (modulo by zero)")

    else:

        add = num1 + num2
        minus = num1 - num2
        times = num1 * num2
        divide = num1 / num2
        remainder = num1 % num2


        print("Sum:			", add)
        print("Product:		", times)
        print("Difference:		", minus)
        print("Quotient:		", divide)
        print("Remainder:		", remainder)


operations(513, 63.1)
