"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

texts = []
calls = []

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
text_data = []
call_data = []
for text in texts:
    text_data.append(text[0])
    text_data.append(text[1])

for call in calls:
    call_data.append(call[0])
    call_data.append(call[1])


records = call_data + text_data
# print(len(records) == 2*(len(calls) + len(texts)))
# print(records[0])

print("There are {} different telephone numbers in the records.".format(
    len(set(records))))
