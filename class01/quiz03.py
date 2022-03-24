#QUIZ #3
#Name: Chatnatee Khamlue
#ID: 2210113

# Follow the instructions in the comments below. Then upload this file, with your answers, to Omnivox.

# 1. In a new line, with a new command, add a string to this list 
games = ["Gloomhaven", "Radlands", "Ethnos", "Res Arcana", "Spirit Island", "Bloc by Bloc"]
games.append("potato")
print(games)

# 2. Loop through the list and print out all string longer than 7.
for hashbrown in games:
    if len(hashbrown) > 7:
        print(hashbrown)

# 3. Create a function that takes in one number and counts backwards from that number to 0 (printing out each number as it goes)
def uncount():
    bacon = input("Enter a number : ")
    bacon = int(bacon)
    for spam in range(bacon, -1, -1):
     print(spam)

# 4. Create a function that takes in a string and returns a list with every other letter in that string
def letterify():
    ham = input("Enter a word : ")
    for fried_rice in ham:
        print(fried_rice)


# 5. Call the functions you created in questions 3 and 4
uncount()
letterify()