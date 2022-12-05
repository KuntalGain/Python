# operators

print("Python Arithmatics :- ")

x = 10
y = 5

add = x + y
sub = x - y
mul = x * y
div = x / y
mod = x % y
exp = x ** y
flr = x // y

print("Addition : ",add)
print("Subtarction : ",sub)
print("Multiplication : ",mul)
print("Division : ",div)
print("Modulas : ",mod)
print("expontial : ",exp)
print("Floor division : ",flr)

# identity operator

a = 10
b = 20

if(a is b):
    print("true")
if(a is not b):
    print("false")

# membership operator

x = [1,2,3]
y = 2

if(y in x):
    print("true")
