# Define the function 'cartons' that calculates the number of different carton sizes needed for 'x' bottles
def cartons(x):
    # Initialize counters for each carton size
    xl = 0  # Extra-large carton (48 bottles)
    l = 0   # Large carton (24 bottles)
    m = 0   # Medium carton (12 bottles)
    s = 0   # Small carton (6 bottles)
    
    # Calculate the number of extra-large cartons (48 bottles) needed
    while x > 48:
        x = x - 48  # Subtract 48 bottles for each extra-large carton
        xl += 1     # Increment the count of extra-large cartons
    
    # Calculate the number of large cartons (24 bottles) needed
    while x > 24:
        x = x - 24  # Subtract 24 bottles for each large carton
        l += 1      # Increment the count of large cartons
    
    # Calculate the number of medium cartons (12 bottles) needed
    while x > 12:
        x = x - 12  # Subtract 12 bottles for each medium carton
        m += 1      # Increment the count of medium cartons
    
    # Calculate the number of small cartons (6 bottles) needed
    while x > 6:
        x = x - 6   # Subtract 6 bottles for each small carton
        s += 1      # Increment the count of small cartons
    if x>0: 
        s+=1        # Increment the small carton count for remaining bottles
    # Print the number of each carton size needed
    print(xl, 'xl', ',', l, 'large', ',', m, 'medium', ',', s, 'small')

# Input the number of bottles from the user
x = int(input('Enter number of bottles: '))

# Call the 'cartons' function with the input value
cartons(x)
