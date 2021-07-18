import random
random_num = random.randint(1,100)
#print(random_num)
chances = 0
while(True):
    guess = int(input("Enter your number: "))
    chances += 1
    if(guess == random_num):
        print(f"you guessed the correct number in {chances} chances")
        break
    elif(guess < random_num):
        print("your guess is smaller")
    else:
        print("your guess is greater")
