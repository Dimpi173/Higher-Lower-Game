import high_low_logo
import question
import random
import os


def display_option(choice):
    name = choice["name"]
    description = choice["description"]
    country = choice["country"]
    return f": {name}, {description}, {country}"


def check_answer(guess, follower_1, follower_2):
    if follower_1 < follower_2:
        if guess == "first":
            return False
        else:
            return True
    else:
        if guess == "first":
            return True
        else:
            return False


choice_2 = random.choice(question.data)
win_score = 0
end_game = False
while not end_game:
    choice_1 = choice_2
    choice_2 = random.choice(question.data)
    while choice_1 == choice_2:
        choice_2 = random.choice(question.data)
    print(high_low_logo.first)
    print("\nGuess who has more followers on Instagram.....  \n")
    print(f"Option 1 {display_option(choice_1)}\n")
    print(high_low_logo.vs)
    print(f"Option 2 {display_option(choice_2)}\n")
    follower1 = choice_1["follower_count"]
    follower2 = choice_2["follower_count"]
    user_guess = input("For option first type 'first' or type 'second' : ").lower()
    while user_guess not in ["first", "second"]:
        user_guess = input("For option first type 'first' or type 'second' : ").lower()
    correct_ans = check_answer(user_guess, follower1, follower2)
    os.system('cls')
    if correct_ans:
        win_score += 1
        print(f"\nWON.... Your Score is {win_score}")
    else:
        print(f"\nLOSE.... Your Score is {win_score}")
        end_game = True

print("Good Bye......")
