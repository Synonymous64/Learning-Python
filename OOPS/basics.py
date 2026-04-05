# l = [1,2,3]
# l.upper() list don't have any upper function

# s = 'hello'
# s.append("P"); string don't have any append function


class ATM:
    # constructor
    def __init__(self):
        self.pin = ''
        self.balance = 0
        print("hello!")

    def menu(self):
        choice = input("""how can i help you?
              Press 1: to create pin
              Press 2: to change pin
              Press 3: to check balance
              Press 4: to withdraw
              Press 5: to exit""")

        # if(choice == 1):
        #     # create pin
        # elif(choice == 2):
        #     # change pin
        # elif(choice == 2):
        #     # to check balance
        # elif(choice == 2):

        # elif(choice == 2):
        #     # to withdraw
        # else:
        #     exit()

    def create_pin(self):
        user_pin = input("enter your pin")
        self.pin = user_pin

        use_balance = input("enter your balance")
        self.balance = use_balance


obj = ATM()
obj.menu()
print(type(obj))

