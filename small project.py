import random

fruits=["apple", "banana", "cherry", "orange"]
computer=random.choice(fruits)
guess=""
while guess !=computer:
    guess = input("choose the right fruit ").lower()
    if guess != computer:
        print("try again")
if guess == computer:        
    print("correct", computer)