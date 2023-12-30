"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
import re

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore. In other words, the calls were initiated by "(080)" area code
to the following area codes and mobile prefixes:
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

def is_fixed_line(number: str) -> bool:
  '''Checks whether a number is a fixed line number or not.'''
  
  return re.fullmatch(r'\(0\d+\)\d+', number) is not None


def is_mobile(number: str) -> bool:
  '''Checks whether a number is a mobile number or not.'''
  
  return re.fullmatch(r'[7-9]\d+\s\d+', number) is not None


def is_telemarketer(number: str) -> bool:
  '''Checks whether a number is a telemarketer number or not.'''
  
  return re.fullmatch(r'140\d+', number) is not None


cities_with_area_code = {"bangalore": "080"}


def get_prefix_number(number: str) -> str:
  '''
  Returns the prefix of the given mobile number.
  For fixed lines, the prefix is the area code.
  For mobile numbers, the prefix is the first four digits.
  For telemarketers, the prefix is the first three numbers that is always 140.
  '''
  
  if is_fixed_line(number=number):
    closing_bracket_position = number.find(')')
    return number[1:closing_bracket_position]
  elif is_mobile(number=number):
    return number[0:4]
  elif is_telemarketer(number=number):
    return number[0:3]
    
  return None


def get_phone_number_origin(number: str) -> str:
  '''
  Returns the city from which the given number is calling.
  Only fixed lines can have the city identified.
  '''
  
  if not is_fixed_line(number=number):
    return None
  
  prefix = get_prefix_number(number=number)
  
  for city, area_code in cities_with_area_code.items():
    if prefix == area_code:
      return city
  
  return None


prefixes_and_area_codes = set()

for entry in calls:
  if get_phone_number_origin(number=entry[0]) == 'bangalore':
    prefix = get_prefix_number(number=entry[1])
    
    if prefix is not None:
      prefixes_and_area_codes.add(prefix)
    
    
print("The numbers called by people in Bangalore have codes:")
for item in sorted(prefixes_and_area_codes):
  print(item)


calls_from_bangalore = 0
calls_to_bangalore = 0

for entry in calls:
  if get_phone_number_origin(number=entry[0]) == 'bangalore':
    calls_from_bangalore += 1
    
    if get_phone_number_origin(number=entry[1]) == 'bangalore':
      calls_to_bangalore += 1

bangalore_calls_percentage = calls_to_bangalore / calls_from_bangalore * 100

print("\n{:.2f} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.".format(bangalore_calls_percentage))