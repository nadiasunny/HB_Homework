"""Generate sales report showing total melons each salesperson sold."""

#create empty salespeople & melons_sold lists
salespeople = []
melons_sold = []

#open sales-report file
f = open('sales-report.txt')

#loop over each line in sales-report
for line in f:
    #get rid of any trailing space, split on '|', 
    # entries is a list containing all words on that line
    line = line.rstrip()
    entries = line.split('|')
    #salesperson is found at index 0 of entries, hence we assign to salesperson var
    salesperson = entries[0]
    #number of melons is found at index of 2, and is converted from a str into an int
    melons = int(entries[2])

    #checking if salesperson already exists in salesperson list
    if salesperson in salespeople:
        #get index of where that salesperson can be found
        position = salespeople.index(salesperson)
        #at that same index, in melons_sold, rests that persons quantity sold
        melons_sold[position] += melons
    #else person not already in salespeople 
    else:
        #add person to end of people list
        salespeople.append(salesperson)
        #add that person's quantity sold
        melons_sold.append(melons)

#iterate starting at 0 going up to length of salespeople list
for i in range(len(salespeople)):
    #at current index, print person and their quantity sold
    print(f'{salespeople[i]} sold {melons_sold[i]} melons')

#a dictionary would be helpful, as we want to store key value pairs