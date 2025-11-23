import random 
import turtle
import time

number = random.randint(1,10)
guess = input("Guess a number between 1 and 10 : ")
guess = int(guess)

if guess == number :
    print("Congraculations.")
    # t = turtle.Turtle()
    # turtle.bgcolor("green")
    # turtle.title("WINNER !!!")
    # turtle.done()

else: 
    print("LOSER!!!")
    # t = turtle.Turtle()
    # turtle.bgcolor("red")
    # turtle.title("LOSER !!!")
    # turtle.done()



print(f"The correct number : {number}")
for i in range(0,1):
    print("You did it.")
    print("You can do anything.")
