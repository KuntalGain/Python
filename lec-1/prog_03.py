# data types

# basic data type

a = 'Hello World'   # String
print(type(a),a)

b = 20              # integer
print(type(b),b)    

c = 20.5            #float
print(type(c),c)

d = 1j              #complex
print(type(d),d)

# data structures

e = ["apple" , "banana" , "cheery"]         # list
print(type(e),e)

f = ("apple" , "banana" , "cheery")         # tuple
print(type(f),f)

g = range(6)                                # range
print(type(g),g)

h = {"name" : "Jhon", "age"  : 36}          # dictionary
print(type(h),h)

i = {"apple" , "banana" , "cheery"}         # set
print(type(i),i)

j = True            # bool
print(type(j),j)

k = b"hello"        # byte
print(type(k),k)

l = bytearray(5)    # bytearray
print(type(l),l)
