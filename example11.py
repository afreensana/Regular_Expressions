#validating email

import re
str = input("Enter an input string:")
m = re.match('[^@]+@[^@]+\.[^@]+',str)
if m:
    print("True")
else:
    print("False")



# shanu@gmail.com  True
##ouput    "89655533@852636.com" true
