import random

lucky_number=random.randint(1,50)
while True:
    num=int(input("Guess the number(between 1 and 50): "))
    if num<lucky_number:
        print("Too low.")
    elif num>lucky_number:
        print("Too high.")
    else:
        print("Congratulation you guessed it correct.")
        break