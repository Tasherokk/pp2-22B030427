import random

print("Hello! What is your name?")
name = str(input())
print()
print("Well,", name, end = '' ", I am thinking of a num")
print()
num = random.randint(1, 20)

guess = 0

while guess != num:
    print("Take a guess.")
    guess = int(input())
    print()
    if guess == num:
        break
    if guess < num:
        print("Your guess is too low.")
    else:
        print("Your guess is too high.")

print("Good job", name, end = '' "! You guessed my num")
