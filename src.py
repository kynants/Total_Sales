# Design a program that asks the user to enter a store's sales for each day of
# the week. The amounts should be stored in a list. Use a loop to calculate
# the total sales for the week and display the result.

# Initialized Variables
week = ('Sunday', 'Monday', 'Tuesday', 'Wednesday',
        'Thursday', 'Friday', 'Saturday')
day = 0
index = 0
total_sales = 0

# Initial Prompt
# sun_sales = float(input('Enter the store\'s sales for Sunday: '))

# Attempted for loop to count through the week array did not work.
# for days in range(len(week)):
#     sales = input('Enter the store\'s sales for', week[index])
#     total_sales += sales
#     index += 1

while day < len(week):
    sales = float(input('Enter the store\'s sales for {}'.format(week[index])))
    total_sales += sales
    index += 1

print(total_sales)