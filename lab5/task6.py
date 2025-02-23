import re

test = "Hello, world. How are you?"
pattern = r'[ ,.]+' 
replacement = ':'

result = re.sub(pattern, replacement, test)
print(result)
