#Celsius to Fahrenheit temperature converter
#11/6/18
#CTI-110 P2HW1 - Celsius Fahrenheit Converter
#Jean


#This program converts Celsius to Fahrenheit
#Formula is F=9/5C+32


#Need user to enter temp in Celsius
celsius_temp = float(input("Enter the temperature in Celcius: "))
#Convert the temperature into Fahrenheit
fahrenheit_temp = 9/5 * celsius_temp + 32
#Display the temperature in Fahrenheit
print("The temperature in Fahrenheit is", fahrenheit_temp)
