balance = 10000
correct_pin = 1234
pin_attempts = 0
max_attempts = 3

def check_pin():
    global pin_attempts
    while pin_attempts < max_attempts:
        pin = int(input("Enter your PIN: "))
        if pin == correct_pin:
            return True
        else:
            pin_attempts += 1
            print(f"Incorrect PIN. Attempts remaining: {max_attempts - pin_attempts}")
    print("Account blocked due to too many incorrect PIN attempts.")
    return False

# Function to display the available balance
def display_balance():
    print(f"Your current balance is {balance}.")

# Function to deposit money
def deposit_money():
    global balance
    amount = int(input("Enter the amount to deposit: "))
    balance += amount
    print(f"Deposit of {amount} successful.")
    display_balance()

# Function to withdraw money
def withdraw_money():
    global balance
    amount = int(input("Enter the amount to withdraw: "))
    if amount > balance:
        print("Insufficient balance.")
    else:
        print("Available notes: 100, 200, 500, 2000")
        selected_notes = [int(x) for x in input("Enter the notes you want to use (separated by space): ").split()]

        # Sort selected notes in descending order to minimize the number of notes used
        selected_notes.sort(reverse=True)

        notes_to_dispense = {}
        remaining_amount = amount
        
        for note in selected_notes:
            if remaining_amount >= note:
                notes_to_dispense[note] = remaining_amount // note
                remaining_amount = remaining_amount % note

        if remaining_amount != 0:
            print("Unable to dispense the exact amount with selected notes.")
        else:
            balance -= amount
            print("Please collect your cash:")
            for note, count in notes_to_dispense.items():
                print(f"{note}: {count} notes")
            display_balance()

# Main program loop
if check_pin():
    while True:
        print("Welcome to the ATM.")
        print("1. Display balance")
        print("2. Deposit money")
        print("3. Withdraw money")
        print("4. Quit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            display_balance()
        elif choice == 2:
            deposit_money()
        elif choice == 3:
            withdraw_money()
        elif choice == 4:
            print("Thank you for using the ATM.")
            break
        else:
            print("Invalid choice.")
else:
    print("Exiting ATM.")
