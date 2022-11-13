ROMAN_NUMERALS = ('I', 'V')
def add(augend, addend):
    if not isinstance(augend, str) or not isinstance(addend, str):
        raise ValueError
    simple_sum = augend + addend
    if any(char != 'I' for char in simple_sum):
        raise ValueError

    canonicalised_sum = simple_sum.replace('IIIII', 'V').replace('IIII', 'IV')
    return canonicalised_sum