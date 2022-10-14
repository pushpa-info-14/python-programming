countries = ["USA", "India", "USA", "China", "India"]
print(countries)

countries_set = set(countries)
print(countries_set)

"""
-Every node has at most 2 child nodes
-Binary Search Tree or BST

-Breadth first search
-Depth first search
    -In order traversal
    -Pre order traversal
    -Post order traversal
    
-Usages
    -Set type of implementation. Ignore duplicates
    -Sorting numbers. Inorder traversal
"""


class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return
        if data < self.data:
            # add data into left subtree
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        else:
            # add data into right subtree
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)

    def in_order_traversal(self):
        elements = []

        # visit left subtree
        if self.left:
            elements += self.left.in_order_traversal()

        # visit base node
        elements.append(self.data)

        # visit right subtree
        if self.right:
            elements += self.right.in_order_traversal()

        return elements

    def pre_order_traversal(self):
        elements = [self.data]

        # visit left subtree
        if self.left:
            elements += self.left.pre_order_traversal()

        # visit right subtree
        if self.right:
            elements += self.right.pre_order_traversal()

        return elements

    def post_order_traversal(self):
        elements = []

        # visit left subtree
        if self.left:
            elements += self.left.post_order_traversal()

        # visit right subtree
        if self.right:
            elements += self.right.post_order_traversal()

        # visit base node
        elements.append(self.data)

        return elements

    def search(self, value):
        if self.data == value:
            return True
        if value < self.data:
            if self.left:
                return self.left.search(value)
        else:
            if self.right:
                return self.right.search(value)
        return False

    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()

    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()

    def calculate_sum(self):
        summation = 0
        if self.left:
            summation += self.left.calculate_sum()
        if self.right:
            summation += self.right.calculate_sum()

        return summation + self.data

    def delete(self, value):
        if value < self.data:
            if self.left:
                self.left = self.left.delete(value)
        elif value > self.data:
            if self.right:
                self.right = self.right.delete(value)
        else:
            # case 1: no child(leaf node)
            if self.left is None and self.right is None:
                return None
            # case 2.1: one child(only right child)
            if self.left is None:
                return self.right
            # case 2.2: one child(only left child)
            if self.right is None:
                return self.left
            # case 3: two children
            """
            Find the min in right subtree           Find the max in left subtree
            Copy the value in targeted node         Copy the value in targeted node
            Delete duplicate from right subtree     Delete duplicate from left subtree
            """
            min_value = self.right.find_min()
            self.data = min_value
            self.right = self.right.delete(min_value)

        return self


def build_tree(elements):
    root = BinarySearchTreeNode(elements[0])

    for i in range(1, len(elements)):
        root.add_child(elements[i])

    return root


if __name__ == "__main__":
    numbers = [15, 12, 27, 7, 14, 20, 23, 88, 5, 8, 13]

    number_tree = build_tree(numbers)
    print("In order traversal  : ", number_tree.in_order_traversal())
    print("Pre order traversal : ", number_tree.pre_order_traversal())
    print("Post order traversal: ", number_tree.post_order_traversal())
    print("Minimum: ", number_tree.find_min())
    print("Maximum: ", number_tree.find_max())
    print("Sum    : ", number_tree.calculate_sum())
    print(number_tree.search(20))  # O(logn)
    print(number_tree.search(21))  # O(logn)

    print("In order traversal after delete 5  : ", number_tree.delete(5).in_order_traversal())
    print("In order traversal after delete 14 : ", number_tree.delete(14).in_order_traversal())
    print("In order traversal after delete 20 : ", number_tree.delete(20).in_order_traversal())
    print("In order traversal after delete 15 : ", number_tree.delete(15).in_order_traversal())

    countries = ["India", "Pakistan", "Germany", "USA", "China", "India", "UK", "USA"]
    country_tree = build_tree(countries)

    print(country_tree.in_order_traversal())
    print("UK is in the list? ", country_tree.search("UK"))
    print("Sweden is in the list? ", country_tree.search("Sweden"))
