# tamrin 3-1
# build an automatic pizza order program:
print(
    "Small Pizza: $15 \n Medium Pizza: $20 \n Large Pizza: $25 \n Large Pizza: $25 \n Pepperoni for Small Pizza: +$2 \n Pepperoni for Medium or Large Pizza: +$3 \n Extra cheese for any size pizza: + $1 ")
bill = 0
size = input("What size pizza do you want? Small Pizza=s  Medium Pizza=m  Large Pizza=l :: ")
if size == 's':
    bill += 15
    print(bill)
elif size == 'm':
    bill += 20
    print(bill)
elif size == 'l':
    bill += 25
    print(bill)
add_Pepperoni=input("Do you want pepperoni? yes  no  :")
if add_Pepperoni == "yes" and size == "s":
    bill += 2
    print(bill)
elif add_Pepperoni == "yes" or size == "m" and size == "l" :
    bill += 3
    print(bill)
else:
    bill += 0
    print(bill)
extra_cheese = input("Would you like extra cheese? yes  no ")
if extra_cheese == "yes":
    bill += 1
else:
    bill += 0
final_bill = bill
print("final_bill :", final_bill)
