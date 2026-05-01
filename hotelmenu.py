#define menu of restaurant
menu={
    "pizza":120,
"burger": 30,
"coffee":10,
"chowmein":30,
"maggie":40,
"dosa": 60

}
#greet
print("hello good morning,welcome to cafe")
print("pizza:120\nburger: 30\ncoffee:10\nchowmein:30\nmaggie:40\ndosa: 60")
order_total = 0
item_1=input("what will you like to have:")
if item_1 in menu:
    order_total += menu[item_1]
    print(f"your item {item_1} is added")
else:
    print(f"plese order something else {item_1} not in menu")
another_order=input ("Dou what to order something else?(yes/no)")
if another_order == "yes":
    item_2=input("enter name of second order:")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"your item {item_2} is added")
    else:
      print(f"plese order something else {item_2} not in menu")  
print(f"The total amount of your bill is {order_total}")


