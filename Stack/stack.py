class Stack:
    mylist = []

    def pushInto(self):
        ele = int(input('Enter an element: '))
        self.mylist.append(ele)

    def popOut(self):
        if self.mylist:
            self.mylist.pop()
        else:
            print('Underflow')

    def printElements(self):
        print(self.mylist)


stack = Stack()
_continue = 'y'
while(_continue == 'y' or _continue == 'Y'):
    print('1. Push\n2. Pop\n3. Print')
    choice = int(input('Enter choice: '))
    if(choice == 1):
        stack.pushInto()
    elif choice == 2:
        stack.popOut()
    elif choice == 3:
        stack.printElements()
    else:
        print('Oops! Wrong selection')
        exit()

    _continue = input('Continue? y/n ')
