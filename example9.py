#validating the name
import re
name = input("enter a string:")
res = re.match("^[A-Za-z]*$",name)
print(res)
if res == None:
    print("enter correct name")
else:
    print("name is:", res)


#res = re.findall("^[A-Za-z]*$",name)       #name is: ['sana']
