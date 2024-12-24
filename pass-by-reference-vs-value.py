# Python's argument-passing model is neither "Pass by Value" nor "Pass by Reference"
# It is "Pass by Object Reference"
# Depending on the type of object you pass in the function, the function behaves differently.
# Immutable objects show “pass by value” whereas mutable objects show “pass by reference”.

def call_by_value(x):
    x = x * 2
    print("in function number updated to", x)
    return

def call_by_reference(list):
    list.append("D")
    print("in function list updated to", list)
    return

my_list = ["E"]
num = 6
print("number before=", num)
call_by_value(num)
print("after function number=", num)
print("list before",my_list)
call_by_reference(my_list)
print("after function list is ",my_list)