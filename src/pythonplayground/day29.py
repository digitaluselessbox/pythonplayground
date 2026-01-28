""" defaultdict """

from collections import defaultdict

def generate():
    print("generate() wurde aufgerufen!")
    return 0

d = defaultdict(generate)

print(d["gibtesnicht"])

d["gibtesnicht"] = d["gibtesnicht"] + 5

print(d)

p = defaultdict(int)

words = ["hello", "Bonjour", "Ola", "hello"]

for word in words:
    p[word] = p[word] + 1

print(p)
