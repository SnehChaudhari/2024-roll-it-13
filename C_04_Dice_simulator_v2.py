import random


# generates a number between 0 and 6
# to simulate a roll of a dice
def roll_die():
    result = random.randint(1, 6)
    return result


# rolls two die and returns total and whether a
# double roll happened
def two_rolls():
    double_score = "no"

    # roll two dice
    roll_1 = roll_die()
    roll_2 = roll_die()

    # check if there is a double score opportunity
    if roll_1 == roll_2:
        double_score = "yes"

    # Find the total points so far
    user_points = roll_1 + roll_2

    # show the user the result
    print(f"Dice 1: {roll_1} \t Dice 2: {roll_2}")

    return user_points, double_score


# main routine starts here

double_points = "no"

how_many = int(input("How many dice? "))

for item in range(0, 5):

    if how_many == 2:
        start_points = two_rolls()
        points = start_points[0]
        double_points = start_points[1]

    else:
        points = roll_die()

    print(f"You have {points} points and a double score of {double_points}")

