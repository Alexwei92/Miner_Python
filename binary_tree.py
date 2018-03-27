
# Define the tree and node
class Tree:
    def __init__(self, cargo, left=None, right=None):
        self.cargo = cargo
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.cargo)

# Print the tree formula
def print_tree(tree):
    if tree is None: return
    print_tree(tree.left)
    print(tree.cargo, end="")
    print_tree(tree.right)

# Print the tree structure
# The most left node is the root, the most right nodes are the leaves
def print_tree_indented(tree, level=0):
    if tree is None: return
    print_tree_indented(tree.right, level+1)
    print("---|" * level + str(tree.cargo))
    print_tree_indented(tree.left, level+1)    