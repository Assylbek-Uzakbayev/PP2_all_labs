import re
pattern = r'a*b'
test_str = "aab"
if re.fullmatch(pattern, test_str):
    print("Match found")
else:
    print("No match")
