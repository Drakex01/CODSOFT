contacts = {}

def add_contact():
    name = input("Enter name: ").strip()
    if name in contacts:
        print("Contact already exists.")
        return
    phone = input("Enter phone: ").strip()
    email = input("Enter email: ").strip()
    address = input("Enter address: ").strip()
    contacts[name] = {"phone": phone, "email": email, "address": address}
    print("Contact added.")

def view_contacts():
    if not contacts:
        print("No contacts found.")
        return
    print("\nContact List:")
    for name, info in contacts.items():
        print(f"{name} - {info['phone']}")

def search_contact():
    query = input("Search by name or phone: ").strip().lower()
    found = False
    for name, info in contacts.items():
        if query in name.lower() or query in info['phone']:
            print(f"\nName: {name}\nPhone: {info['phone']}\nEmail: {info['email']}\nAddress: {info['address']}")
            found = True
    if not found:
        print("No matching contact found.")

def update_contact():
    name = input("Enter the name of the contact to update: ").strip()
    if name not in contacts:
        print("Contact not found.")
        return
    print("Leave field blank to keep current value.")
    phone = input(f"New phone ({contacts[name]['phone']}): ").strip()
    email = input(f"New email ({contacts[name]['email']}): ").strip()
    address = input(f"New address ({contacts[name]['address']}): ").strip()
    if phone: contacts[name]['phone'] = phone
    if email: contacts[name]['email'] = email
    if address: contacts[name]['address'] = address
    print("Contact updated.")

def delete_contact():
    name = input("Enter the name to delete: ").strip()
    if name in contacts:
        del contacts[name]
        print("Contact deleted.")
    else:
        print("Contact not found.")

def main():
    while True:
        print("\n--- Contact Book ---")
        print("1. Add Contact")
        print("2. View All Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Choose an option (1-6): ").strip()
        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print("Exiting Contact Book. Goodbye!")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()
