from os import path, system, name

# global constant variables

ALPHA_LOWER = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
NUMS = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
CHAR = ['~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '-', '=', '{', '}', '[', ']', '\\', '|', ':', ';', '"', '\'', ',', '.', '<', '>', '/', '?', '`', ]
ALPHA_UPPER = []            # will be using lower case letters to convert to upper
for char in ALPHA_LOWER:
    ALPHA_UPPER.append(char.upper())

# getting required info to build a password model
