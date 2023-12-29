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


all_contacts = {}
'''Dict of telephone numbers with total duration of calls made and received.'''


for entry in calls:
    sender = entry[0]
    receiver = entry[1]
    
    all_contacts[sender] = all_contacts[sender] + int(entry[3]) if sender in all_contacts.keys() else int(entry[3])
    all_contacts[receiver] = all_contacts[receiver] + int(entry[3]) if receiver in all_contacts.keys() else int(entry[3])


telephone = next(iter(all_contacts))
'''Telephone number with the longest time spent on the phone'''
time_in_seconds = all_contacts[telephone]
'''Time spent on the phone by the telephone number with the longest time spent on the phone'''


for key in all_contacts:
    if all_contacts[key] > time_in_seconds:
        time_in_seconds = all_contacts[key]
        telephone = key
    


print(f"{telephone} spent the longest time, {time_in_seconds} seconds, on the phone during September 2016.")