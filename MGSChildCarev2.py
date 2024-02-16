"""MGS Childcare v2
Fixed loop, and finished the program to drop off,
pick up, calculate costs and print the child roll,
in a simple format."""


def menu():
    choice = ""
    while choice != 5:
        print("What would you like to do?: ")
        print()
        print("1 - Drop off a child.")
        print()
        print("2 - Pick up a child")
        print()
        print("3 - Calculate Cost")
        print()
        print("4 - Print Child Roll/List")
        print()
        print("5 - Exit the system")
        print()
        print("---------------------------------------------")

        choice = input("Enter your choice (Choose between 1-5): ")
        if choice == "1":
            drop_off()
        elif choice == "2":
            pick_up()

        elif choice == "3":
            hours = int(input(f"How many hours would you like your child to stay for?: "))
            print(f"The charge for looking after {len(roll)}) for {hours} hours is $"
                  f"{calc_cost(len(roll), hours):.2f}")

        elif choice == "4":
            print_roll()

        elif choice == "5":
            print("Thank you for choosing MGS Child Care! Goodbye!")

        else:
            print("Invalid input! Please choose a number between 1-5!")


def drop_off():
    name1 = input("What is the name of the child you are dropping off?: ")
    while len(
            name1) < 3:
        name1 = input("Please enter a valid name! No funny business!")
    roll.append(name1)
    print()
    print(f"Success! {name1} was added to the roll!")
    print()


def pick_up():
    name2 = input(input("What is the name of the child you are picking up?: "))
    if name2 in roll:
        roll.remove(name2)
        print(f"Success! {name2} was removed from the roll!")
        print()
    else:
        print(f"{name2} was not found present. Please check your name again!")
        print()


def calc_cost(number, hours2):
    rate = 12.00
    cost = number * hours2 * rate
    return cost


def print_roll():
    print("MGS Daycare children currently present are:")
    for item in roll:
        print(f"\t{item}")
    print()


roll = []

print("---------------------------------------------")
print("Welcome to MGS Childcare!")
print("What would you like to do today? Please choose one of the items below:")
print("---------------------------------------------")
menu()
