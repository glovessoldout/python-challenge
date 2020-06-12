#!/usr/bin/env python
# coding: utf-8

# In[35]:


import os
import csv

csvpath = os.path.join('.', 'Resources','budget_data.csv')
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    bank_header = next(csvreader) #seperate header from the data
    date = []
    change = [] #easier to manage this particular dataset as 2 lists
    month = 0
    total = 0
    difference = 0
    for row in csvreader:
        month = month + 1
        date.append(row[0])
        change.append(int(row[1]))
    
dolla = open("./analysis/Financial Analysis.txt",'w')
dolla.write("Financial Analysis")
dolla.write("\n")
dolla.write("-------------------------------")
dolla.write("\n")
dolla.write("Total Months: " + str(month))
dolla.write("\n")
dolla.write("Total: $" + str(sum(change)/month*1.00))
dolla.write("\n")
dolla.write("Average Change: $" +  str(sum(change)/month))
dolla.write("\n")
dolla.write("Greatest Increase in Profits: " + date[change.index(max(change))] + " ("+str(max(change))+")")
dolla.write("\n")
dolla.write("Greatest Decrease in Profits: " + date[change.index(min(change))] + " ("+str(min(change))+")")
dolla.write("\n")
dolla.write("\n")

dolla.close()


# In[ ]:




