class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    # 1. Create a linked list
    def create(self):
        n = int(input("Enter number of nodes: "))

        for i in range(n):
            data = int(input("Enter data: "))
            new_node = Node(data)

            if self.head is None:
                self.head = new_node
                new_node.next = self.head
            else:
                temp = self.head

                while temp.next != self.head:
                    temp = temp.next

                temp.next = new_node
                new_node.next = self.head

        print("Circular linked list created.")

    # 2. Insert at beginning
    def insert_beginning(self):
        data = int(input("Enter data: "))
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            new_node.next = self.head
        else:
            temp = self.head

            while temp.next != self.head:
                temp = temp.next

            new_node.next = self.head
            temp.next = new_node
            self.head = new_node

        print("Node inserted at beginning.")

    # 3. Insert at ending
    def insert_end(self):
        data = int(input("Enter data: "))
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            new_node.next = self.head
        else:
            temp = self.head

            while temp.next != self.head:
                temp = temp.next

            temp.next = new_node
            new_node.next = self.head

        print("Node inserted at ending.")

    # 4. Insert at index
    def insert_index(self):
        index = int(input("Enter index: "))
        data = int(input("Enter data: "))

        new_node = Node(data)

        if index == 0:
            if self.head is None:
                self.head = new_node
                new_node.next = self.head
            else:
                temp = self.head

                while temp.next != self.head:
                    temp = temp.next

                new_node.next = self.head
                temp.next = new_node
                self.head = new_node

            print("Node inserted.")
            return

        if self.head is None:
            print("Invalid index.")
            return

        temp = self.head

        for i in range(index - 1):
            temp = temp.next

            if temp == self.head:
                print("Invalid index.")
                return

        new_node.next = temp.next
        temp.next = new_node

        print("Node inserted.")

    # 5. Delete by value
    def delete_value(self):
        value = int(input("Enter value to delete: "))

        if self.head is None:
            print("List is empty.")
            return

        # If first node has the value
        if self.head.data == value:

            # Only one node
            if self.head.next == self.head:
                self.head = None
            else:
                temp = self.head

                while temp.next != self.head:
                    temp = temp.next

                temp.next = self.head.next
                self.head = self.head.next

            print("Node deleted.")
            return

        temp = self.head

        while temp.next != self.head:
            if temp.next.data == value:
                temp.next = temp.next.next
                print("Node deleted.")
                return

            temp = temp.next

        print("Value not found.")

    # 6. Delete first node
    def delete_first(self):
        if self.head is None:
            print("List is empty.")
            return

        if self.head.next == self.head:
            self.head = None
        else:
            temp = self.head

            while temp.next != self.head:
                temp = temp.next

            temp.next = self.head.next
            self.head = self.head.next

        print("First node deleted.")

    # 7. Delete last node
    def delete_last(self):
        if self.head is None:
            print("List is empty.")
            return

        if self.head.next == self.head:
            self.head = None
        else:
            temp = self.head

            while temp.next.next != self.head:
                temp = temp.next

            temp.next = self.head

        print("Last node deleted.")

    # 8. Count number of nodes
    def count_nodes(self):
        if self.head is None:
            print("Number of nodes: 0")
            return

        count = 0
        temp = self.head

        while True:
            count += 1
            temp = temp.next

            if temp == self.head:
                break

        print("Number of nodes:", count)

    # 9. Display / Traverse
    def display(self):
        if self.head is None:
            print("List is empty.")
            return

        temp = self.head

        while True:
            print(temp.data, end=" -> ")
            temp = temp.next

            if temp == self.head:
                break

        print("(back to head)")


# Main program
list1 = CircularLinkedList()

while True:
    print("\n----- CIRCULAR LINKED LIST -----")
    print("1. Create a linked list")
    print("2. Insert at beginning")
    print("3. Insert at ending")
    print("4. Insert at index")
    print("5. Delete by value")
    print("6. Delete first node")
    print("7. Delete last node")
    print("8. Count number of nodes")
    print("9. Display / Traverse")
    print("10. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        list1.create()

    elif choice == 2:
        list1.insert_beginning()

    elif choice == 3:
        list1.insert_end()

    elif choice == 4:
        list1.insert_index()

    elif choice == 5:
        list1.delete_value()

    elif choice == 6:
        list1.delete_first()

    elif choice == 7:
        list1.delete_last()

    elif choice == 8:
        list1.count_nodes()

    elif choice == 9:
        list1.display()

    elif choice == 10:
        print("Program exited.")
        break

    else:
        print("Invalid choice.")