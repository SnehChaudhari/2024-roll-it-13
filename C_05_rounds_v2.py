import random


# generates a number between 0 and 6
# to simulate a roll of a dice
def roll_die():
    roll_result = random.randint(1, 6)
    return roll_result


# rolls two dice and returns total and there was
# a double roll
def two_rolls(who):
    double_score = "no"

    # roll two dice
    roll_1 = roll_die()
    roll_2 = roll_die()

    # check if there is a double score opportunity
    if roll_1 == roll_2:
        double_score = "yes"

    # find the total points so far
    first_points = roll_1 + roll_2

    # show the user the result
    print(f"{who}: {roll_1} & {roll_2} - Total: {first_points}")

    return first_points, double_score


# main routine starts here

# initialise 'pass' variables
user_pass = "no"
computer_pass = "no"

# start round...
print("Press <enter> to begin this round: ")
input()

# get initial dice rolls for user
user_first = two_rolls("User")
user_points = user_first[0]
double_points = user_first[1]

# tell the user if they are eligible for double points
if double_points == "yes":
    print("If you win this round, you gain double points!")

# get initial dice rolls for computer
computer_first = two_rolls("Computer")
computer_points = computer_first[0]

# print(f"The computer rolled a total of {computer_points}.")

# Loop (while both user & computer have <= 13 points)...
while computer_points < 13 and user_points < 13:

    # ask user if they want to roll again, update
    # points & status
    print()
    if user_pass == "no":
        roll_again = input("Do you want to roll the dice (type 'no' to pass): ")
    else:
        roll_again = "no"

    if roll_again == "yes":
        user_move = roll_die()
        user_points += user_move

        # if user goes over 13 points, tell them that they lose and set points to 0
        if user_points > 13:
            print(f"💥💥💥 Oops! You rolled a {user_move} so your total is {user_points}.  "
                  f"Which is over 13 points .💥💥💥")

            # reset user points to zero so that when we update their
            # score at the end of round it is correct.
            user_points = 0

            break

        else:
            print(f"You rolled a {user_move} and have a total score of {user_points}.")

    else:
        # if the user passes, dont let them roll again
        user_pass = "yes"

    # if computer has 10 points or more (and is winning) it should pass
    if computer_points >= 10 and computer_points >= user_points:
        computer_pass = "yes"

    else:
        # roll dice for computer and update computer points
        computer_move = roll_die()
        computer_points += computer_move

        # check computer has not gone over
        if computer_points > 13:
            print(f"💥💥💥The computer rolled a {computer_move}, taking their points"
                  f" to {computer_points}.  This is over 13 points so the computer loses!💥💥💥")
            computer_points = 0
            break

        else:
            print(f"The computer rolled a {computer_move}.  The computer"
                  f" now has {computer_points}.")

    print()
    # tell user if they are winning, losing, or if it's a tie
    if user_points > computer_points:
        result = "🙂🙂🙂 You are ahead. 🙂🙂🙂"
    elif user_points < computer_points:
        result = "😯😯😯 The computer is ahead! 😯😯😯"
    else:
        result = "👀It's currently a tie.👀"

    print(f"{result} \tUser: {user_points} \t | \t Computer: {computer_points}")

    # if both the user and the computer have passed,
    # exit the loop.
    if computer_pass == "yes" and user_pass == "yes":
        break

# outside loop - double user points if they won and are eligible

# show rounds result
print()

if user_points < computer_points:
    print("😢😢😢 Sorry - you lost this round and no points "
          "have been added to your total score.  The computer's score has "
          f"increased by {computer_points} points.😢😢😢")

# currently does not include double points
elif user_points > computer_points:
    # double user points if they are eligible
    if double_points == "yes":
        user_points *= 2

    print(f"you won the round and {user_points} points have "
          f"been added to your score.")

else:
    print(f"The result for this round is a tie.  You and the computer "
          f"have {user_points}.")
