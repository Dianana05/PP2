import re

text = "ConvertThisCamelCaseToSnakeCase"
pattern = r'([a-z])([A-Z])'
snake_case = re.sub(pattern, r'\1_\2', text).lower()
print(snake_case)
