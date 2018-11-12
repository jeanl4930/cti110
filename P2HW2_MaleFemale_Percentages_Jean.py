#Number of Male and Female Students as Percentages
#11/10/18
#CTI-110 P2HW2 - Male Female Percentage
#Jean


#This program display the percentage of males and females in class


#Need user to enter number of males in class?
male_numbers = int(input("Enter the number of male students:  "))
#Need user to enter number of females in class?
female_numbers = int(input("Enter the number of female students: "))
#Need total number of students calculated
totalNumber = male_numbers + female_numbers
#Need calculation for percentage of male students
male_percentage = male_numbers/totalNumber
#Need calculation for percentage of female students
female_percentage = female_numbers/totalNumber
#Display the percentage of males and females in class
print("The percentage of male students is", float(male_percentage))
print("The percentage of female students is", float(female_percentage))





