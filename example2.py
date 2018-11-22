# avoid spaces
import re
e2 = input("enter a string")
res = re.findall(r"\w",e2)
print(res)
