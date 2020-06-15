import smtplib

class cloud_manager():
    def __init__(self):
        self.sensor_id=None
    def create_lookup_table(self):
        self.lookup_table={}
        self.lookup_table[0]="192.168.0.0"
        self.lookup_table[1]="192.168.0.1"
        self.lookup_table[2]="192.168.0.2"
        self.lookup_table[3]="192.168.0.3"
        self.lookup_table[4]="192.168.0.4"
    def get_water_sensor_data(self,water_data,sensor_id):
        self.water_sensor_data=water_data
        self.sensor_id=sensor_id
    def get_ir_sensor_data(self,ir_data,sensor_id):
        self.ir_sensor_data=ir_data
        self.sensor_id=sensor_id
    def process_water_sensor_data(self):
        if self.water_sensor_data==0:
            return "Dry"
        elif self.water_sensor_data < 500:
            emailManager = Email_Manager()
            msg = "Partially Submerged at location " +  str(self.sensor_id) + " with ip address " + str(self.lookup_table[self.sensor_id])
            rcvem = "ankitkumar56666@gmail.com"
            emailManager.send_email(rcvem, msg)
            return "Partially Submerged"
        else:
            emailManager = Email_Manager()
            msg = "Fully Submerged at location " +  str(self.sensor_id) + " with ip address " + str(self.lookup_table[self.sensor_id])
            rcvem = "ankitkumar56666@gmail.com"
            emailManager.send_email(rcvem, msg)
            return "Fully Submerged"
    

    def process_ir_sensor_data(self):
        if self.ir_sensor_data==1:
            emailManager = Email_Manager()
            msg = "Obstacles present at location " +  str(self.sensor_id) + " with ip address " + str(self.lookup_table[self.sensor_id])
            rcvem = "ankitkumar56666@gmail.com"
            emailManager.send_email(rcvem, msg)
            return "obstacles present"
        else:
            return "obstacles not present"

class Email_Manager():
    def __init__(self):
        self.email_id = "perceptronfordesignlab@gmail.com"
        self.password = "Perceptron@1234"

    def send_email(self,recievers_email, message):
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(self.email_id, self.password)
        server.sendmail(self.email_id, recievers_email,message)
        server.quit()
        print("Email Sent Successfully")

cloud_manager_1=cloud_manager()
cloud_manager_1.create_lookup_table()
def process_ir_sensor():
    sensor_data=int(input())
    sensor_id=int(input())
    cloud_manager_1.get_ir_sensor_data(sensor_data,sensor_id)
    print(cloud_manager_1.process_ir_sensor_data())

def process_water_sensor():
    sensor_data=int(input())
    sensor_id=int(input())
    cloud_manager_1.get_water_sensor_data(sensor_data,sensor_id)
    print(cloud_manager_1.process_water_sensor_data())

switcher={
    1:process_ir_sensor,
    2:process_water_sensor
}
while True :
    print("1-Ir_sensor\n2-Water_sensor\n0-Exit")
    argument=int(input())
    if argument==1 or argument==2:
        func = switcher.get(argument)
        func()
    else :
        break
