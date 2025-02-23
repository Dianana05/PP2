import re

text = "InsertSpacesBetweenWordsStartingWithCapitalLetters"
pattern = r'([A-Z][a-z]*)'
result = re.findall(pattern, text)
res=' '.join(result)  
print(res)
