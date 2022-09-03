class Node:
    def __init__(self, data, next=None):
        self.data = data
        if next is None:
            self.next = None
        else:
            self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def append(self, data):
        p = Node(data)
        if self.head == None:
            self.head = p
        else:
            temp = self.head
            while temp.next != None:
                temp = temp.next
            temp.next = p

    def size(self):
        count = 0
        current_node = self.head
        while (current_node != None):
            count += 1
            current_node = current_node.next
        return count

    def printList(self):
        txt = ''
        p = self.head
        while p != None:
            # print(p.data," ", end = '')
            txt += p.data + ' '
            p = p.next
        return txt

    def removeTail(self):
        if self.isEmpty():
            raise Empty('List is Empty')
        p = self.head
        if p.next == None:
            return p.data
        while p.next != None and p.next.next != None:
            p = p.next
        temp = p.next.data
        p.next = None
        return temp


inp1, inp2 = input('Enter Input (L1,L2) : ').split()

list1 = inp1.split('->')
list2 = inp2.split('->')

L1 = LinkedList()
L2 = LinkedList()

for i in list1:
    L1.append(i)
print(f'L1    : {L1.printList()}')

for i in list2:
    L2.append(i)
print(f'L2    : {L2.printList()}')

mergeList = LinkedList()
mergeList = L1
i = 0
for i in range(L2.size()):
    mergeList.append(L2.removeTail())
print(f'Merge : {mergeList.printList()}')
