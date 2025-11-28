class Notification:
    def send(self,message):
        print("Sending Message",message)

class EmailNotification(Notification):
    def send(self,message):
        print("Sending Email",message)

class SmsNotification(Notification):
    def send(self, message):
        print("Sending sms", message)

class PopNotification(Notification):
    def send(self, message):
        print("Beep you have a message", message)

n1 = EmailNotification()
n2 = SmsNotification()
n3 = PopNotification()
n1.send("Hello World")
n2.send("Why World")
n3.send("Which World")