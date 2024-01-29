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
                



t1= BST()
t1.insert(2)
t1.insert(1)
t1.insert(3)
print(t1.root.val)
print(t1.root.left.val)
print(t1.root.right.val)
