# Return the first two character of each word
import re
e5 = input("enter a string:")
res = re.findall(r"\w\w",e5)
print(res)
#getting two consecutive char's
print("======================")
rt = re.findall(r"\b\w",e5)
print(rt)