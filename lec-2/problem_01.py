# There are two friends, John and Smith, and the parameters j_angry 
# and s_angry to indicate if each is angry. You are in trouble if 
# both of them are angry or no one of them is angry.

x = input()
y = input()

if x == "true" and y == "true":
    print("I am in Trouble")
elif x == "true" or y == "true":
    print("I am in Trouble")
else:
    print("I am Saved")