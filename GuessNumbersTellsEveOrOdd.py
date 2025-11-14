import random


a = int(input("Enter your first number to guess limitayion: "))
b = int(input("Enter your second number to guess limitayion: "))


n = int(input("How many times you want me to guess? "))

for i in range(0, n):
    guess = random.randrange(a, b)
    if  guess % 2 == 0 :
        print(f"oh, {guess} is a even number.")
        print(guess)
        print("-----------------")
    else:
        print(f"But {guess} is odd.")
        print(guess)
        print("-----------------")
        
print("This is a test from Mobina.")
print("I made another branch guys.")
