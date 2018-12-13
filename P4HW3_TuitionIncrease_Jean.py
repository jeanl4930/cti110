#CTI110
#P4T1a
#Jean
#12/02/18

#This program will display the projected tuition amount
#for the next 5 years increase.


#Current tuition for full-time student
Tuition = 8000       
print("Current tuition is: $%.2f" % Tuition)

#Tuition will increase 3% each year 
Increase_rate = 0.03

#Calculate tuition increase for next 5 years
for year in range (1,6):
    Tuition += Tuition * Increase_rate
    print('Projected tuition year {}: $%.2f'.format(year) % Tuition)













