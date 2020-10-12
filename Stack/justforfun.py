class Stack:
    mylist = []

    def pushInto(self, ele):
        self.mylist.append(ele)

    def popOut(self):
        if self.mylist:
            self.mylist.pop()
        else:
            print('Underflow')

    def printElements(self):
        print(self.mylist)


stack = Stack()

stack.pushInto(10)
stack.pushInto(20)
stack.popOut()
stack.printElements()
stack.pushInto(10)
stack.popOut()
stack.printElements()
