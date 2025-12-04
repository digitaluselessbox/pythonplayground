"""no module just some try, catch exception handling"""

# x = 0
# print(5/x)

import sys
import traceback

try:
    print(5 / 0)
    print("after error")
except ZeroDivisionError:
    print("Division by zero is not allowed!")

print(5)

# FileNotFoundError
try:
    with open("not_existing.txt", "r") as file:
        print(file)
except FileNotFoundError:
    print("File is not available!")


# ZeroDivisionError
try:
    # print(5 / 0)
    with open("not_existing.txt", "r") as file:
        print(file)
except ZeroDivisionError:
    print("Division by zero is not allowed!")
except FileNotFoundError:
    print("File is not available!")


# error in sub parts of a program
def do_something():
    print(5 / 0)


try:
    do_something()
except ZeroDivisionError:
    print("Division by zero is also not allowed in functions!")


# own exception
class InvalidEmailError(Exception):
    pass


def send_mail(mail, subject, content):
    if not "@" in mail:
        raise InvalidEmailError("E-Mail address must contains a @-character!")


try:
    send_mail("novalidmail", "Mail Subject", "Mail content")
except InvalidEmailError:
    print("Please insert a valid e-mail address!")


# finally block
try:
    file = open("src/pythonplayground/example_files/datei.csv", "r")
    print(file)
    print(5 / 0)
except FileNotFoundError:
    print("File is not available!")
except ZeroDivisionError:
    print("Again Devisoion by Zerrroooo!")
finally:
    print("FINALLY!")
    file.close()


try:
    do_something()
except Exception as e:
    print("Fehler")
    # print(e)
    # print(sys.exc_info()[1])
    custom_exception = {
        "message": str(sys.exc_info()[1]),
        "traceback": traceback.format_exception(*sys.exc_info()),
    }

    # send_exception_to_sentry(custom_exception)

    raise  # reraises the exception
