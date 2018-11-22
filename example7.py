#Returning date from given string

import re
e7 = input("enter date:")
result = re.findall(r"\d",e7)
print(result)
