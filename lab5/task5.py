import re

test=r"accb bgia ab aandb a_b ah kghti dhb a1b"
pattern=r'a+\w*b\b'
res=re.findall(pattern, test)
print(res)