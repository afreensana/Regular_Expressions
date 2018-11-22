
import re
na = input("Enter a String:")
res = re.match(r"Sana", na)
print(res)
print("===========================================")
print(res.group())
print(res.start())
print(res.end())
