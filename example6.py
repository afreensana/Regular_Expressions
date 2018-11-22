# returning domain of mail id

import re
e6 = input("enter ur mailid:")
res = re.findall(r"@\w+",e6)
print(res)  # ['@gmail']
print("======================================================")

# domain
res = re.findall(r"@\w+.\w+",e6)
print(res)     # ['@gmail.com', '@yahoo.com']

print("====================================================")

#only domain name
res = re.findall(r"@\w+.(\w+)",e6)
print(res)



