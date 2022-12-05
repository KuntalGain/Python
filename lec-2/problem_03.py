# Given two integer variables a and b, and a boolean variable flag. 
# The task is to check the status and return accordingly.
# Return True for the following cases:

# Either a or b is non-negative and flag is false.
# Both a and b are negative and flag is true.
# Otherwise, return false.


def checkFlag(a,b,flag):
    if a < 0 or b < 0:
        if flag == True:
            return True
    elif a < 0 and b < 0:
        if flag == True:
            return True
    else:
        return False

a = int(input('Enter 1st num : '))
b = int(input('Enter 2nd num : '))
flag = input()

if checkFlag(a, b, flag) is True:
    print("true")
else:
    print("false")
