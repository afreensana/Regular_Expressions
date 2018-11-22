# using"^","$" to get first and last string

import re
e4 = input("enter a string:")
res = re.findall(r"^\w+",e4) #['java']
#res = re.findall(r"^\w",e4) ['j']

print(res)
print("==============================================================")
rt = re.findall(r"\w+$",e4)     #['python']

#rt = re.findall(r"\w+$",e4) ['p']
print(rt)
