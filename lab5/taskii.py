import re

test=r'a and aBb ab or abba but not aBB abb abbb abba'
pattern=r'ab*'
res = re.findall(pattern, test, re.IGNORECASE)
print(res)