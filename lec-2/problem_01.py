# There are two friends, John and Smith, and the parameters j_angry 
# and s_angry to indicate if each is angry. You are in trouble if 
# both of them are angry or no one of them is angry.

j_angry = bool(input())
s_angry = bool(input())

if j_angry == True and s_angry == False:
    print("You are in Troble")
elif j_angry == False and s_angry == True:
    print("You are in Troble")
elif j_angry == True and s_angry == True:
    print("You are in Troble")
elif j_angry == False and s_angry == False:
    print("You are Safe")