# Function to push an element onto the stack
def push(x):
    # Append the element 'x' to the stack
    stack.append(x)

# Function to pop the top element from the stack
def pop():
    # Check if the stack is not empty before popping
    if len(stack) > 0:
        # Remove the last element from the stack
        del stack[-1]
    else:
        # If the stack is empty, print an error message
        print('Stack empty')

# Function to peek at the top element of the stack without removing it
def peek():
    # Check if the stack is not empty before peeking
    if len(stack) > 0:
        # Print the last element in the stack (top of the stack)
        print(stack[-1])
    else:
        # If the stack is empty, print an error message
        print('Stack empty')

# Initialize an empty stack
stack = []

# Infinite loop for user interaction
while True:
    # Ask the user for an operation to perform
    y = int(input('Enter 1 for pushing an element\nEnter 2 for popping\nEnter 3 for peek\nEnter 4 to exit: '))
    
    # If user chooses to push an element
    if y == 1:
        # Input the value to push onto the stack
        x = int(input('Enter value to push: '))
        push(x)  # Call the push function
    # If user chooses to pop an element
    elif y == 2:
        pop()  # Call the pop function
    # If user chooses to peek at the top element
    elif y == 3:
        peek()  # Call the peek function
    # If user chooses to exit the loop
    elif y == 4:
        break  # Exit the loop
    # Handle invalid input
    else:
        print('Input invalid')
