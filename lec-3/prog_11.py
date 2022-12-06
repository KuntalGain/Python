# format Strings

age = 20
txt = "My Name is Kuntal , and I am {}"
print(txt.format(age))

quantity = 3
item_no = 567
price = 49.95

myOrder = "I want to pay {2} dollars for {0} pieces of item {1}"

print(myOrder.format(quantity,item_no,price))