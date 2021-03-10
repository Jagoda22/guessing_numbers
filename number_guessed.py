print("Bienvenido a nuestro juego! \n") 

import random
rand_num = random.randint(1,101)
score = 100

print(f"You have one job: guess a number from 1 to 100. Watch out! More attempts you have, less points you get. \n \nYou have {score} points for the good start. Mucha suerte mi amigo. \n ")

def first_clue(rand_num):
    if rand_num % 2 == 0:
        return "I will help you mi amigo. The number you need to guess is even"
    else:
        return "I will help you mi amigo. The number you need to guess is odd"

print(first_clue(rand_num))

user_num = input("THE NUMBER: ")





