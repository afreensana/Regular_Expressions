# search if an e-mail address is in a string:

import re
input = input("enter a string")
m = re.search('[^@]+@[^@]+\.[^@]+',input)
if m:
    print("String found.")
else:
    print("No String found.")