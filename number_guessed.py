import random
print("BIENVENIDO A NUESTRO JUEGO! \n")

rand_num = random.randint(1, 11)
score = 100

print(
    f"""You have one job: guess a number from 1 to 10. Watch out! More attempts you have, less points you get. You have maximum four attempts.  
    You have {score} points for the good start. 
    Mucha suerte mi amigo. Let's start!
    """)


def first_clue(rand_num):
    if rand_num % 2 == 0:
        return "Okay, I will help you a little. The number you need to guess is even.\n"
    else:
        return "Okay, I will help you a little. The number you need to guess is odd.\n"


print(first_clue(rand_num))

user_num1 = int(input("THE NUMBER: "))

if user_num1 == rand_num:
    print(
        f"You have a luck! Guessed with the first try. You got {score} points \n")
elif user_num1 > rand_num:
    print(
        f"Sorry darling! The number you are trying to guess is smaller. You have {score -25} points \n ")
else:
    print(
        f"Sorry darling! The number you are trying to guess is bigger. You have {score -25} points \n ")


user_num2 = int(input("SECOND ATTEMPT: "))


if user_num2 == rand_num:
    print(
        f"You have a luck! Guessed with the second try. You got {score} points\n")
elif user_num2 > rand_num:
    print(
        f"The number you are trying to guess is smaller, baby. You have {score -50} points.\n")
else:
    print(
        f"The number you are trying to guess is bigger, baby. You have {score -50} points.\n")

user_num3 = int(input("THIRD ATTEMPT: "))

if user_num3 == rand_num:
    print(
        f"Well done. You guessed with the thirdattempt. You got {score - 75} points\n")
elif user_num3 > rand_num:
    print(
        f"The number you are trying to guess is smaller, baby. You have {score - 75} points\n")
else:
    print(
        f"The number you are trying to guess is bigger, baby. You have {score - 75} points\n")

user_num4 = int(input("FOURTH, LAST ATTEMPT: "))

if user_num4 == rand_num:
    print(f"Enhorabuena! You kept your honour and guessed the number.\n")
elif user_num4 > rand_num:
    print(f"The number you are trying to guess is smaller, baby. You re loosing the game.\n")
else:
    print(f"The number you are trying to guess is bigger, baby. You are losing the game. \n")
