'''It is possible to name the days 0 thru 6 where day 0 is Sunday and day 6 is Saturday. If you go on a wonderful holiday leaving on day number 3 (a Wednesday) and you return home after 10 nights you would return home on a Saturday (day 6). Write a general version of the program which asks for the starting day number, and the length of your stay, and it will tell you the number of day of the week you will return on.
'''

#Create a list of days of the week and ask the user for input selecting what number day of the week they're leaving and how many nights they're staying.
days_in_week = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
startDay = int(input("Number the days of the week 0 thru 6 where day 0 is Sunday and day 6 is Saturday. What day are you leaving (in number)?"))
returnDay = int(input("How many nights are you staying?"))

#Calculate what number day of the week the user will return on
returnNum = (startDay + returnDay) % len(days_in_week)

#Use indexing to figure out the written-out name of the number day the user will return
returnDay = days_in_week[returnNum]

print("You will return on {}, ".format(returnDay), "day #", returnNum)
