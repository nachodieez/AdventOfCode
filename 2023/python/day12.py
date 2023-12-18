import sys
from functools import cache

# Read the puzzle input
with open("../data/day12.in") as file_desc:
    raw_file = file_desc.read()
# Trim whitespace on either end
raw_file = raw_file.strip()

output = 0

@cache
def calc(record, groups, n_current_group = 0):
    
    ## ADD LOGIC HERE ... Base-case logic will go here

    # If the string is empty and the groups are empty
    if not record and not groups:
        return 1
    
    # If the string is empty but some records are yet to be completed
    if not record and groups:
        return 0
    
    # If the groups are completed, the string is not empty but only dots 
    # (or question marks treated as dots) are left
    if not groups and record:
        return all(x == "." or x == "?" for x in record) # i treat ? as dots

    # Think of these like fib(0) or fib(1). In this case, we have to handle an empty record or an empty groups

    # Look at the next element in each record and group
    next_character = record[0]
    next_group = groups[0]

    # Logic that treats the first character as pound-sign "#"
    def pound():
        ## ADD LOGIC HERE ... need to process this character and call
        #  calc() on a substring

        return calc(record[1:], groups, n_current_group + 1)
        
    # Logic that treats the first character as dot "."
    def dot():
        ## ADD LOGIC HERE ... need to process this character and call
        #  calc() on a substring
        if next_group == n_current_group:
            return calc(record[1:], groups[1:])
        elif n_current_group == 0:
            return calc(record[1:], groups)
        else:
            return 0

    if next_character == '#':
        # Test pound logic
        out = pound()

    elif next_character == '.':
        # Test dot logic
        out = dot()

    elif next_character == '?':
        # This character could be either character, so we'll explore both
        # possibilities
        out = dot() + pound()

    else:
        raise RuntimeError

    # Help with debugging
    # print(record, groups, "->", out)
    return out

# Iterate over each row in the file
for entry in raw_file.split("\n"):

    # Split by whitespace into the record of .#? characters and the 1,2,3 group
    record, raw_groups = entry.split()
    record += "."

    # Convert the group from string "1,2,3" into a list of integers
    groups = [int(i) for i in raw_groups.split(',')]

    # Call our test function here
    output += calc(record, tuple(groups))

    # print(10*"-")

print("Sol 1:", output)

output = 0
for entry in raw_file.split("\n"):

    record, raw_groups = entry.split()
    record = "?".join([record] * 5)
    record += "."

    groups = [int(i) for i in raw_groups.split(',')]
    groups *= 5

    output += calc(record, tuple(groups))

print("Sol 2:", output)