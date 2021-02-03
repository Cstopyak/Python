# # container to store all these nodes

class Node:
    def __init__(self, valueInput):
        self.value = valueInput
        self.next = None


class SLL:
    def __init__(self):
        self.head = None

#     def addToBack(self, valueInput):
#         newnode = Node(valueInput)
#         if self.head == None:    
#             self.head = newnode
#         else:
#             #runner is a variable we use to iterate through the SLL
#             runner = self.head

#             while runner.next != None:
#                 runner = runner.next

#             runner.next = newnode
#         return self

#     def display(self):
#         runner = self.head
#         result = ""
#         while runner != None:
#             result += f"{runner.value}-->"
#             runner = runner.next
#         print(result)
#         return self

#     def contains(self, valueToFind):
#         # HINT: to go from node to node, use a runner
#         if self.head == None:
#             print("no nodes in this list fam")
#             return False
#         else:
#             runner = self.head
#             while runner!= None:
#                 if runner.value == valueToFind:
#                     print("found the value!")
#                     return True
#                 runner = runner.next
#             return False


#     def addFront(self, valueInput):
#         if self.head != None:
#             newnode = Node(valueInput)
#             newnode.next = self.head
#             self.head.prev = newnode
#             self.head= newnode
#             return self

#     def remove_front(self):
#         if self.head != None:
#             self.head = self.head.next
#         return self
    


#     def remove_tail(self):
#         runner = self.head
#     while runner.next.next != None:
#         runner = runner.next
#     runner.next = None
#     return self

# def moveMinToFront(linkList):
#     if linkList.head.value != None:
#         _min = linkList.head
#         runner = linkList.head
#         while runner.next != None:
#             if runner.next.value < _min.value:
#                 _min = runner.next
#             runner = runner.next
#         runner = linkList.head
#         while runner.next != None:
#             if runner.next == _min:
#                 runner.next = runner.next.next
#             if runner.next != None:
#                 runner = runner.next
#         _min.next = linkList.head
#         linkList.head = _min
#     return linkList

#     def moveMinToFront(sllInput):
#     #go from node to node (runner) and check the value at each node and find the minimum value. have before node and min node variables set up
#     minvalue = sllInput.head.value
#     runner = sllInput.head
#     beforNode = None
#     while runner.next != None:
#         if runner.next.value < minvalue:
#             minvalue = runner.next.value
#             minNode = runner.next
#             beforNode = runner
#         runner = runner.next
#     if beforNode != None:
#         beforNode.next = minNode.next
#         minNode.next = sllInput.head
#         sllInput.head = minNode
#     else:
#         print("already got the min in the front fam")
#     return sllInput

sll1 = SLL()
MoveMinToFront(sll1)



def prependVal(sllInput, valToInsert, valToFind):
    if sllInput.head != None:
        runner = sllInput.head
        while runner.next != None:
            if runner.next == valToFind:
                newnode = Node(valToInsert)







sll1.addToBack(5).addToBack(8).addToBack(10).addToBack(20).display()
# sll1.addFront(69).addFront(5).display()
# sll1.addToBack(5).addFront(4). addToBack(8).display()
# sll1.contains(42)
# sll1.remove_front().remove_front().display()
# sll1.remove_tail().display()

n1 = Node(5)
n2 = Node(8)
n3 = Node(10)

head = n1

n1.next = n2
n2.next = n3


