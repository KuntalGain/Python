# Given two strings a and b. The task is to make a new string where 
# the string with longer length should be in between and the one with
# shorter length should be outside on front and end. New string should
# be like shorter+longer+shorter.

a = input()
b = input()

if len(a) > len(b):
    longer = a
    shorter = b
else:
    longer = b
    shorter = a

print(shorter+longer+shorter)
