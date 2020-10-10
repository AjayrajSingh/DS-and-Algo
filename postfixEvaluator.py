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


operators = ['+', '-', '*', '/', '^']


def evaluate(a, b, operator):
    if operator is '+':
        return a+b
    elif operator is '-':
        return a-b
    elif operator is '*':
        return a*b
    elif operator is '/':
        return a/b
    elif operator is '^':
        return a ^ b


if __name__ == '__main__':
    stack = Stack()
    exp = input('Enter the postfix expression: ')
    exp = exp.strip().split(' ')

    try:
        for element in exp:
            if str(element) in operators:
                stack.mylist[-2] = evaluate(stack.mylist[-2],
                                            stack.mylist[-1], str(element))
                stack.popOut()
            else:
                stack.pushInto(int(element))
    except:
        print('Invailid Expression')

    stack.printElements()
