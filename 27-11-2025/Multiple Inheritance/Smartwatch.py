class HealthDevice :
    def __init__(self,price,details):
        self.price = price
        self.details=details

    def show_feature(self):
        print(f'Your Health Device cost {self.price} and these are the feature {self.details}')


class NotificationDevice:
    def __init__(self,color,time):
        self.color = color
        self.time = time
    def show_details(self):
        print(f"Color of notification {self.color}  and time you got {self.time}")

class SmartWatch(NotificationDevice,HealthDevice):
    def __init__(self,price,details,color,time):
        HealthDevice.__init__(self,price,details)
        NotificationDevice.__init__(self,color,time)
    def display(self):
        self.show_feature()
        self.show_details()



x = SmartWatch(500,"Oxy Meter and Pulse","red","21 mins ago")
x.display()