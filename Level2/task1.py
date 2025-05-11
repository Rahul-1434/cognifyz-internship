import random

target=random.randint(1,100)
while True:
    x=int(input("GUess the number between 1 to 100: "))
    if x==target:
        break
    elif x<target:
        print("Too Low! Try again.")
    else:
        print("Too  High! Try again.")
print("You gussed the correct number :",target)


