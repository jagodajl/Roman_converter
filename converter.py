import re


class NumberOutOfRangeError(Exception):
    pass


class InvalidRomanNumeralError(Exception):
    pass


roman_numeral_validator = re.compile(
    "^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$",
    re.IGNORECASE
)

base_conversions = {
    1: 'I',
    4: 'IV',
    5: 'V',
    9: 'IX',
    10: 'X',
    40: 'XL',
    50: 'L',
    90: 'XC',
    100: 'C',
    400: 'CD',
    500: 'D',
    900: 'CM',
    1000: 'M'
}

base_numerals = {v: k for k, v in base_conversions.items()}

base_numbers = sorted(base_conversions.keys(), reverse=True)


def to_roman(arabic_number):
    if arabic_number < 0:
        raise NumberOutOfRangeError('negative values are not allowed')
    elif arabic_number == 0:
        raise NumberOutOfRangeError('zero is not allowed')
    elif arabic_number > 3999:
        raise NumberOutOfRangeError('number is too big')

    resulting_numeral = ''
    for num in base_numbers:
        while arabic_number >= num:
            arabic_number -= num
            resulting_numeral += base_conversions[num]

    return resulting_numeral


def from_roman(roman_numeral):
    if not roman_numeral_validator.match(roman_numeral):
        raise InvalidRomanNumeralError('invalid roman numeral')

    resulting_number = 0
    i = 0
    while i < len(roman_numeral):
        current_letter = roman_numeral[i]

        if i + 1 < len(roman_numeral):
            potential_base_numeral = current_letter + roman_numeral[i + 1]
            if potential_base_numeral in base_numerals:
                resulting_number += base_numerals[potential_base_numeral]
                i += 2
                continue

        resulting_number += base_numerals[roman_numeral[i]]
        i += 1

    return resulting_number

# checking how it works
if __name__ == "__main__":
    arabic_number = 942
    print(to_roman(arabic_number))

    roman_numeral = "XVII"
    print(from_roman(roman_numeral))
