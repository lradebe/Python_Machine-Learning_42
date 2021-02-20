"""This program is supposed to reverse the order of a string, and the case of its
words. If we have more than one argument we have to merge them into a single string and separate each arg by a ’ ’
(space char)."""

def exec(String):

    Caps = " ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890~!@#$%^&*()_+:><}{][/\\|?,\";.'"
    Low = " abcdefghijklmnopqrstuvwxyz1234567890~!@#$%^&*()_+:><}{][/|\\?,"";.'"
    NewString = ""

    for i in String:
        if i in Caps:
            NewString += i.lower()
        elif i in Low:
            NewString += i.upper()

    print(NewString[::-1])
