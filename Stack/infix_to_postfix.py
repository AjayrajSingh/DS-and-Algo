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
exp = input('Enter the infix expression: ')
postExp = ''
operators = ['+', '-', '*', '/']
exp = exp.split()

precMap = {
    '+': 1,
    '-': 1,
    '*': 2,
    '/': 2,
    '^': 3,
}

for ele in exp:

    if str(ele).isalnum():
        postExp += str(ele)

    elif ele in operators:
        if len(stack.mylist) is 0:
            stack.pushInto(ele)

        elif str(stack.mylist[-1]) is '(':
            stack.pushInto(ele)

        elif precMap[ele] > precMap[stack.mylist[-1]]:
            stack.pushInto(ele)

        elif precMap[ele] is precMap[stack.mylist[-1]]:
            postExp += str(stack.mylist[-1])
            stack.popOut()
            stack.pushInto(ele)

        elif precMap[ele] < precMap[stack.mylist[-1]]:

            try:
                while precMap[ele] < precMap[stack.mylist[-1]]:
                    postExp += str(stack.mylist[-1])
                    stack.popOut()

            except:
                while not len(stack.mylist) is 0:
                    postExp += str(stack.mylist[-1])
                    stack.popOut()

    elif str(ele) is ')':
        while stack.mylist[-1] is not '(':
            postExp += str(stack.mylist[-1])
            stack.popOut()

        stack.popOut()

    elif str(ele) is '(':
        stack.pushInto(ele)


for _ in range(0, len(stack.mylist)):
    postExp += str(stack.mylist[-1])
    stack.popOut()


print('Postfix Expression:', postExp)
