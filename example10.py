# Match a string to a numeric sequence of exactly five

import re
e10 = input("Enter an input string:")
m = re.match('\d{5}\Z',e10)
if m:
    print("True")
else:
    print("False")
