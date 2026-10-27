
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1


class AVLTree:
    # Get height of a node
    def height(self, node):
        if node is None:
            return 0
        return node.height

    # Get balance factor
    def get_balance(self, node):
        if node is None:
            return 0
        return self.height(node.left) - self.height(node.right)

    # Update height of a node
    def update_height(self, node):
        node.height = 1 + max(
            self.height(node.left),
            self.height(node.right)
        )

    # Right rotation
    def right_rotate(self, y):
        x = y.left
        T2 = x.right

        x.right = y
        y.left = T2

        self.update_height(y)
        self.update_height(x)

        return x

    # Left rotation
    def left_rotate(self, x):
        y = x.right
        T2 = y.left

        y.left = x
        x.right = T2

        self.update_height(x)
        self.update_height(y)

        return y

    # Insert a key
    def insert(self, root, key):
        if root is None:
            return Node(key)

        if key < root.key:
            root.left = self.insert(root.left, key)
        elif key > root.key:
            root.right = self.insert(root.right, key)
        else:
            return root  # Duplicate keys are not allowed

        self.update_height(root)
        balance = self.get_balance(root)

        # LL case
        if balance > 1 and key < root.left.key:
            return self.right_rotate(root)

        # RR case
        if balance < -1 and key > root.right.key:
            return self.left_rotate(root)

        # LR case
        if balance > 1 and key > root.left.key:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        # RL case
        if balance < -1 and key < root.right.key:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    # Find the node with minimum key
    def min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    # Delete a key
    def delete(self, root, key):
        if root is None:
            return root

        if key < root.key:
            root.left = self.delete(root.left, key)
        elif key > root.key:
            root.right = self.delete(root.right, key)
        else:
            # Node with zero or one child
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            # Node with two children
            successor = self.min_value_node(root.right)
            root.key = successor.key
            root.right = self.delete(root.right, successor.key)

        if root is None:
            return root

        self.update_height(root)
        balance = self.get_balance(root)

        # LL case
        if balance > 1 and self.get_balance(root.left) >= 0:
            return self.right_rotate(root)

        # LR case
        if balance > 1 and self.get_balance(root.left) < 0:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        # RR case
        if balance < -1 and self.get_balance(root.right) <= 0:
            return self.left_rotate(root)

        # RL case
        if balance < -1 and self.get_balance(root.right) > 0:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    # Search for a key
    def search(self, root, key):
        if root is None or root.key == key:
            return root

        if key < root.key:
            return self.search(root.left, key)

        return self.search(root.right, key)

    # Inorder traversal: Left, Root, Right
    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.key, end=" ")
            self.inorder(root.right)

    # Preorder traversal: Root, Left, Right
    def preorder(self, root):
        if root:
            print(root.key, end=" ")
            self.preorder(root.left)
            self.preorder(root.right)

    # Postorder traversal: Left, Right, Root
    def postorder(self, root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.key, end=" ")

    # Level-order traversal
    def level_order(self, root):
        if root is None:
            print("Tree is empty")
            return

        queue = [root]
        while queue:
            node = queue.pop(0)
            print(node.key, end=" ")

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    # Display tree sideways
    def display(self, root, level=0, prefix="Root: "):
        if root is not None:
            print(" " * (level * 4) + prefix + str(root.key))
            self.display(root.left, level + 1, "L: ")
            self.display(root.right, level + 1, "R: ")


# Main program
tree = AVLTree()
root = None

while True:
    print("\n\n--- AVL TREE OPERATIONS ---")
    print("1. Insert")
    print("2. Delete")
    print("3. Search")
    print("4. Inorder Traversal")
    print("5. Preorder Traversal")
    print("6. Postorder Traversal")
    print("7. Level-order Traversal")
    print("8. Display Tree")
    print("9. Find Minimum")
    print("10. Find Maximum")
    print("11. Height of Tree")
    print("12. Balance Factor of Root")
    print("13. Exit")

    choice = input("Enter your choice: ").strip()

    if choice == "1":
        key = int(input("Enter value to insert: "))
        if tree.search(root, key):
            print("Duplicate values are not allowed.")
        else:
            root = tree.insert(root, key)
            print("Inserted successfully.")

    elif choice == "2":
        key = int(input("Enter value to delete: "))
        if tree.search(root, key):
            root = tree.delete(root, key)
            print("Deleted successfully.")
        else:
            print("Value not found.")

    elif choice == "3":
        key = int(input("Enter value to search: "))
        result = tree.search(root, key)
        if result:
            print("Value found:", result.key)
        else:
            print("Value not found.")

    elif choice == "4":
        print("Inorder:", end=" ")
        tree.inorder(root)
        print()

    elif choice == "5":
        print("Preorder:", end=" ")
        tree.preorder(root)
        print()

    elif choice == "6":
        print("Postorder:", end=" ")
        tree.postorder(root)
        print()

    elif choice == "7":
        print("Level order:", end=" ")
        tree.level_order(root)
        print()

    elif choice == "8":
        tree.display(root)

    elif choice == "9":
        if root is None:
            print("Tree is empty.")
        else:
            print("Minimum value:",
                  tree.min_value_node(root).key)

    elif choice == "10":
        if root is None:
            print("Tree is empty.")
        else:
            current = root
            while current.right:
                current = current.right
            print("Maximum value:", current.key)

    elif choice == "11":
        print("Tree height:", tree.height(root))

    elif choice == "12":
        if root is None:
            print("Tree is empty.")
        else:
            print("Root balance factor:",
                  tree.get_balance(root))

    elif choice == "13":
        print("Exiting program.")
        break

    else:
        print("Invalid choice. Please try again.")
