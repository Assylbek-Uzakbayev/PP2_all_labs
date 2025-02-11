def spy_game(nums):
    code = [0, 0, 7]
    code_index = 0
    for num in nums:
        if num == code[code_index]:
            code_index += 1
        if code_index == len(code):
            return True
    return False
