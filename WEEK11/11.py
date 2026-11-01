size = 10

# Separate Chaining
chain = [[] for i in range(size)]

# Linear Probing
linear = [-1] * size

# Quadratic Probing
quadratic = [-1] * size


def separate_chaining(key):
    index = key % size
    chain[index].append(key)


def linear_probing(key):
    index = key % size

    while linear[index] != -1:
        index = (index + 1) % size

    linear[index] = key


def quadratic_probing(key):
    index = key % size
    i = 0

    while quadratic[(index + i * i) % size] != -1:
        i = i + 1

        if i == size:
            print("Hash table is full")
            return

    index = (index + i * i) % size
    quadratic[index] = key


# Input
n = int(input("Enter number of elements: "))

for i in range(n):
    key = int(input("Enter key: "))

    separate_chaining(key)
    linear_probing(key)
    quadratic_probing(key)


# Display Separate Chaining
print("\nSeparate Chaining:")
for i in range(size):
    print(i, ":", chain[i])


# Display Linear Probing
print("\nLinear Probing:")
for i in range(size):
    print(i, ":", linear[i])


# Display Quadratic Probing
print("\nQuadratic Probing:")
for i in range(size):
    print(i, ":", quadratic[i])