class Node:
    def __init__(self,info=None,children=[],parent=None,data = None):
        self.info = data if not info else info
        self.children = children
        self.parent = parent
        self.data = data
    def __str__(self):
        return "info:%s children:%s parent: %s data:%s" % (self.info, self.children, self.parent,self.data)
    def __repr__(self):
        return str(self.info)

class Tree:
    def __init__(self,root=Node()):
        self.root = root

    def __str__(self):
        return self.root



if __name__ == "__main__":
    tree = Tree()
    for i in range(0,10):
        tree.root.children.append(Node(data = i))
    print(tree.root)