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
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""


def get_date_and_time(date: str) -> tuple(str, str):
    """
    This function takes a date string as input and extracts the date and time values.
    """
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
