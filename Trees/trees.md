# Trees
Trees are another type of data structure. Each tree consists of a root node as the Parent node, and the left and right nodes as Child nodes.

## Wait what's a node?
Put simply, a node is just data, it can be text, a number, or anything really.

# Binary Trees
A tree whose elements have at most two children is called a `Binary Tree`. A Binary tree has two children, with the left child having a value **less** than the parent node, and the right child having a vaule **greater** than the parent node.

![](https://github.com/LyrasaurusRose/CSE212Final/blob/d463ecbef4f581417b450cce0bf7e78aa4e2975e/Trees/basicbinarytree.PNG)

## Tricky things to keep in mind
>I've labled a few common terms in the image above, however several terms can refer to one node. For example the **root node** is the **parent node** of the nodes '14' and '37' (those nodes are the root node's **child nodes**). However there is only ever `one` root node.

>A **subtree** is just a grouping of a parent and children nodes. The nodes to the right and left of any parent node form a subtree.

# Adding new values
So, how do we add values to the tree? Let's walk through it on paper first. Remember above that there were two rules to data in our Binary Tree:
* The left child node is less than the parent
* The right child node is greater than the parent

So let's take our tree above and add some values to it.

For example, let's take the value `20`, and do the following:
1. Start at the root node. In this case it's 27.
2. Since 20 is less than 27, we go to the left. 
3. The next node is 14, and 20 is greater than 14, so we go right.
4. The next node is 19, and 20 is greater than 19, so we go right.
5. There is no node to the right of 19. We place 20 there.

