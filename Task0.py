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


def get_date_and_time(date):
    """This function takes a date as input and extracts the date and time components."""
    result = date.split()
    return result[0], result[1]


first_texts_record = texts[0]
first_texts_record_date_time = get_date_and_time(first_texts_record[2])

last_calls_record = calls[-1]
last_calls_record_date_time = get_date_and_time(last_calls_record[2])

print(f"First record of texts, {first_texts_record[0]} texts {first_texts_record[1]} "
      f"at time {first_texts_record_date_time[1]}")
print(f"Last record of calls, {last_calls_record[0]} calls {last_calls_record[1]} "
      f"at time {last_calls_record_date_time[1]},"
      f" lasting {last_calls_record[3]} seconds")
