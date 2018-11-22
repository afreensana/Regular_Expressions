#using *,+  to get word

import re
e3=input("enter a string:")
res = re.findall(r"\w*",e3)
print(res) # ['python', '', 'is', '', 'best', '']
# space is also returning, to avid  space we will use +
print("===================================")

rt = re.findall(r"\w+",e3)
print(rt)


