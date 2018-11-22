import re
st = input("enter number")
res = re.compile("(0/91)?[6-9][0-9][5]")
if res.match(st):
    print("valid")

else:
    print("invalid")
print("=======================================")

name = input("enter ur name")
name_check = re.compile(r"[^A-Za-zs.]")
if name_check.search(name) == None:
    print("invalid name")
else:
    print("valid")
