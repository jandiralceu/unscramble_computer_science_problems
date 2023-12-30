"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""


all_contacts = {}
'''Dict of telephone numbers with total duration of calls made and received.'''


for entry in calls:
    all_contacts[entry[0]] = all_contacts.get(entry[0], 0) + int(entry[3])
    all_contacts[entry[1]] = all_contacts.get(entry[1], 0) + int(entry[3])


telephone = max(all_contacts, key=all_contacts.get)
time_in_seconds = all_contacts[telephone]
    

print(f"{telephone} spent the longest time, {time_in_seconds} seconds, on the phone during September 2016.")