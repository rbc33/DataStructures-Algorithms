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

text_num = []
incoming = []
call_num = []
for text in texts:
    if text[0] not in text_num:
        text_num.append(text[0])
    if text[1] not in text_num:
        text_num.append(text[1])
for call in calls:
    if call[0] not in call_num:
        call_num.append(call[0])
    if call[1] not in incoming:
        incoming.append(call[1])
sus_nums = []
for call in call_num:
    if call not in text_num and call not in incoming:
        sus_nums.append(call)
sus_nums.sort()

print("These numbers could be telemarketers: ")
for num in sus_nums:
    print(num)

