class Child:
    def __init__(self, name):
        self.name = name
        self.checked_in = False

class DayCare:
    def __init__(self):
        self.children = []

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

    def calculate_charge(self):
        # Assuming $12 per hour per child
        return len(self.children) * 12

    def print_child_list(self):
        for child in self.children:
            print(child.name)

# Main program
day_care = DayCare()

while True:
    print("\nDay Care Menu:")
    print("1. Check-in a child")
    print("2. Check-out a child")
    print("3. Calculate charges")
    print("4. Print child list")
    print("5. End of the day and exit")

    choice = int(input("Enter your choice (1-5): "))

    if choice == "1":
        name = input("Enter the child's name to check-in: ")
        day_care.check_in_child(name)

    elif choice == "2":
        name = input("Enter the child's name to check-out: ")
        if not day_care.check_out_child(name):
            print("Error: Child not found!")

    elif choice == "3":
        charges = day_care.calculate_charge()
        print(f"Total charges: ${charges}")

    elif choice == "4":
        print("Child list:")
        day_care.print_child_list()

    elif choice == "5":
        print("End of the day. Exiting program.")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
