#CTI110
#P4T1a
#Jean
#12/02/18

#This program displays a table of Celsius
#temperature & Fahrenheit equivalent.

#Formula F = 9/5C + 32

#Print the table headings.
print('C_temp\tF_temp')
print('-------------------')

#Print the Celsius temperature 0 through 20 and
#their Fahrenheit equivalent. 

for Celsius_temp in range(0,21):
    Fahrenheit_temp = 9/5 * Celsius_temp + 32   #Convert to Fahrenheit
    print(Celsius_temp, '\t', Fahrenheit_temp)  #Print table 


