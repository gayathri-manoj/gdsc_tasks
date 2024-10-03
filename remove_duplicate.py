# Function to remove duplicates from the array
def removeduplicates(array):
    # Initialize an empty list to store the unique elements
    removed = []
    # Get the length of the array
    length = len(array)
    
    # Loop through each element in the array
    for i in range(0, length):
        # If the current element is not the same as the previous one, add it to the 'removed' list
        # This works because it assumes the array is sorted or consecutive duplicates
        if i==0 or array[i] != array[i-1]:
            removed.append(array[i])
    
    # Return the list with duplicates removed
    return removed

# Initialize an empty list to store user input
array = []

# Get the number of elements to input
num = int(input('Enter number of elements: '))

# Loop to take 'num' number of elements as input from the user
for i in range(0, num):
    # For each iteration, input an integer and append it to the array
    element = int(input('Enter integer: '))
    array.append(element)

# Call the 'removeduplicates' function to remove duplicates from the array
removed = removeduplicates(array)

# Print the resulting list without duplicates
print(removed)
