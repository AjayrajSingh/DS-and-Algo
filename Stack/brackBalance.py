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


# [====== Driver ======]
stack = Stack()
brackMap = {
    ')': '(',
    '}': '{',
    ']': '[',
    '(': ')',
    '{': '}',
    '[': ']',
}

eq = 'a + b * ( c + d ) - { ( e + f ) }'
#eq = input('Enter the expression: ')
equation = eq.split(' ')

for char in equation:
    if char is '(' or char is '{' or char is '[':
        stack.pushInto(char)
    elif char is ')' or char is '}' or char is ']':
        try:
            if brackMap[char] is stack.mylist[-1]:
                stack.popOut()
                continue
            else:
                print('>> Not balanced <<')
                exit(0)
        except:
            continue
    else:
        continue

if len(stack.mylist) is 0:
    print('>> Balanced <<')
else:
    print('>> Not balanced <<')
