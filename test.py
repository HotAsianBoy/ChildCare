class Child:
    def child(self, name):
        self.name = name
        self.checked_in = False


class DayCare:
    def daycare(self):
        self.children = []
        self.hourly_rate = 12

    def check_in_child(self, name):
        child = Child(name)
        self.children.append(child)
        child.checked_in = True

    def check_out_child(self, name):
        for child in self.children:
            if child.name == name:
                self.children.remove(child)
                child.checked_in = False
                return True
        return False

    def calculate_charge(self, hours):
        # Assuming $12 per hour per child
        return len(self.children) * self.hourly_rate * hours

    def print_child_list(self):
        print("Children checked into the day-care:")
        for child in self.children:
            print(child.name)


# Main program
day_care = DayCare()


while True:
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

    if choice == "1":
        name = input("Enter the child's name to check-in: ")
        day_care.check_in_child(name)

    elif choice == "2":
        name = input("Enter the child's name to check-out: ")
        if not day_care.check_out_child(name):
            print("Error: Child not found!")

    elif choice == "3":
        hours = int(input("Enter the number of hours: "))
        charges = day_care.calculate_charge(hours)
        print(f"Total charges: ${charges}")

    elif choice == "4":
        day_care.print_child_list()

    elif choice == "5":
        print("End of the day. Exiting program.")

    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
