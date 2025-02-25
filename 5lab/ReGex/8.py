import re
text = "SplitAtUppercaseLetters"
result = re.findall(r'[A-Z][a-z]*', text)
print(result)
