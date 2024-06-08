contacts = {}

def display_menu():
    print("nContact Book Menu:")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Display All Contacts")
    print("4. Exit")


def add_contact():
    name = input("Enter the contact name: ")
    phone = input("Enter the contact phone number: ") 
    if name in contacts:
        print("This contact name already exists. Please use a different name.")
    else:
        contacts[name] = phone
        print("Contact added successfully!")


def search_contact():
    name = input("Enter the contact name: ")
    if name in contacts:
        print("Phone number:", contacts[name])
    else:
        print("Contact not found!")


def display_contacts():
    if len(contacts) == 0:
        print("No contacts found!")
    else:
        print("All contacts:")
        for name, phone in contacts.items():
            print("Name:", name, "| Phone number:", phone)


def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            search_contact()
        elif choice == "3":
            display_contacts()
        elif choice == "4":
            print("Exiting the program...")
            break
        else:
            print("Invalid choice! Try again.")


if __name__ == "__main__":
    main()
