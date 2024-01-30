class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
class BST:
    def __init__(self):
        self.root=None
    def insert(self,val):
        new_node=Node(val)
        if self.root is None:
            self.root=new_node
            return True
        cur = self.root
        while(True):
            if cur.val == new_node.val:
                return False
            
            if new_node.val < cur.val:
                if cur.left is None:
                    cur.left=new_node
                    return True
                cur = cur.left
            else:
                if cur.right is None:
                    cur.right = new_node
                    return True
                cur = cur.right
    
    def contains(self,val):
        if self.root == None: 
            return False
        cur = self.root
        while cur:
            if val < cur.val:
                cur = cur.left
            elif val > cur.val:
                cur = cur.right
            else:
                return True
        return False









t1= BST()


# t1.insert(2)
# t1.insert(1)
# t1.insert(3)
# print(t1.root.val)
# print(t1.root.left.val)
# print(t1.root.right.val)

t1.insert(47)
t1.insert(21)
t1.insert(76)
t1.insert(18)
t1.insert(27)
t1.insert(52)
t1.insert(82)

print('BST Contains 27:')
print(t1.contains(27))

print('\nBST Contains 17:')
print(t1.contains(17))
