from SinglyLinkedList  import Node, LinkedList

nl = LinkedList(1)

nl.append(2)
nl.append(3)
nl.append(4)
nl.append(5)
nl.append(6)

# print(nl.length)

# print(int(5/2)+1)
# nl.print_list()

l=int((nl.length /2))
count = 0
temp = nl.head
arr =[]
while temp is not None:

    if count < l:
        temp = temp.next
        count+=1
        continue
    else:
        arr.append(temp.value)
        temp = temp.next
    count+=1

print(arr)

def middle_node(nl):
    l=int((nl.length /2))
    count = 0
    temp = nl.head
    arr =[]
    while temp is not None:
        if count < l:
            temp = temp.next
            count+=1
            continue
        else:
            arr.append(temp.value)
            temp = temp.next
        count+=1

    return arr


print(middle_node(nl))

myList = LinkedList(1)
myList.append(2)
myList.append(3)
myList.append(4)
myList.append(5)
myList.append(6)
myList.append(7)
myList.append(8)

print(middle_node(myList))