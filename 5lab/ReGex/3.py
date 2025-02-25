import re
pattern = r'[a-z]+_[a-z]+'
test_str = "hello_world"
if re.fullmatch(pattern, test_str):
    print("Match found")
else:
    print("No match")
