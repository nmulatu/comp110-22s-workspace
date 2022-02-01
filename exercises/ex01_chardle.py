"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730530477"

five_characters: str = str(input("Enter a 5-character word: ")) 

single_character: str = (input("Enter a single character: "))
 
print("Searching for " + single_character + " in " + five_characters)

if five_characters[0] == single_character: 
    print(single_character + " found at index 0")
if five_characters[1] == single_character:
    print(single_character + " found at index 1")
if five_characters[2] == single_character:
    print(single_character + " found at index 2")
if five_characters[3] == single_character:
    print(single_character + " found at index 3")
if five_characters[4] == single_character:
    print(single_character + " found at index 4") 
