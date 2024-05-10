import random


# generates a number between 0 and 6
# to simulate a roll of a dice
def roll_die():
    result = random.randint(1, 6)
    return result


# rolls two dice and returns total and whether
# a double roll happened
def two_rolls():
    double_score = "no"

    # roll two die
    roll_1 = roll_die()
    roll_2 = roll_die()

    # check if there is a double score opportunity
    if roll_1 == roll_2:
        double_score = "yes"

    # Find the total points so far
    user_points = roll_1 + roll_2

    # show the user the result
    print(f"Die 1: {roll_1} \t Die 2: {roll_2}")

    return user_points, double_score


# roll dice for user / computer
def make_move(first="no"):
    if first == "yes":
        start_points = two_rolls()
        points = start_points[0]
        double_points = start_points[1]

        return points, double_points

    else:
        points = roll_die()
        return points


# main routine starts here

print("Press <enter> to begin this round: ")
input()


# retrieve initial user points and double result
print("**** Initial Move Results! *****")

# first move for the user
user_first = make_move("yes")
user_points = user_first[0]
double_score = user_first[1]

# tell user if they are eligible for double points
if double_score == "no":
    double_feedback = ""
else:
    double_feedback = "If you win this round, you gain double points!"

# output initial move results
print(f"You rolled a total of {user_points}.  {double_feedback}")
print()

# first move for computer initial computer points
computer_first = make_move("yes")
computer_points = computer_first[0]
print(f"The computer rolled a total of {computer_points}.")

# loop to continue rolling dice until round has ended
while computer_points <= 13 and user_points <= 13:

    print()
    roll_again = input("Do you want to roll the dice (type 'no' to pass): ")
    if roll_again == "yes":
        user_move = make_move()
        user_points += user_move
        print(f"You rolled a {user_move}.  You now have {user_points} points.")

    print("\nPress <enter> to continue...")
    input()

    if computer_points < 13:
        computer_move = make_move()
        computer_points += computer_move
        print(f"The computer rolled a {computer_move}.  The computer"
              f" now has {computer_points}.")

    print()
    if user_points > computer_points:
        result = "You are ahead."
    else:
        result = "The computer is ahead!"

    print(f"***Round Update****: {result} ")
    print(f"User Score: {user_points} \t | \t Computer Score: {computer_points}")

    if roll_again == "no":
        break

# Round Result
if user_points < computer_points:
    print("Sorry - you lost this round and no points "
          "have been added to your total score.  The computer's score has "
          f"increased by {computer_points} points.")

# currently doesnt include double points
else:
    print(f"Yay!  You won the round and {user_points} points have "
          f"been added to your score")




