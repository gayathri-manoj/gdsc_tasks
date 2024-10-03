# Define the function 'date' which calculates the day and month based on day number 'x' and year 'y'
def date(x, y):
    # List of month names for reference
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    
    # List of the number of days in each month for a regular (non-leap) year
    l = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    # Check if the year is a leap year and update February days to 29 if true
    if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0):
        l[1] = 29  # Set February to 29 days in leap years
    # Initialize a counter to track the current month
    count = 0   
    
    # Loop through the list 'l' containing the days in each month
    for i in l:
        # If the day number 'x' is greater than the current month's days, subtract that month from 'x'
        if x > i:
            x = x - i
            # Move to the next month by incrementing the counter
            count = count + 1
    
    # Print the resulting day, month, and year
    print(x, months[count], ',', y)

# Input the day number from the user
x = int(input('Enter day number: '))

# Input the year from the user
y = int(input('Enter year: '))

# Call the 'date' function with the input values
date(x, y)
