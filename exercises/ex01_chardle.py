"""EX 01 - Chardle - A cute step toward Wordle."""

_author_ = "730294791"

user_word: str = input("Enter a 5-character word: ")
if ((len(user_word)) != 5):
    print("Error: Word must contain 5 characters")
    exit()
user_character: str = input("Enter a single character: ")
if ((len(user_character)) != 1):
    print("Error: Character must be a single character.")
    exit()

print("Searching for " + user_character + " in " + user_word)
count: int = 0

if (user_character == user_word[0]): 
    print(user_character + " found at index 0")
    count = count + 1
if (user_character == user_word[1]): 
    print(user_character + " found at index 1")
    count = count + 1
if (user_character == user_word[2]): 
    print(user_character + " found at index 2")
    count = count + 1
if (user_character == user_word[3]): 
    print(user_character + " found at index 3")
    count = count + 1
if (user_character == user_word[4]): 
    print(user_character + " found at index 4")
    count = count + 1


if (count == 0):
     print("No instances of " + user_character + " found in " + user_word)
if (count == 1):
     print("1 instance of " + user_character + " found in " + user_word)
if (count == 2):
     print(" 2 instances of " + user_character + " found in " + user_word)
if (count == 3):
     print(" 3 instances of " + user_character + " found in " + user_word)
if (count == 4):
     print(" 4 instances of " + user_character + " found in " + user_word)
if (count == 5):
     print(" 5 instances of " + user_character + " found in " + user_word)