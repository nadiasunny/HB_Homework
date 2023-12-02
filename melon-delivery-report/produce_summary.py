"""Module providing a function printing delivery statements."""

def produce_sum(filename):
    """Prints each delivery's details; what, how many, and how much.

        input-
        str: filename

        output-
        str: each sales info
    """
    #open given file
    the_file = filename.open()
    #iterate over each line in file
    for line in the_file:
        #get rid of any trailing white space on right side & split str on each "|" into a list
        delivery = line.rstrip().split('|')
        #assign melon, count, and amount to their values found in delivery list
        melon = delivery[0]
        count = delivery[1]
        amount = delivery[2]
        #Print informative line about each delivery
        print(f"Delivered {count} {melon}s for total of ${amount}")
    #close file
    the_file.close()