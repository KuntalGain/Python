# Given a positive integer x. Your task is to check, if it is even 
# or odd (Any number that gives zero as remainder when divided by
#  2 is an even number)

num = int(input('Enter the number : '))

if num % 2 == 0:
    print("Even")
else:
    print("Odd")