
# Checks that users enter an integer
# that is more than 13
def int_check():

    while True:
        error = "Please enter a number that is 13 or more."

        try:
            response = int(input("Enter a number: "))

            # checks that the number is more than or equal to 13
            if response < 13:
                print(error)
            else:
                return response

        except ValueError:
            print(error)


# main routine goes here
target_score = int_check()
print(target_score)