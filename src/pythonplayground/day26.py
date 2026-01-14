""" learn about the wild possibilities to hand over parameters to a function """

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
def example(a,b,c):
    print(a)
    print(b)
    print(c)

list_a = [ 1, 2, 3]

example(a = list_a[0], b=list_a[1], c=list_a[2]) # long version
example(*list_a) # using star unpacking of an iterable
