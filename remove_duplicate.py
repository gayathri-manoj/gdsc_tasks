def removeduplicates(array):
    removed = []
    length = len(array)
    for i in range(0, length):
        if i==0 or array[i] != array[i-1]:
            removed.append(array[i])
    return removed
array = []
num = int(input('Enter number of elements: '))
for i in range(0, num):
    element = int(input('Enter integer: '))
    array.append(element)
removed = removeduplicates(array)
print(removed)

