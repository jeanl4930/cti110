#CTI110
#P4T2
#Jean
#12/02/18


#Set total to 0
#For 7 days input number of bugs collected for a day
#Add bugs collected to total
#Display total

#Initialize the accumulator
total = 0
#Get the bugs collected for each day
for day in range(1, 8):
    #Prompt the user.
    print('Enter the bugs collected on day', day)
    #Input the number of bugs.
    bugs = int(input())
    #Add bugs to total.
    total = total + bugs
    #total += bugs          #Another way of writing the total statement above

#Display the total bugs
print('You collected a total of', total, 'bugs.')
