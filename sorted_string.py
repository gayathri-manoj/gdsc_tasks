def stringorder(string):
    # Split the input string into individual words
    words = string.split()
    
    # Sort the words based on their length using the 'sorted' function
    sortedwords = sorted(words, key=len)
    
    # Join the sorted words back into a single string with spaces in between
    sortedstring = ' '.join(sortedwords)
    
    # Return the sorted string
    return sortedstring

# Take user input for the string
string = input('Enter a string: ')

# Call the function to sort words by length and print the result
sortedstring = stringorder(string)
print(sortedstring)
