import re
pattern = r'ab{2,3}'
test_str = "abbb"
if re.fullmatch(pattern, test_str):
    print("Match found")
else:
    print("No match")
