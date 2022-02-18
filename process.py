log_file = open("um-server-01.txt")
# Sets a variable to the data within um-server-01.txt

def sales_reports(log_file):
    #Defines a function called sale_reports that takes in one argument called log_file
    for line in log_file:
        #loops through each line within the file
        line = line.rstrip()
        
        #gets rid of extra syntax that's not part of our data and sets it to line
        day = line[0:3]
        #sets a variable day equal to the first three char in the line
        if day == "Mon":
            #checks to see if day is equal to Tue, now Mon
            print(line)
            #if it is it prints the whole line


sales_reports(log_file)
#invoke the function with the data we opened
