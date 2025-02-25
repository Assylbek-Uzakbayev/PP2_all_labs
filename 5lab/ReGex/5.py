import re
pattern = r'a.*b'
test_str = "a123b"
if re.fullmatch(pattern, test_str):
    print("Match found")
else:
    print("No match")
