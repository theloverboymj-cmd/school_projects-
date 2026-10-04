"""
A simple command-line calculator.

Supports addition, subtraction, multiplication, and division.
Run it with:  python calculator.py
"""


def add(a: float, b: float) -> float:
    return a + b


def subtract(a: float, b: float) -> float:
    return a - b


def multiply(a: float, b: float) -> float:
    return a * b


def divide(a: float, b: float) -> float:
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b


OPERATIONS = {
    "1": ("Add", add, "+"),
    "2": ("Subtract", subtract, "-"),
    "3": ("Multiply", multiply, "*"),
    "4": ("Divide", divide, "/"),
}


def get_number(prompt: str) -> float:
    while True:
        raw = input(prompt).strip()
        try:
            return float(raw)
        except ValueError:
            print(f"  '{raw}' is not a valid number. Try again.")


def get_choice() -> str:
    print("\nSelect an operation:")
    for key, (name, _, _) in OPERATIONS.items():
        print(f"  {key}. {name}")
    print("  q. Quit")

    while True:
        choice = input("Enter choice (1-4 or q): ").strip().lower()
        if choice == "q" or choice in OPERATIONS:
            return choice
        print("  Invalid choice. Please pick 1, 2, 3, 4, or q.")


def main() -> None:
    print("=== Python Calculator ===")
    while True:
        choice = get_choice()
        if choice == "q":
            print("Goodbye!")
            break

        name, func, symbol = OPERATIONS[choice]
        a = get_number("Enter first number:  ")
        b = get_number("Enter second number: ")

        try:
            result = func(a, b)
        except ZeroDivisionError as err:
            print(f"Error: {err}")
            continue

        print(f"Result: {a} {symbol} {b} = {result}")


if __name__ == "__main__":
    main()
