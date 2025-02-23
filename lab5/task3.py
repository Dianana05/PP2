import re

text ="Hello_world This_is_Diana_s lab work example job_number"
pattern = r'[a-z]+_[a-z]+'
res=re.findall(pattern, text, re.IGNORECASE)
print(res)