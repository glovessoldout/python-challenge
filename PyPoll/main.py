#!/usr/bin/env python
# coding: utf-8

# In[20]:


#ignore this one

#import os
#import csv

#csvpath = os.path.join('.', 'Resources','election_data.csv')
#with open(csvpath) as csvfile:
    
#    csvreader = csv.reader(csvfile, delimiter=',')
#    #print(csvreader)
#    count = 0
#    for row in csvreader:
#        count = count + 1
#print(count)
#print(csvpath[0])


# In[87]:


import os
import csv

csvpath = os.path.join('.', 'Resources','election_data.csv')
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    vote_header = next(csvreader) #seperate header from votes
    candidate_list = []
    vote_count = []
    count = 0
    for row in csvreader:
        count = count + 1
        if row[2] not in candidate_list:
            candidate_list.append(row[2])
            vote_count.append(0)
        nth = candidate_list.index(row[2])
        vote_count[nth] = vote_count[nth] + 1
    
        
    #print(f"{vote_header}")
    #print(row)
    #print(count)
    #print(candidate_list)
    #print(vote_count)
    
poll = open("./analysis/polling results.txt",'w')
poll.write("Election Results:")
poll.write("\n")
poll.write("-------------------------------")
poll.write("\n")
poll.write(f"Total Votes:  {count}")
poll.write("\n")
poll.write("-------------------------------")
poll.write("\n")
for word in candidate_list:
    mth = candidate_list.index(word)
    poll.write(f"{candidate_list[mth]}: " "{:.3%}".format(vote_count[mth]/count))
    poll.write("      ")
    poll.write("("+str(vote_count[mth])+")")
    poll.write("\n")
    
poll.write("-------------------------------")
poll.write("\n")
winner = candidate_list[(vote_count.index(max(vote_count)))]
poll.write(f"Winner: {winner}")
poll.close()


# In[ ]:





# In[ ]:




