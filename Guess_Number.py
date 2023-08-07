import random
from  art import logo
print(logo)
print("welcome to the number guessing game!")
print("i am thinking of a number between 1 and 100")
easy_number_of_attempts=10
hard_number_of_attempts=5
turns=0
win=False
random_number= random.randint(1, 101)
def check_answer(ran,choo):
    if choo>ran:
        print("to high!")
    elif choo<ran:
        print(("too low"))
    else:
        print("you win")
        global win
        win=True
correct=True
def set_difficulty():

    choosen_level = input("choose a dificulty.Type 'easy' or 'hard': ")
    if choosen_level=="easy":
        return easy_number_of_attempts
    elif choosen_level=='hard':
       return hard_number_of_attempts

turns=set_difficulty()

print(random_number)
while turns>0 and not win:
    print(f"you have remaining {turns} no of attempts ")
    choosen_number=int(input("guess number: "))
    check_answer(random_number,choosen_number)
    if turns==1 and not  win:
        print("you have run out of guesses")
    elif not win:
        print("guess again")

    turns-=1


