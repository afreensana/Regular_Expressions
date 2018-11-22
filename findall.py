import re
na = input("Enter a string:")
res = re.findall(r"python",na)
print(res)
print(len(res))

print("=================================================================")
if res == None:
    print("match not found")
else:
    print("match found:",res)
    print(len(res))
print("that's it")