def stringorder(string):
    words = string.split()
    sortedwords = sorted(words, key=len)
    sortedstring = ' '.join(sortedwords)
    return sortedstring
string = input('Enter a string: ')
sortedstring = stringorder(string)
print(sortedstring)

