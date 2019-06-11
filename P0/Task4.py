"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

calls = []
texts = []
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

# TeleMarketers which make outgoing call but never make texs...

# Mkaing a List of Outgoing calls
outgoing_calls = []
incoming_calls = []
s_message = []
r_message = []
for call in calls:
    outgoing_calls.append(call[0])
    incoming_calls.append(call[1])
for text in texts:
    s_message.append(text[0])
    r_message.append(text[1])

outgoing_calls = list(set(outgoing_calls))
incoming_calls = list(set(incoming_calls))
s_message = list(set(s_message))
r_message = list(set(r_message))

no_defaulters = incoming_calls + s_message + r_message
no_defaulters = list(set(no_defaulters))

potential_tele_marketers = []
for num in outgoing_calls:
    if num in no_defaulters:
        continue
    else:
        potential_tele_marketers.append(num)

potential_tele_marketers = list(set(potential_tele_marketers))
potential_tele_marketers = sorted(potential_tele_marketers)
print("These numbers could be telemarketers: ")
for num in potential_tele_marketers:
    print(num)
