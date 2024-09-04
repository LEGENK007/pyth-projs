#Guess Game on CLI
from random import randint    

print(" Welcome to the Number Guessing Game!",'\n',
      "I'm thinking of a number between 1 and 100",'\n',
      "You have 5 chances to guess the correct number",'\n','\n',
      "Please select the difficulty level:",'\n',
      "1. Easy (10 chances)",'\n',
      "2. Medium (5 chances)",'\n',
      "3. Hard (3 chances)",'\n')
x = randint(1,100)
diff = int(input(" Enter your choice: "))

if diff > 3:
    diff = int(input(" Please enter your choice between 1, 2 and 3: "))

if diff == 1:
    print(" Great! You have selected the Easy difficulty level.",'\n',
          "Let's start the game!")
    for i in range(1,11):
        y = int(input(" Enter your guess: "))
        if x == y:
            print(" Congratulations! You guessed the correct number in ", i, " attempts.")
            break
        elif x > y:
            print ("Incorrect! The number is greater than ",y)
        else:
            print ("Incorrect! The number is less than ",y)
elif diff == 2:
    print(" Great! You have selected the Medium difficulty level.",'\n',
          "Let's start the game!")
    for i in range(1,6):
        y = int(input(" Enter your guess: "))
        if x == y:
            print(" Congratulations! You guessed the correct number in ", i, " attempts.")
            break
        elif x > y:
            print ("Incorrect! The number is greater than ",y)
        else:
            print ("Incorrect! The number is less than ",y)
elif diff == 3:
    print(" Great! You have selected the Hard difficulty level.",'\n',
          "Let's start the game!")
    for i in range(1,4):
        y = int(input(" Enter your guess: "))
        if x == y:
            print(" Congratulations! You guessed the correct number in ", i, " attempts.")
            break
        elif x > y:
            print ("Incorrect! The number is greater than ",y)
        else:
            print ("Incorrect! The number is less than ",y)


