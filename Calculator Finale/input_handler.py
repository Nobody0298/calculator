class InputHandler:
    @staticmethod
    def take_number_input(prompt):
        while True:
            try:
                num = float(input(prompt))
                return num
            except ValueError:
                print("Invalid input. Please enter a numeric value.")

    @staticmethod
    def take_choice_input(prompt, choices):
        while True:
            choice = input(prompt)
            if choice in choices:
                return choice
            else:
                print("Invalid input. Please enter a valid choice.")

    @staticmethod
    def validate_choice(choice):
        if choice < 1 or choice > 4:
            raise ValueError("Invalid choice. Please enter a valid option (1-4).")

    @staticmethod
    def take_calculation_inputs():
        print("Please enter the numbers you want to do calculation with in series.")

        numbers = []

        while True:
            num = InputHandler.take_number_input("Enter a number (or enter '0' to perform calculation): ")
            if num == 0:
                break
            numbers.append(num)

        if len(numbers) < 2:
            print("Insufficient numbers to perform calculation.")
            return None

        return numbers