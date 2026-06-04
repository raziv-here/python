def addition():
    value1 = float(input("Enter the first number: "))
    value2 = float(input("Enter the second number: "))
    return value1 + value2

def subtraction():
    value1 = float(input("Enter the first number: "))
    value2 = float(input("Enter the second number: "))
    return value1 - value2

def multiplication():
    value1 = float(input("Enter the first number: "))
    value2 = float(input("Enter the second number: "))
    return value1 * value2

def division():
    value1 = float(input("Enter the first number: "))
    value2 = float(input("Enter the second number: "))
    if value2 == 0:
        return "Error: Division by zero is not allowed."
    return value1 / value2

def calculator_menu():
    print("\n******* Welcome to the calculator *******")
    print("1. Jodna Lai 1 thichnu hola")
    print("2. Ghatauna lai 2 thichnu hola")
    print("3. Multiply garna 3 thichnu hola")
    print("4. Divide garna 4 thichnu hola")
    print("Enter 'Q' to quit")

# Main Program Loop
while True:
    calculator_menu() # Displays the menu on every loop
    choice = input("\nChoose an operation (1/2/3/4) or 'Q' to quit: ").strip().upper()
    
    if choice == 'Q':
        print("Exiting the calculator. Sayonara!")
        break  # This actually stops the loop

    if choice == '1':
        print(f"The result of addition is: {addition()}")
    elif choice == '2':
        print(f"The result of subtraction is: {subtraction()}")
    elif choice == '3':
        print(f"The result of multiplication is: {multiplication()}")
    elif choice == '4':
        print(f"The result of division is: {division()}")
    else:
        print("Invalid choice. Please try again.")


