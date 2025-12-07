""" queue and priority queue """

import queue

car_q = queue.Queue()

car_q.put("Mustang")
car_q.put("Cevelle")
car_q.put("Firebird")
car_q.put("Cuda")
car_q.put("GTO")

print(car_q)

print("First get()")
print(car_q.get())
print("---")
print("Second get()")
print(car_q.get())

print("---")
print("while not empty() → get()")
while not car_q.empty():
    print(car_q.get())


print("---")
print("Priority Queue")
print("---")
q_prio = queue.PriorityQueue()

car_q.put((5, "Mustang"))
car_q.put((2, "Cevelle"))
car_q.put((4, "Firebird"))
car_q.put((3, "Cuda"))
car_q.put((1, "GTO"))

print(car_q.get())


# ######### PriorityQueue

example = "A A A A A A A B B B C C C C C C C D D D D D D D D D D D D"

d = {}
for character in example.split(" "):
    if character in d:
        d[character] = d[character]+1
    else:
        d[character] = 1

print(d.items())

chars_queue = queue.PriorityQueue(  )

# loop all dictionary items (item = tupel = ('A', 5) )
# with the loop switch to a tupel with (5 , 'A')
for char, priority in d.items():
    chars_queue.put((-priority, char)) # use minus to "switch" priority

while not chars_queue.empty():
    print(chars_queue.get())
