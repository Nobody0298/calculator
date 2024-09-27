from input_handler import take_calculation_inputs, take_choice_input, validate_choice

def inputting():
    while True:
        numbers = take_calculation_inputs()
        if numbers is None:
            continue
    
        print("Select operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")

        choice = take_choice_input("Enter choice (1/2/3/4): ", ['1', '2', '3', '4'])
        validate_choice(int(choice))
        break