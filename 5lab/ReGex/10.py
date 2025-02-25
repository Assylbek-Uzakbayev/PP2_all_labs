import re
def camel_to_snake(camel_str):
    return re.sub(r'([a-z])([A-Z])', r'\1_\2', camel_str).lower()

camel_str = "camelCaseString"
snake_str = camel_to_snake(camel_str)
print(snake_str)
