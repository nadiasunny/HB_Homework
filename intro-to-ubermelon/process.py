log_file = open("um-server-01.txt")


def generate_sales_reports(log_file):
    for line in log_file:
        line = line.rstrip()
        day = line[0:3]
        if day == "Tue":
            print(line)


generate_sales_reports(log_file)
log_file = open("um-server-01.txt")
# create a varible log file and assign it to the contents of the file

def generate_sales_reports(log_file):
# define the function sales report and use a parameter of log_file
    for line in log_file:
# looping over each line in given file   
        line = line.rstrip()
# we're creating a varible called line and assigning it to a line that has the white space removed from the right side 
        day = line[0:3]
# day is the first three letters of the line, which happen to be a day of the week
        if day == "Mon":
# day is changed to Mon, if the day is Monday then
            print(line)
# print the line of the sales on Monday 


generate_sales_reports(log_file)
# we're calling the function and passing in log_file as the argument