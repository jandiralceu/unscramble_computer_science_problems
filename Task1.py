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
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""


numbers_list: [str] = []

for entry in texts:
    numbers_list.append(entry[0])
    numbers_list.append(entry[1])

for entry in calls:
    numbers_list.append(entry[0])
    numbers_list.append(entry[1])

contacts = set(numbers_list)

print(f"There are {len(contacts)} different telephone numbers in the records.")
