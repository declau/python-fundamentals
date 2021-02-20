from collections import deque


d = deque()

d.append(1)
d.append(2)
d.appendleft(3)

print(d)

d.pop()
print(d)  # removes the last element


d.popleft()  # removes the element on the left side
print(d)

d.clear()  # removes all
print(d)

d.extend([4, 5, 6])  # add multiple elements
print(d)

d.extendleft([3, 2, 1])  # add multiple elements on the left
print(d)

d.rotate(1)
print(d)