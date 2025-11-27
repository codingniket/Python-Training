class Amazon():

    def __init__(self, balance, amount):
        self.balance = balance

        self.amount = amount

    def payment(self):
        if self.amount > self.balance:
            print("Insufficient balance!")

            return

        print("\nPayment is successful!")

        print("Remaining Balance:", self.balance - self.amount)


class AmazonPayBalance(Amazon):

    def __init__(self, balance, amount, phone_number, password):
        super().__init__(balance, amount)

        self.phone_number = phone_number

        self.password = password


class UPI(Amazon):

    def __init__(self, balance, amount, upi_id, pin):
        super().__init__(balance, amount)

        self.upi_id = upi_id

        self.pin = pin


class Card(Amazon):

    def __init__(self, balance, amount, card_details, pin):
        super().__init__(balance, amount)

        self.pin = pin

        self.card_details = card_details


payment_option = input("Enter 1 for AmazonPay, 2 for UPI, 3 for Card: ")

if payment_option == "1":

    user = AmazonPayBalance(int(input("Enter Balance: ")), int(input("Enter Amount: ")),
                            int(input("Enter Phone Number: ")), input("Enter Password: "))

elif payment_option == "2":

    user = UPI(int(input("Enter Balance: ")), int(input("Enter Amount: ")), input("Enter UPI ID: "),
               input("Enter PIN "))

elif payment_option == "3":

    user = Card(int(input("Enter Balance: ")), int(input("Enter Amount: ")), input("Enter Card Details: "),
                input("Enter PIN: "))

else:

    print("Invalid option")

if user:
    user.payment()
