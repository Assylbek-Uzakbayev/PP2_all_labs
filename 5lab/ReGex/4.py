import re
pattern = r'[A-Z][a-z]+'
test_str = "Hello"
if re.fullmatch(pattern, test_str):
    print("Match found")
else:
    print("No match")
