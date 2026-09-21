class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
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
            else:
                temp = self.head

                while temp.next is not None:
                    temp = temp.next

                temp.next = new_node
                new_node.prev = temp

        print("Linked list created.")

    # 2. Insert at beginning
    def insert_beginning(self):
        data = int(input("Enter data: "))
        new_node = Node(data)

        new_node.next = self.head

        if self.head is not None:
            self.head.prev = new_node

        self.head = new_node

        print("Node inserted at beginning.")

    # 3. Insert at ending
    def insert_end(self):
        data = int(input("Enter data: "))
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            temp = self.head

            while temp.next is not None:
                temp = temp.next

            temp.next = new_node
            new_node.prev = temp

        print("Node inserted at ending.")

    # 4. Insert at index
    def insert_index(self):
        index = int(input("Enter index: "))
        data = int(input("Enter data: "))

        new_node = Node(data)

        if index == 0:
            new_node.next = self.head

            if self.head is not None:
                self.head.prev = new_node

            self.head = new_node
            print("Node inserted.")
            return

        temp = self.head

        for i in range(index - 1):
            if temp is None:
                print("Invalid index.")
                return
            temp = temp.next

        if temp is None:
            print("Invalid index.")
            return

        new_node.next = temp.next
        new_node.prev = temp

        if temp.next is not None:
            temp.next.prev = new_node

        temp.next = new_node

        print("Node inserted.")

    # 5. Delete by value
    def delete_value(self):
        value = int(input("Enter value to delete: "))

        temp = self.head

        while temp is not None:
            if temp.data == value:

                if temp.prev is not None:
                    temp.prev.next = temp.next
                else:
                    self.head = temp.next

                if temp.next is not None:
                    temp.next.prev = temp.prev

                print("Node deleted.")
                return

            temp = temp.next

        print("Value not found.")

    # 6. Delete first node
    def delete_first(self):
        if self.head is None:
            print("List is empty.")
            return

        self.head = self.head.next

        if self.head is not None:
            self.head.prev = None

        print("First node deleted.")

    # 7. Delete last node
    def delete_last(self):
        if self.head is None:
            print("List is empty.")
            return

        temp = self.head

        while temp.next is not None:
            temp = temp.next

        if temp.prev is None:
            self.head = None
        else:
            temp.prev.next = None

        print("Last node deleted.")

    # 8. Count number of nodes
    def count_nodes(self):
        count = 0
        temp = self.head

        while temp is not None:
            count += 1
            temp = temp.next

        print("Number of nodes:", count)

    # 9. Display / Traverse
    def display(self):
        if self.head is None:
            print("List is empty.")
            return

        temp = self.head

        while temp is not None:
            print(temp.data, end=" <-> ")
            temp = temp.next

        print("None")


# Main program
list1 = DoublyLinkedList()

while True:
    print("\n----- DOUBLY LINKED LIST -----")
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