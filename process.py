import csv
from collections import Counter
from Tkinter import Tk
from tkFileDialog import askopenfilename

Tk().withdraw() #Show just the file picker
filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
print(filename)

n = input("How many customers would you like to see: ")

with open(filename, 'r') as f:
    column = (row[0] for row in csv.reader(f))
    if n == 1:
        #TODO Input File error check
        #Generator epression to process customer_id field for one customer. More efficient memory use.
        print("Customer ID with most consecutive daily payments: {0}".format(Counter(column).most_common()[0][0]))

    elif n >=2 :
        #TODO Input Error Check
        print "Customer IDs with most consecutive daily payments:"
        client = Counter(column).most_common(n)
        #Clean Output to show only Customer ID
        print [client for client,cnt in client]
