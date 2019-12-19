from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.order = Queue()
    # Insert the given value into the tree
    def insert(self, value):
        # If inserting we must already have a tree/root
        # if value is less than self.value go left, make a new tree/node if empty, otherwise
        # keep going (recursion)
        # if greater than or equal to then go right, make a new tree/node if empty, otherwise
        # keep going.
        if value < self.value:
            if self.left:
                self.left.insert(value)
            else:
                self.left = BinarySearchTree(value)
        else:
            if self.right:
                self.right.insert(value)
            else:
                self.right = BinarySearchTree(value)
        

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # if target == self.value, return it
        # go left or right based on smaller or bigger
        if target == self.value:
            return True
        elif self.left is None and self.right is None:
            return False
        else:
            if self.left and target < self.value:
                return self.left.contains(target)
            if self.right and target > self.value:
                return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        # if right exists, go right
        # otherwise return self.value
        if self.right:
            return self.right.get_max()
        else:
            return self.value

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        cb(self.value)
        if self.left:
            self.left.for_each(cb)
        if self.right:
            self.right.for_each(cb)
        
    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if node == None:
            return

        self.in_order_print(node.left)
        print(node.value)
        self.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        new_node = []
        queue = Queue()
        queue.enqueue(node)
        while queue.size > 0:
            val = queue.dequeue()
            new_node.append(val)
            if val.left:
                queue.enqueue(val.left)
            if val.right:
                queue.enqueue(val.right)
        return new_node


    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        new_node = []
        stack = Stack()
        stack.push(node)

        while stack.size > 0:
            val = stack.pop()
            new_node.append(val.value)
            if val.left:
                stack.push(val.left)
            if val.right:
                stack.push(val.right)
        return new_node

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT
    def pre_order_dft(self, node):
        # visit left 
        #push
        # visit right
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
    #visit all left
    # then visit right
    #push the root to current
    


bst = BinarySearchTree(1)
bst.insert(8)
bst.insert(5)
bst.insert(7)
bst.insert(6)
bst.insert(3)
bst.insert(4)
bst.insert(2)

bft = bst.bft_print(bst)
# for i in bft:
#     print(i.value)

# order = bst.in_order_print(bst)
# for i in order:
#     print(i)

# dft = bst.dft_print(bst)
# for i in dft:
#     print(i)