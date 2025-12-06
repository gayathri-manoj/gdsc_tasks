def date(x, y):
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    l = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0):
        l[1] = 29  
    count = 0   
    for i in l:
        if x > i:
            x = x - i
            count = count + 1
    print(x, months[count], ',', y)
x = int(input('Enter day number: '))
y = int(input('Enter year: '))
date(x, y)

