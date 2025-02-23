import re

def replace(s):
    return re.sub(r'_([a-z])', lambda match: match.group(1).upper(), s)

test = "this_is_snake_case_example"
camel_case = replace(test)

print(camel_case)
