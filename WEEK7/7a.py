# ---------------- ARRAY QUEUE ----------------

queue = []

def array_enqueue():
    value = int(input("Enter element: "))
    queue.append(value)
    print("Element inserted.")

def array_dequeue():
    if len(queue) == 0:
        print("Queue is empty.")
    else:
        value = queue.pop(0)
        print("Deleted element:", value)

def array_peek():
    if len(queue) == 0:
        print("Queue is empty.")
    else:
        print("Front element:", queue[0])

def array_display():
    if len(queue) == 0:
        print("Queue is empty.")
    else:
        print("Queue:", queue)


# ---------------- LINKED LIST QUEUE ----------------

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


front = None
rear = None


def linked_enqueue():
    global front, rear

    value = int(input("Enter element: "))
    new_node = Node(value)

    if front is None:
        front = rear = new_node
    else:
        rear.next = new_node
        rear = new_node

    print("Element inserted.")


def linked_dequeue():
    global front, rear

    if front is None:
        print("Queue is empty.")
    else:
        value = front.data
        front = front.next

        if front is None:
            rear = None

        print("Deleted element:", value)


def linked_peek():
    if front is None:
        print("Queue is empty.")
    else:
        print("Front element:", front.data)


def linked_display():
    if front is None:
        print("Queue is empty.")
    else:
        temp = front

        print("Queue:", end=" ")
        while temp is not None:
            print(temp.data, end=" ")
            temp = temp.next
        print()


# ---------------- MAIN MENU ----------------

while True:
    print("\n===== QUEUE MENU =====")
    print("1. Array Queue")
    print("2. Linked List Queue")
    print("3. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        while True:
            print("\n--- Array Queue ---")
            print("1. Enqueue")
            print("2. Dequeue")
            print("3. Peek")
            print("4. Display")
            print("5. Back")

            ch = int(input("Enter your choice: "))

            if ch == 1:
                array_enqueue()
            elif ch == 2:
                array_dequeue()
            elif ch == 3:
                array_peek()
            elif ch == 4:
                array_display()
            elif ch == 5:
                break
            else:
                print("Invalid choice.")

    elif choice == 2:
        while True:
            print("\n--- Linked List Queue ---")
            print("1. Enqueue")
            print("2. Dequeue")
            print("3. Peek")
            print("4. Display")
            print("5. Back")

            ch = int(input("Enter your choice: "))

            if ch == 1:
                linked_enqueue()
            elif ch == 2:
                linked_dequeue()
            elif ch == 3:
                linked_peek()
            elif ch == 4:
                linked_display()
            elif ch == 5:
                break
            else:
                print("Invalid choice.")

    elif choice == 3:
        print("Program ended.")
        break

    else:
        print("Invalid choice.")

