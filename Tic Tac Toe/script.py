row1 = [" ", " ", " "]
row2 = [" ", " ", " "]
row3 = [" ", " ", " "]


def display(row1, row2, row3):
    print(row1)
    print(row2)
    print(row3)


# result = input("Enter Value: ")
# result_to_num = int(result)
# position = int(input("Choose position: "))


def user_choice():
    choice = 'wrong'
    ideal_range = range(0, 10)
    within_range = False

    while choice.isdigit() == False or within_range == False:
        choice = input("Please enter a number (0-10)")

        if choice.isdigit() == False:
            print("Enter a digit: ")

        if choice.isdigit() == True:
            if int(choice) in ideal_range:
                within_range = True
            else:
                print("Sorry cannot acceptable")
                within_range = False

    return int(choice)


# display(row1, row2, row3)

user_choice()
