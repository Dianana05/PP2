import re

test=r'a and aBb or abba but not aBB abb abbb abba'
pattern=r'\bab{2,3}\b'
res=re.findall(pattern, test, re.IGNORECASE)
print(res)