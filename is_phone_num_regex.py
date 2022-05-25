#! /usr/bin/python3
# esse programa faz a mesma coisa que o programa is_phone_number.py usando re

import re

is_phone_number_regex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
message = is_phone_number_regex.findall('Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.')
for i in range(len(message)):
    print(f'Phone number found: {message[i]}')
print('Done')
