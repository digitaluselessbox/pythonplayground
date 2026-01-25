word = "hello"
print(word.upper())                     # HELLO
print("hello".upper())                  # HELLO


word = "HELlo"
print(word.lower())                     # hello
print("HELlo".lower())                  # hello


sentence = "How is the weather today?"
if sentence.startswith("How"):
    print("The sentence is a question.")

if sentence.endswith("?"):
    print("The sentence is definetly a question.")


word = "____Hello.__"
print(word.strip("_."))                 # Hello
print(word.lstrip("_"))                 # Hello.__
print(word.rstrip("_"))                 # ____Hello.


sentence = "How is the weather today?"
print(sentence.rstrip(".!?"))           # How is the weather today


sentence = "How is the, weather today?"
print(sentence.find(","))               # 10
print(sentence.find("!"))               # -1


sentence = "How is the, weather today?"
print(sentence.replace(","," -"))       # How is the - weather today?
print(sentence.replace("e","o"))        # How is tho, woathor today?
