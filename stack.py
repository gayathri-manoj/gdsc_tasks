def push(x):
    stack.append(x)
def pop():
    if len(stack) > 0:
        del stack[-1]
    else:
        print('Stack empty')
def peek():
    if len(stack) > 0:
        print(stack[-1])
    else:
        print('Stack empty')
stack = []
while True:
    y = int(input('Enter 1 for pushing an element\nEnter 2 for popping\nEnter 3 for peek\nEnter 4 to exit: '))
    if y == 1:
        x = int(input('Enter value to push: '))
        push(x) 
    elif y == 2:
        pop() 
    elif y == 3:
        peek()  
    elif y == 4:
        break 
    else:
        print('Input invalid')
