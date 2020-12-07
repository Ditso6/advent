# Class to help create a tree structure
class TreeNode:

    parent = ""
    children = []

    def __init__(self, parent, children):
        self.parent = parent
        self.children = children

    def add_child(self, child):
        self.children.append(child)


