# How to Remove \xa0 from a String in Python

import unicodedata

my_str = 'bobby\xa0hadz'

result = unicodedata.normalize('NFKD', my_str)
print(result)  # 👉️ 'bobby hadz'