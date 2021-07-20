class BST:
    """
    Implement the Binary Search Tree (BST) data structure.
    """

    class Node:
        """
        Each node of the BST will have data and links to the 
        left and right sub-tree. 
        """

        def __init__(self, data):
            """ 
            Initialize the node to the data provided.  Initially
            the links are unknown so they are set to None.
            """
       
            self.data = data
            self.left = None
            self.right = None

    def __init__(self):
        """
        Initialize an empty BST.
        """
        self.root = None

    def insert(self, data):
        """
        Insert 'data' into the BST.  If the BST
        is empty, then set the root equal to the new 
        node.  Otherwise, use _insert to recursively
        find the location to insert.
        """
        if self.root is None:
            self.root = BST.Node(data)
        else:
            self._insert(data, self.root)  # Start at the root

    ###################
    # Start Problem 1 #
    ###################
    def _insert(self, data, node):
        """
        This function will look for a place to insert a node
        with 'data' inside of it.  The current sub-tree is
        represented by 'node'.  This function is intended to be
        called the first time by the insert function.
        """
        if data < node.data:
            # The data belongs on the left side.
            if node.left is None:
                # We found an empty spot
                node.left = BST.Node(data)
            else:
                # Need to keep looking.  Call _insert
                # recursively on the left sub-tree.
                self._insert(data, node.left)
        else:
            # The data belongs on the right side.
            if node.right is None:
                # We found an empty spot
                node.right = BST.Node(data)
            else:
                # Need to keep looking.  Call _insert
                # recursively on the right sub-tree.
                self._insert(data, node.right)
    
    #################
    # End Problem 1 #
    #################

    def __iter__(self):
        """
        Perform a forward traversal (in order traversal) starting from 
	    the root of the BST.  This is called a generator function.
        This function is called when a loop	is performed:

        for value in my_bst:
            print(value)

        """
        yield from self._traverse_forward(self.root)  # Start at the root
        
    def _traverse_forward(self, node):
        """
        Does a forward traversal (in-order traversal) through the 
        BST.
        """
        if node is not None:
            yield from self._traverse_forward(node.left)
            yield node.data
            yield from self._traverse_forward(node.right)
    
    def get_height(self):
        """
    Determine the height of the BST.  Note that an empty tree
    will have a height of 0 and a tree with one item (root) will
    have a height of 1.
    
    If the tree is empty, then return 0.  Otherwise, call 
    _get_height on the root which will recursively determine the 
    height of the tree.
    """
        if self.root is None:
            return 0
        else:
            return self._get_height(self.root)  # Start at the root

    ###################
    # Start Problem 2 #
    ###################
    def _get_height(self, node):
        """
        Determine the height of the BST.  The height of a sub-tree 
        (represented by 'node') is 1 plus the height of either the 
        left sub-tree or the right sub-tree (whichever one is bigger).

        This function intended to be called the first time by 
        get_height.
        """
        if node is None:
            return 0 
        else:
    
            # Compute the height of each subtree
            lheight = self._get_height(node.left)
            rheight = self._get_height(node.right)
    
            # Use the larger one
            if lheight > rheight :
                return lheight + 1
            else:
                return rheight + 1

    #################
    # End Problem 2 #
    #################

# Sample Test Cases (may not be comprehensive) 
print("\n=========== PROBLEM 1 TESTS ===========")
tree = BST()
tree.insert(5)
tree.insert(3)
tree.insert(7)
tree.insert(4)
tree.insert(10)
tree.insert(1)
tree.insert(6)
for x in tree:
    print(x)  # 1, 3, 4, 5, 6, 7, 10

print("\n=========== PROBLEM 2 TESTS ===========")
print(tree.get_height()) # 3
tree.insert(6)
print(tree.get_height()) # 3
tree.insert(12)
print(tree.get_height()) # 4