![](https://github.com/LyrasaurusRose/CSE212Final/blob/d463ecbef4f581417b450cce0bf7e78aa4e2975e/Trees/addnode.PNG)

# A balancing act
The process above is quite an efficient process. If we used a dynamic array or a linked list containing sorted values, we would have an O(n) operation time as we search for the location we needed to insert the data into the proper sorted position.

By using our binary tree, we can exclude a subtree with each comparison that we make. This ability that the tree has to split it's job in half recursively leads to a performance of O(log n). As such, a sorted, balanced BST performs better than other data structures.

However, you may have noticed that I said the word **balanced**. An **unbalanced** tree looks like a linked list. All the nodes are in a straight line connected to each other. This requires O(n) timing, as we have to traverse every single item in the list, we can't exclude any.

Because of this, we'd need to balance our tree. There are several different algorithms that have been made to balance trees. One of these is AVL (Adelson-Velskii and Landis). An AVL tree is balanced when the height between the subtrees is less than 2.

To practice balancing trees, feel free to look at this website: https://visualgo.net/en/bst

# Recursion
The big 'R' of programming is here. It's called recursion, and a simple explanation is it's when a function calls itself again.

Before we move on, let's look at a simple example of recursion:

```py
def fib(n):

    # Base case or the stopping point
    if (n == 0):
        return 0
    
    # Base case or the stopping point
    if (n == 1 or n == 2):
        return 1
    
    # Recursion function
    else:
        return (fib(n - 1) + fib(n - 2))

# Base code
n = 15;
print("Fibonacci series of 15 numbers is :",end=" ")
 
# for loop to print the fiboancci series.
for i in range(0,n):
    print(fib(i),end=" ")
```
This will give us the output: `Fibonacci series of 15 numbers is : 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377`


In order for us to traverse a BST, we'll have to use recursion. Hopefully the examples will help to shed a bit of light, as it's quite a difficult and confusing concept.

# BST's and Recursion
We'll look at two examples before we start practicing: insertion and traversing trees.
## Inserting values

>Inserting into a BST is a recursive operation. Our smaller problem is that we must insert a value into either the left subtree or the right subtree based on the value. Our base case or stopping point is if there is space to add the node (the subtree is empty), then the correct place has been found and the item can be inserted.

There are three things to keep in mind with the following example:
1. In this example, a node is defined as an object of the class **BST.Node**. The **Node** class contains three things: data (the value), left (pointer to the left node), and right (pointer to the right node).
2. There are two functions. The **insert** function is the one called by the user who wants to insert a value into the tree. This function is used to call the recursive function **_insert** starting at the root node. As a special case, if the root node is empty (none), then we will put the new node in the root without using any recursion.
3. In the **_insert** function, we should identify the base case and the recursive calls to the correct subtrees.
```py
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

def _insert(self, data, node):
	"""
	This function will look for a place to insert a node
	with 'data' inside of it.  The current subtree is
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
			# recursively on the left subtree.
			self._insert(data, node.left)
	elif data >= node.data:
		# The data belongs on the right side.
		if node.right is None:
			# We found an empty spot
			node.right = BST.Node(data)
		else:
			# Need to keep looking.  Call _insert
			# recursively on the right subtree.
			self._insert(data, node.right)
```
## Traversing the tree
We traverse a BST when we want to display all of the data that's in the tree. An in-order traversal will visit each node from smallest to largest. A similair process can be followed to visit each node from the largest to the smallest.

>This is also a recursive process. Our smaller problem is that we must traverse the left subtree of a node, use the current node, and then traverse the right subtree of the node. Our base case or stopping point is if the subtree is empty, then we don't need to recursively traverse anything.

In addition, the following things should be noted about this code:
1. The starting function is called `__iter__`. The use of double underscores in Python means that this function is part of the Python framework. When we write code like for item in collection, the `__iter__` function is called on the collection to get the next item. In our case, the `__iter__` will provide the user the next value in the BST. We call this a generator function.

2. The yield command is used to provide the next value to the for loop. The yield is like a return statement in a function. However, unlike a return, the yield will allow the function to start back where it left off in the function when `__iter__` is called again. If we want delegate the yield operation to another function, the command is modified to be yield from. If a generator function (e.g. `__iter__`) needs to call another function which will yield the result, then we will need to use the yield from keywords.

```py
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
	BST.  If the node that we are given (which is the current
	subtree) exists, then we will keep traversing on the left
	side (thus getting the smaller numbers first), then we will 
	provide the data in the current node, and finally we will 
	traverse on the right side (thus getting the larger numbers last).

	The use of the 'yield' will allow this function to support loops
	like:

	for value in my_bst:
		print(value)

    The keyword 'yield' will return the value for the 'for' loop to
    use.  When the 'for' loop wants to get the next value, the code in
    this function will start back up where the last 'yield' returned a 
    value.  The keyword 'yield from' is used when our generator function
    needs to call another function for which a `yield` will be called.  
    In other words, the `yield` is delegated by the generator function
    to another function.

	This function is intended to be called the first time by 
	the __iter__ function.
	"""
	if node is not None:
		yield from self._traverse_forward(node.left)
		yield node.data
		yield from self._traverse_forward(node.right)
```

# BST in Python
Python does not have a built-in BST class. We have to make our own. However, there are packages that can be installed from other developers that provide implementations of the BST. Here are some common functions that BST's use:
![](https://github.com/LyrasaurusRose/CSE212Final/blob/d463ecbef4f581417b450cce0bf7e78aa4e2975e/Trees/bstoperationtable.png)
# Practice Example
For trees, we will be doing a two part example - the first part, we will be writing code to insert nodes into the tree, and in the second part we will be finding the height of the tree.

We will start with the following base code:
```py
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
 	pass
    
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
        pass

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
```
Your job for the practice problem is to write the `_insert` function. Once it is correct, the tests at the bottom will print out the commented line at the bottom.

[Solution](https://github.com/LyrasaurusRose/CSE212Final/blob/bc88263396a83476340da110f3ef6db7abb37496/Trees/treespractice.py)
# Prove Example
Continue with the code that you have finished earlier. This time we will be working on the `_get_height` function. Your job for this one is to write a function that will figure out recursively which side is the longest, and find the height of the tree.

[Solution](https://github.com/LyrasaurusRose/CSE212Final/blob/bc88263396a83476340da110f3ef6db7abb37496/Trees/treesprove.py)
