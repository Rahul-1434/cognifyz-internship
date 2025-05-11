import random

low=int(input('Enter the starting range: '))
high=int(input("Enter the ending range: "))
target=random.randint(low,high)

while True:
    x=int(input(f"GUess the number between {low} to {high}: "))
    if x==target:
        break
    elif x<target:
        print("Too Low! Try again.")
    else:
        print("Too  High! Try again.")
print("You gussed the correct number :",target)


