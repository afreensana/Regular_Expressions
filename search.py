
import re
se = input("ENter a String:")
result = re.search(r"Python",se)
if result == None:
    print("match not found")
else:
    print("match found")
    print(result.group())
    print(result.start())
    print(result.end())

print("thank you")
