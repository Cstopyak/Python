class Node:
    def __init__(self, valueInput):
        self.value = valueInput
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def push(self, valueInput):
        newNode = Node(valueInput)
        if self.top == None:
            self.top = newNode
        else:
            newNode.next = self.top
            self.top = newNode
        return self

    def pop(self):
        if self.top !=None:
            self.top = self.top.next
        return self

    def display(self):
        runner = self.top
        result = ""
        while runner != None:
            result += f"{runner.value}-->"
            runner = runner.next
        print(result)
        return self



stak1 = Stack()
stak1.push(5).push(12).push(24).push(10).display()
stak1.pop().display()