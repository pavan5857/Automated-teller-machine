username='pavan'
password='python5857'
c_name=input("Enter your name:")
c_pass=str(input("Enter your password:"))
if c_name==username and c_pass==password:
    print('''
    1.Deposite
    2.Withdraw
    3.mini_statement
    4.exit
    ''')
    amount=50000
    option=int(input("select your option:"))
    if option==1:
        dep=int(input("Enter the amount"))
        amount+=dep
        print("Total amount:",amount)
    elif option==2:
        withd=int(input("enter the amount:"))
        amount-=withd
        print("total amount:",amount)
    elif option==3:
        print("====ATM====")
        print("username:",username)
        print("total amount:",amount)
        print("thanks for visiting")
    elif option==4:
        exit()
else:
    print("please enter correct login's")
