
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

    def print_tree(self):
        spaces = '  ' * self.get_level()
        prefix = spaces + '|__' if self.parent else ""
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.print_tree()


def build_product_tree():
    root_node = TreeNode("Electronics")

    laptop = TreeNode("Laptop")
    laptop.add_child(TreeNode("Mac"))
    laptop.add_child(TreeNode("Surface"))
    laptop.add_child(TreeNode("Think pad"))

    cell_phone = TreeNode("Cell Phone")
    cell_phone.add_child(TreeNode("iPhone"))
    cell_phone.add_child(TreeNode("Google Pixel"))
    cell_phone.add_child(TreeNode("Samsung"))

    tv = TreeNode("TV")
    tv.add_child(TreeNode("Samsung"))
    tv.add_child(TreeNode("LG"))
    tv.add_child(TreeNode("Singer"))

    root_node.add_child(laptop)
    root_node.add_child(cell_phone)
    root_node.add_child(tv)

    return root_node


if __name__ == '__main__':
    root = build_product_tree()
    root.print_tree()
