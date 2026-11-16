# integer_value=24#integer age
# float_value=3.14#float pi
# # remainder=7%2
# # print(remainder)
# # print(age)
# # print(pi)
# string_value="prasad"#name is string variable
# #list starts
# list_value=[["prasad,33"],["john,24"],["raj,34"]]
# # print(list_value)
# # print(list_value[0])
# #dictionary starts
# dict_value={"name":"prasad",
#               "age":33,
#               "course":"ece"}
# print(dict_value["age"])
# #tuple starts
# tuple_value=(90,8,8)
# print(tuple_value)
# #set starts
# set_value={"prasad","john"}
# print(set_value)
# d={0,1,5,5,7}
# print (d)

# for value in [
#     integer_value,
#     float_value,
#     list_value,
#     set_value,dict_value,
#     tuple_value,
# ]:
#     print(value, type(value))
integer_value = 5
float_value = 3.14
string_value = "Sales"
list_value = [1, 2, 3]
dict_value = {"item": "Notebook", "price": 120}
set_value = {"North", "South"}
tuple_value = ("January", "February")

# Print each value and its type
for value in [
    integer_value,
    float_value,
    string_value,
    list_value,
    dict_value,
    set_value,
    tuple_value,
]:
    print(value, type(value))

#####################################
sales=[12000,0,8500,15000,-200,9800]
total=0
for amount in sales:
    if amount <= 0:
        print("skipped invalid value{amount}")
        continue
    total+=amount
    print(f"total amount{amount}")
    if total>30000:
        break

if total>30000:
    print("target reached at{total}") 
else:
    print("target not reached at {total}")        

print(total)        
        
