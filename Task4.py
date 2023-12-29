"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""


all_contacts = set()

for entry in calls:
    all_contacts.add(entry[0])
    all_contacts.add(entry[1])
    
for entry in texts:
    all_contacts.add(entry[0])
    all_contacts.add(entry[1])


def has_sent_or_received_message(number: str) -> bool:
    '''Checks whether a number has sent or received a message.'''
    for entry in texts:
        if entry[0] == number or entry[1] == number:
            return True
        
    return False

def has_income_call(number: str) -> bool:
    '''Checks whether a number has received an income call.'''
    for entry in calls:
        if entry[1] == number:
            return True
        
    return False

for number in all_contacts.copy():
    if has_sent_or_received_message(number) or has_income_call(number):
        all_contacts.remove(number)


print("These numbers could be telemarketers: ")
for number in sorted(all_contacts):
    print(number)