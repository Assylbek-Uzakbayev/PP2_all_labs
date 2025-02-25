def snake_to_camel(snake_str):
    components = snake_str.split('_')
    return components[0] + ''.join(x.title() for x in components[1:])

snake_str = "snake_case_string"
camel_str = snake_to_camel(snake_str)
print(camel_str)
