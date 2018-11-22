#returning words that start with vowels

import re
e8 = input("enter a string:")
res = re.findall(r"\w+",e8)
print(res)

print("=====================")

# vowels

res = re.findall(r"[aeiouAEIOU]\w+",e8)
print(res)

