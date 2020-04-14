price= {"Paracetamol": 2.50, "alcohol":4.50, "Nicotine": 3.50, "Caffine": 1.99}
Basket={}
print("welcome to Bewts drug store!\n The list below are the products we currently offer for sale:\n1, Paracetamol:2.50£ \n2, Alcohol:4.50\n3, Nicotine:3.50\n4, Caffine:1.99")
buy_another = 1
total_amount, total=0,0

while buy_another !=0:
    option=int(input("would you like to purchase any of the items? "))
    if option ==1:
        quantity= int(input("please enter how many paracetamols you would like to purchase: "))
        total= quantity * 2.50
        print("Your total is: "+str(total))

    elif option ==2:
        quantity= int(input("please enter how much alcohol you would like to purchase: "))
        total = quantity*4.50
        print("Your total is: "+str(total))
    elif option ==3:
        quantity= int(input("please enter how much nicotine you would like to purchase: "))
        total = quantity*3.50
        print("Your total is: "+str(total))
    elif option ==4:
        quantity= int(input("please enter how much caffine you would like to purchase: "))
        total = quantity*1.99
        print("Your total is: "+str(total))
    total_amount+=total
    buy_another= int(input("Would you like tp purchase another item? Enter Yes(1) or No (0):"))
print("Your total for your basket is: ",total_amount)
