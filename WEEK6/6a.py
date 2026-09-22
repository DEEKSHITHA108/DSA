# STACK USING ARRAY

stack = []

def push_array():
    element = int(input("Enter element: "))
    stack.append(element)
    print("Element pushed")


def pop_array():
    if len(stack) == 0:
        print("Stack Underflow")
    else:
        print("Popped element:", stack.pop())


def peek_array():
    if len(stack) == 0:
        print("Stack is empty")
    else:
        print("Top element:", stack[-1])


def display_array():
    if len(stack) == 0:
        print("Stack is empty")
    else:
        print("Stack elements:", stack)


# -------- Array Menu --------

while True:

    print("\n===== STACK USING ARRAY =====")
    print("1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Display")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        push_array()

    elif choice == 2:
        pop_array()

    elif choice == 3:
        peek_array()

    elif choice == 4:
        display_array()

    elif choice == 5:
        break

    else:
        print("Invalid choice")

# STACK USING LINKED LIST

class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


top = None


def push_linked():
    global top

    element = int(input("Enter element: "))

    new_node = Node(element)

    new_node.next = top
    top = new_node

    print("Element pushed")


def pop_linked():
    global top

    if top is None:
        print("Stack Underflow")

    else:
        print("Popped element:", top.data)
        top = top.next


def peek_linked():

    if top is None:
        print("Stack is empty")

    else:
        print("Top element:", top.data)


def display_linked():

    if top is None:
        print("Stack is empty")

    else:
        temp = top

        print("Stack elements:")

        while temp is not None:
            print(temp.data)
            temp = temp.next


# -------- Linked List Menu --------

while True:

    print("\n===== STACK USING LINKED LIST =====")
    print("1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Display")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        push_linked()

    elif choice == 2:
        pop_linked()

    elif choice == 3:
        peek_linked()

    elif choice == 4:
        display_linked()

    elif choice == 5:
        break

    else:
        print("Invalid choice")