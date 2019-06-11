"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
calls = []
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


number_time = {}
for call in calls:
    number_time[call[0]] = number_time.get(call[0], 0) + int(call[3])
    number_time[call[1]] = number_time.get(call[1], 0)+int(call[3])

longest_duration = max(number_time, key=number_time.get)
# print(number_time[longest_duration])

print("{} spent the longest time, {} seconds, on the phone during September 2016.".format(
    longest_duration, number_time[longest_duration]))
