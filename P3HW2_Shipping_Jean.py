#CTI110
#P3HW2
#Jean
#11/13/18

#This program displays the shipping charges based on the weight
#Get user to enter weight of package
#Display the shipping charges
#Calculate total charge

package_weight = float(input('Enter the weight of your package: '))
if package_weight <= 2:
    total_cost2 = package_weight * 1.50
    print('Shipping cost $1.50 per lbs')
    print('Total is $',total_cost2)
if package_weight > 2 and package_weight <= 6:
    total_cost2_6 = package_weight * 3.00
    print('Shipping cost $3.00 per lbs')
    print('Total is $',total_cost2_6)
if package_weight > 6 and package_weight <= 10:
    total_cost6_10 = package_weight * 4.00
    print('Shipping cost $4.00 per lbs')
    print('Total is $',total_cost6_10)
if package_weight > 10:
    total_cost10 = package_weight * 4.75
    print('Shipping cost $4.75 per lbs')
    print('Total is $',total_cost10)    
