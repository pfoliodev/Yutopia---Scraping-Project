# utils.py
import re

def string_to_boolean(stock_element):
    # Convert text to boolean
    stock_text = stock_element.text.strip()
    return 'In stock' in stock_text

def convert_string_to_int(string_element):
    numbers = []
    current_number = ""

    for char in string_element:
        if char.isdigit():
            current_number += char

        elif current_number:
            numbers.append(int(current_number))
            current_number = ""

    if current_number:
        numbers.append(int(current_number))

    if not numbers:
        return 0

    return int(''.join(map(str, numbers)))

def convert_string_to_float(string_element):
    return float(''.join(map(str, re.findall(r'\d+\.*\d*', string_element))))
