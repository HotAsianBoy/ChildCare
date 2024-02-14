choice = 0
Child_Care_Kids_List = []


def drop_off():
    child_name = input("Please enter your child's name: ")
    Child_Care_Kids_List.append(child_name)
    print(f"Success! Little {child_name} has been added to the list!")
    choice = 0


def pick_up():
    child_name = input("Please enter your child's name: ")
    Child_Care_Kids_List.append(child_name)
    Child_Care_Kids_List.remove(child_name)
    print(f"Success! Little {child_name} has been picked up!")
    choice = 0


def calculate_cost():
    child_name = input("Please enter your child's name: ")
    amount_of_hours_charge = input(f"How many hours would you like Little {child_name}"
                                         f" to stay for?:\n ")
    cost


while choice != 5:
    print("-----------------------------------------------------------------------")
    print("Welcome to MGS Childcare")
    print("What would you like to do? Please choose one of the items below")
    print("-----------------------------------------------------------------------")
    print()
    print("1 Drop off a child")
    print("2 Pick up a child")
    print("3 Calculate cost")
    print("4 Print roll")
    print("5 Exit the system")
    print()
    choice = int(input("Enter your choice (number between 1 and 5): "))
    break
print()


if choice == 1:
    drop_off()
    choice = 0
elif choice == 2:
    pick_up()
    choice = 0
elif choice == 3:
    calculate_cost()
    choice = 0
elif choice == 4:
    printRoll()
    choice = 0
else:
    print("Goodbye!")