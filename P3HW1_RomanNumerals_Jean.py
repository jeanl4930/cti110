#CTI110
#P3HW1
#Jean
#11/13/18

#This program displays the Roman numeral of a number 1 through 10
#Get user to enter a number
#Display the Roman muneral version
#If number is outside the range 1 through 10
#Display an error message


number = int(input('Enter number between 1 through 10:  '))
if number == 1:
    print('The Roman numeral is I.')
if number == 2:
    print('The Roman numeral is II.')
if number == 3:
    print('The Roman numeral is III.')
if number == 4:
    print('The Roman numeral is IV.')
if number == 5:
    print('The Roman numeral is V.')
if number == 6:
    print('The Roman numeral is VI.')
if number == 7:
    print('The Roman numeral is VII.')
if number == 8:
    print('The Roman numeral is VIII.')
if number == 9:
    print('The Roman numeral is IX.')
if number == 10:
    print('The Roman numeral is X.')
elif number < 1 or number > 10:
    print('Error_Number not within range!') 
