import re

text = "SplitThisStringAtUpperCaseLetters"
pattern = r'([A-Z][a-z]*)' 
result = re.findall(pattern, text)
print(result)
