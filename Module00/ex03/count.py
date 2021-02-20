'''This function displays the sums of upper-case characters, lower-case characters,
punctuation characters and spaces in a given text.
If there is no text passed to the function, the user is prompted to give
one.'''
def text_analyzer(String):

    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lower = "abcdefghijklmnopqrstuvwxyz"
    numbers = "0123456789"
    punctuation = "`-=~!@#$%^&*()_+:><}{][/|\\'.;\",?"
    spaces = " "
    upper_count = 0
    lower_count = 0
    numbers_count = 0
    punctuation_count = 0
    spaces_count = 0

    if len(String) == 0:
        text = input("What is the text to analyze? ")
        for i in text:
            if i in upper:
                upper_count += 1
            elif i in lower:
                lower_count += 1
            elif i in numbers:
                numbers_count += 1
            elif i in punctuation:
                punctuation_count += 1
            elif i in spaces:
                spaces_count += 1

        print(text, "\n\n")
        print(f"Upper Case: {upper_count}\n\
Lower Case: {lower_count}\n\
Numbers: {numbers_count}\n\
Punctuation: {punctuation_count}\n\
Spaces: {spaces_count}")


    else:
        for i in String:
            if i in upper:
                upper_count += 1
            elif i in lower:
                lower_count += 1
            elif i in numbers:
                numbers_count += 1
            elif i in punctuation:
                punctuation_count += 1
            elif i in spaces:
                spaces_count += 1

        print(String, "\n\n")
        print(f"Upper Case: {upper_count}\n\
Lower Case: {lower_count}\n\
Numbers: {numbers_count}\n\
Punctuation: {punctuation_count}\n\
Spaces: {spaces_count}")
