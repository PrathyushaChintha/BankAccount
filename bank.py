class Bankaccount:
    def __init__(self):
        self.Balance=0
        # self.owner=input()
        print("Account Created")



    def deposit(self):
        a =int(input("Enter the deposit amount"))
        # print(type(self.Balance))
        self.Balance+=a
        print("Updated Balance after deposit")
        return self.Balance

    def withdrawal(self):
        b=int(input("enter withdrawal amount"))
        self.Balance-= b
        print("Updated Balance after withdrawal")
        return self.Balance




    # if __name__=='__main__':
    #     if(withdrawal()>deposit()):
    #         print("Operation Failed")
    #     print("Successful")
acc= Bankaccount()
while(True):
    print("Please enter your choice")
    n=input()
    if(n=="exit"):
        break
    if(n=="deposit"):
        print(acc.deposit())
    elif(n=="withdrawal"):
        print(acc.withdrawal())
    else:
        print("You have selected wrong choice")