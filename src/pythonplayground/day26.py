"""learn about the wild possibilities to hand over parameters to a function"""


# parameters with default values
def word_printer(number=2, word="Hello"):
    print("\nWord_printer:")
    for i in range(0, number):
        print(f"{i+1}:{word}")


# the use of named and positional parameters
word_printer()
word_printer(1)
word_printer(3, "Hola")
# word_printer(number=5, "Bonjour") # error: positional parameter after named
word_printer(5, word="Bonjour")
word_printer(word="Hei")


# hand over variable function parameters


## iterable unpacking / star-unpacking
def example(a, b, c):
    print(a)
    print(b)
    print(c)


# attention must have as many iterable elements as the function parameters
list_a = [1, 2, 3]

example(a=list_a[0], b=list_a[1], c=list_a[2])  # long version
example(*list_a)  # using star unpacking of an iterable


## function with keyword attributes filled with dictonary unpacking
def dict_parameter(param_a, param_b, param_c):
    print(param_a)
    print(param_b)
    print(param_c)


dictionary_a = {"param_a": 111, "param_b": 222, "param_c": 333}
# ,"param_d" : 444  # attention keys in the dictonary must have the save name as the function parameters

dict_parameter(**dictionary_a)  # using dictoinary unpacking


# function with arbitrary arguments (*args as function parameter)
def number_adder(*args):
    print(args)  # args is a tuple with the arguments

    result = 0

    for item in args:
        result += item

    return result


# give as many arguments to the function. Attention: use integer type here
print(number_adder(1, 2, 3, 4, 5))


# function with a mix of regular parameter and arbitrary arguments (*args as function parameter)
def find_max_value(initial_value=0, *args):
    print(args)

    if not len(args):
        return initial_value

    for item in args:
        if item > initial_value:
            initial_value = item

    return initial_value


print(find_max_value(2, 3, 1, 5, 8, 2, 3, 5))
print(find_max_value())
print(find_max_value(1))



# function with arbitrary keyword arguments (**kwagrs) and a regular argument
def print_user(username, **kwargs):
    print("kwargs:", kwargs) # kwargs becomes a dictionary
    print("Type kwargs:", type(kwargs))

    print("Username:", username)
    print("Name:", kwargs["name"])
    print("Lastname:", kwargs["lastname"])
    print("Age:", kwargs["age"])

print_user("PaulchenPanter", name = "Paul", lastname = "Pille", age = 21 )

# Attention: missing arguments must be handled within the function. Otherwise: KeyError: 'age'.
# print( print_user( name = "Paul", lastname = "Pille" ) )



# and finally the complete overkill → all together
# The order must be:
# regular parameters
# *args
# **kwargs


def log_event(
    event_type,                 # regular argument
    user_id,                    # regular argument
    timestamp=None,             # regular argument with a default
    *tags,                      # *args
    **metadata                  # **kwargs
):
    print(f"Event: {event_type}")
    print(f"User: {user_id}")
    print(f"Timestamp: {timestamp}")
    print(f"Tags: {tags}")
    print(f"Meta IP: {metadata['ip']}")
    print(f"Meta Browser: {metadata['browser']}")


# all data as direct argumwnts
log_event(
    "login", 42,         # regular arguments
    "mobile", "premium", # *args
    ip = "192.168.0.1", browser = "Firefox" # **kwargs
)

# prepare a fictional event data
event_core = ["login", 42]         #
event_tags = ["mobile", "premium"] # environment tags
event_meta = {                     # strukturierte Zusatzdaten
    "ip": "192.168.0.1",
    "browser": "Firefox"
}

# all data as prepared data argumwnts
log_event(
    *event_core,          # unpack list → regular parameters (event_type, user_id)
    "2026-01-15T21:22:23",# timestamp as positional argument
    *event_tags,          # unpack list → *args
    **event_meta          # unpack dict → **kwargs
)
