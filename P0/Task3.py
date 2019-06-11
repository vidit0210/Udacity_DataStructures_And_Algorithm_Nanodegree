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
in Bangalore.
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

toMatch = "(080)"  # Fixed Lines

caller_fixed_code = []

called_by_bangalore = []
callers = []
recievers = []
for call in calls:
    if(toMatch in call[0]):
        called_by_bangalore.append(call[1])
        callers.append(call[0])

len_callers = float(len(callers))
for call in called_by_bangalore:
    if(toMatch in call):
        recievers.append(call)

len_receivers = float(len(recievers))

area_code = []  # Begins With 080
mobile_number = []  # have Space in Between
telem = []  # 140
s = "(04344)316423"
start = re.escape("(")
end = re.escape(")")
result = re.search('%s(.*)%s' % (start, end), s).group(1)

mobile_match = " "
telem_match = "140"
for call in called_by_bangalore:

    if(str(call[0:3]) == telem_match):
        telem.append(call[0:3])
    elif(mobile_match in call):
        mobile_number.append(call[0:4])
    else:
        result = re.search('%s(.*)%s' % (start, end), str(call)).group(1)
        area_code.append(result)


area_code = list(set(area_code))
mobile_number = list(set(mobile_number))
telem = list(set(telem))
all_codes = area_code + mobile_number + telem
all_codes = list(set(all_codes))
all_codes = sorted(all_codes)
print("The numbers called by people in Bangalore have codes:")
for num in all_codes:
    print(num)


"""
Part B
"""
# print(length_fixed_code)
# print(len(caller_fixed_code))

percentage = (len_receivers/len_callers) * 100
print(round(percentage, 2))
