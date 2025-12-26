a = [10, 20, 30, 40, 50]

a.append(60)
print("After append:", a)

a.clear()
print("After clear:", a)

a = [10, 20, 30, 40, 50]  # reinitialize

print("Count of 10:", a.count(10))

a.extend([60, 70])
print("After extend:", a)

print("Index of 10:", a.index(10))

a.insert(0, 2)
print("After insert:", a)

print("Pop element:", a.pop(0))
print("After pop:", a)

a.remove(10)
print("After remove:", a)

a.reverse()
print("After reverse:", a)

a.sort()
print("After sort:", a)
