#CTI110
#P4T1a
#Jean
#12/02/18

#This program analysis user's budget

#Create a variable to control the loop.
another = 'y' 

#Initialize the accumulator
total = 0.00

#User enters the amount budgeted for a month.
budget = float(input('Enter the amount budgeted for the month: '))


while another == 'y' or another == 'y':
    #User enters expenses for the month.
    expense = float(input('Enter expense ' +\
                          'for the month: '))
    

    #Validate the expense amount.
    while expense < 0:
        print('ERROR:  expense cannot be negative.')
        expense = float(input('Enter the correct ' +\
                                'expense: '))

    #Add expance to total.
    total = total + expense 

    after_expenses = budget - total

    #Display the total.
    print('Total expenses are $', \
          format(total, ',.2f'))

    #See if user wants to enter another expense.
    another = input('Do you want to enter another ' +\
                'expense (Enter y for yes): ')


   #Displays the amount the user is over or under budget
    after_expense = budget - total
    if total < budget:
        print('You are below budget, YEAH', '$', after_expense)
    if total > budget:
        print('You are over budget.', '$', after_expense)
                  
   
                     
            


    






