# Circular Queue using Array

size = int(input("Enter size of queue: "))

queue = [None] * size
front = -1
rear = -1


def enqueue():
    global front, rear

    if (rear + 1) % size == front:
        print("Queue is full.")
        return

    value = int(input("Enter element: "))

    if front == -1:
        front = 0
        rear = 0
    else:
        rear = (rear + 1) % size

    queue[rear] = value
    print("Element inserted.")


def dequeue():
    global front, rear

    if front == -1:
        print("Queue is empty.")
        return

    value = queue[front]
    print("Deleted element:", value)

    if front == rear:
        front = -1
        rear = -1
    else:
        front = (front + 1) % size


def peek():
    if front == -1:
        print("Queue is empty.")
    else:
        print("Front element:", queue[front])


def display():
    if front == -1:
        print("Queue is empty.")
        return

    print("Queue:", end=" ")

    i = front

    while True:
        print(queue[i], end=" ")

        if i == rear:
            break

        i = (i + 1) % size

    print()


# Menu
while True:
    print("\n===== CIRCULAR QUEUE =====")
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Peek")
    print("4. Display")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        enqueue()

    elif choice == 2:
        dequeue()

    elif choice == 3:
        peek()

    elif choice == 4:
        display()

    elif choice == 5:
        print("Program ended.")
        break

    else:
        print("Invalid choice.")

