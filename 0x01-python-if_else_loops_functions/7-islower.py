#!/usr/bin/python3

# islower - function that checks for lowercase character
# Return - True if equals lowercase, otherwise False

def islower(char):
    if (ord(char) > 96 and ord(char) < 123):
        return True
    else:
        False
