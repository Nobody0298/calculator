from calculator import Calculator
from input_handler import InputHandler

calculator = Calculator()
input_handler = InputHandler()

operations = {
    1: calculator.add,
    2: calculator.subtract,
    3: calculator.multiply,
    4: calculator.divide
}  

while True:
    numbers = input_handler.take_calculation_inputs()
    if numbers is None:
        continue

    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = input_handler.take_choice_input("Enter choice (1/2/3/4): ", ['1', '2', '3', '4'])
    input_handler.validate_choice(int(choice))

    operation = operations.get(int(choice))
    if operation:
        result = numbers[0]
        for num in numbers[1:]:
            result = operation(result, num)
        print("Result:", result)
    else:
        print("Invalid input")

    choice = input_handler.take_choice_input("Do you want to perform another calculation? (yes/no): ", ['yes', 'no'])

    if choice.lower() == "no":
        break
    elif choice.lower() == "yes":
        continue
    