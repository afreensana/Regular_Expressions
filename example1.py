
# first word of a given string

import re
e1 = input("enter a string:")
res = re.findall(r".",e1)
print(res)
# using '.', we are getting spaces as well