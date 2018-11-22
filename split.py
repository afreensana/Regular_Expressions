
import re
stg = input("enter a string:")
result = re.split(r"s",stg,5)
print(result)
print(len(result))
print(len(result)-1)

