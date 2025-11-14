import random

for i in range(0, 10):
    guess = random.randrange(50,80)
    if guess % 2 == 0 :
        print(f"oh, {guess} is a even number.")
        print(guess)
        print("-----------------")
    else:
        print(f"But {guess} is odd.")
        print(guess)
        print("-----------------")
        print("Comitted!")