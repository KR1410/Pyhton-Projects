import random

def game_swg(comp,you):
    if comp==you:
        return None
    elif comp== 'snake':
        if you=='water':
            return False
        elif you=='gun':
            return True
    elif comp== 'water':
        if you=='gun':
            return False
        elif you=='snake':
            return True
    elif comp== 'gun':
        if you=='snake':
            return False
        elif you=='water':
            return True

print("computer turn: Snake, Water or Gun ?")
randomint = random.randint(1,3) #returns a random integer from 1 to 3

if randomint == 1:
    comp="snake"
elif randomint == 2:
    comp="water"
else:
    comp="gun"

you = input("enter your choice: ")

result = game_swg(comp,you)

print("computer choice: " + comp)
print("your choice: " + you)

if result==None:
    print("It's a tie")
elif result==False:
    print("you lose")
elif result==True:
    print("Yayy!!!!! you win")
else:
    print("invalid choice")