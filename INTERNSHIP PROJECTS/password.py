import random
import string

def generate_password(length, upper=True, lower=True, digits=True, symbols=True):
    chars = ''
    if lower: chars += string.ascii_lowercase
    if upper: chars += string.ascii_uppercase
    if digits: chars += string.digits
    if symbols: chars += "!@#$%^&*()_+-=[]{}|;:,.<>?"
    if not chars: chars = string.ascii_letters + string.digits + "!@#$%^&*"
    return ''.join(random.choice(chars) for _ in range(length))

def get_length():
    while True:
        try:
            l = int(input("Password length (min 4): "))
            if l >= 4: return l
            print("Too short.")
        except: print("Invalid input.")

def get_choice():
    print("\nComplexity Options:\n1. Simple\n2. Medium\n3. Strong\n4. Custom")
    while True:
        try:
            c = int(input("Enter choice (1-4): "))
            if c in [1, 2, 3, 4]: return c
            print("Choose 1 to 4.")
        except: print("Invalid input.")

def get_custom():
    def ask(q): return input(q).strip().lower().startswith('y')
    return (
        ask("Include uppercase? (y/n): "),
        ask("Include lowercase? (y/n): "),
        ask("Include numbers? (y/n): "),
        ask("Include symbols? (y/n): ")
    )

def full_mode():
    while True:
        length = get_length()
        choice = get_choice()
        if choice == 1:
            pw = generate_password(length, True, True, True, False)
        elif choice == 2 or choice == 3:
            pw = generate_password(length, True, True, True, True)
        else:
            u, l, d, s = get_custom()
            pw = generate_password(length, u, l, d, s)
        print("\nGenerated Password:\n" + pw)
        again = input("Generate another? (y/n): ").strip().lower()
        if not again.startswith('y'): break

def quick_mode():
    try:
        l = int(input("Password length: "))
        if l < 4: l = 4
    except: l = 8
    print("\nGenerated Password:\n" + generate_password(l))

if __name__ == "__main__":
    mode = input("Choose mode: 1. Full  2. Quick (Enter 1 or 2): ").strip()
    full_mode() if mode != "2" else quick_mode()
