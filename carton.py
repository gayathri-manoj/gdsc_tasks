def cartons(x):
    xl = 0 
    l = 0  
    m = 0   
    s = 0   
    while x > 48:
        x = x - 48 
        xl += 1    
    while x > 24:
        x = x - 24  
        l += 1      
    while x > 12:
        x = x - 12  
        m += 1      
    while x > 6:
        x = x - 6   
        s += 1      
    if x>0: 
        s+=1       
    print(xl, 'xl', ',', l, 'large', ',', m, 'medium', ',', s, 'small')
x = int(input('Enter number of bottles: '))
cartons(x)

