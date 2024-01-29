from SinglyLinkedList  import LinkedList
import random

ll = LinkedList(1)
# for i in range(10):
#     ll.append(random.randint(1,100))

ll.append(2)
ll.append(3)
ll.append(4)
ll.append(5)
ll.append(6)

# ll.print_list()

def t(node):
    temp = node.head
    while(temp):
        print(temp.value, end="-->")
        temp = temp.next
    print("None")
# t(ll)

def t2(node):
    temp = node.head
    while(temp):
        if temp.next is None:
            print(temp.value)
        temp = temp.next

t2(ll)

def isFound(node,n):
    temp = node.head
    while(temp):
        if temp.value == n:
            print("found", n)
            return
        temp = temp.next
    print("Not Found")

# isFound(ll,12)

