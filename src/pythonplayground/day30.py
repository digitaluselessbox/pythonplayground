""" smal tool to calculate BMI """

def user_number_input(question: str) -> int:
    """Function asks user for a number input with a given question string."""

    number_input = ""

    while not number_input.isnumeric():
        number_input = input(f"{question}")

    return int( number_input )


def __main__():
    print("Hello, this tool will caculate your BMI. Give your height and your weight, and the tool will show you your BMI")
    body_height = user_number_input("First we need you height in cm (for example: 178).\n")
    body_weight = user_number_input("Second, we need your weight in kg (for example: 82).\n")

    bmi = body_weight / (body_height/100) ** 2

    print(f"\nHere is the hard truth. Your BMI is: {bmi:4.2f}")

__main__()
