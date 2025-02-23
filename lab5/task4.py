import re

text = "Hello World, this Is a Test  Diana work Comment string lab5 PP2 String"
pattern = r'[A-Z][a-z]+'
res = re.findall(pattern, text)
print(res)
