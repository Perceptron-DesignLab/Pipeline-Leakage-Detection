import smtplib
import csv
import os
import time

path = os.getcwd() + "/file.csv"
Mailpath = os.getcwd() + "/body.csv"
Dry = "Dry"
Partial = "Partially Submerged."
Full = "Fully Submerged."
Obstacle = "Obstacles Present"
NoObstacle = "No Obstacles Present"
MidLevel = 500
ServerEmail = "perceptronfordesignlab@gmail.com"
ServerPassword = "Perceptron@1234"
MailSent = "Email Sent Successfully"
ReceiverMail = "hitmanabhishek089@gmail.com"
HeaderSubject = "Pipeline Leakage Detection"
Sensor_ids=[1,2,3]
Delay=30

class Connection:
    def __init__(self,path):
        self.path = path
        self.list_of_list = []
    def read_csv_file(self,path):
        with open(path,newline='') as f:
            csvreader = csv.reader(f)
            for row in csvreader:
                self.list_of_list.append(row)
                temp = self.list_of_list[-1]
                if(len(temp)==0):
                    self.list_of_list.pop()
                    
class cloud_manager():
    def __init__(self):
        self.sensor_id=None
    def create_lookup_table(self):
        self.lookup_table={}
        self.lookup_table[0]="at GODREJ WATERSIDE."
        self.lookup_table[1]="in front of COLLEGE MORE."
        self.lookup_table[2]="near WIPRO MORE."
        self.lookup_table[3]="near KARUNAMOYEE."
        self.lookup_table[4]="at CITY CENTRE 1."
    def get_water_sensor_data(self,water_data,sensor_id):
        self.water_sensor_data=water_data
        self.sensor_id=sensor_id
    def get_ir_sensor_data(self,ir_data,sensor_id):
        self.ir_sensor_data=ir_data
        self.sensor_id=sensor_id
    def process_water_sensor_data(self):
        if self.water_sensor_data==0:
            return Dry
        elif self.water_sensor_data < MidLevel:
            emailManager = Email_Manager()
            msg = MailBody[0][0] +'\n' + MailBody[0][1] + str(self.lookup_table[self.sensor_id - 1])+'.' +'\n' +MailBody[0][2] + Partial +'\n'+ MailBody[0][3]+'\n'+MailBody[0][4]
            message = 'Subject: {}\n\n{}'.format(HeaderSubject, msg)
            emailManager.send_email(ReceiverMail, message)
            return Partial
        else:
            emailManager = Email_Manager()
            msg = MailBody[0][0] +'\n' + MailBody[0][1] + str(self.lookup_table[self.sensor_id - 1])+'.' +'\n' +MailBody[0][2] + Full +'\n'+ MailBody[0][3]+'\n'+MailBody[0][4]
            message = 'Subject: {}\n\n{}'.format(HeaderSubject, msg)
            emailManager.send_email(ReceiverMail, message)
            Delay=5
            return Full
    

    def process_ir_sensor_data(self):
        if self.ir_sensor_data==1:
            emailManager = Email_Manager()
            msg = MailBody[1][0] + '\n' + MailBody[1][1] + str(self.lookup_table[self.sensor_id - 1]) + '\n' + MailBody[1][2] + '\n' + MailBody[1][3]
            message = 'Subject: {}\n\n{}'.format(HeaderSubject, msg)
            emailManager.send_email(ReceiverMail, message)
            return Obstacle
        else:
            return NoObstacle

class Email_Manager():
    def __init__(self):
        self.email_id = ServerEmail
        self.password = ServerPassword

    def send_email(self,recievers_email, message):
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(self.email_id, self.password)
        server.sendmail(self.email_id, recievers_email,message)
        server.quit()
        print(MailSent)

cloud_manager_1=cloud_manager()
cloud_manager_1.create_lookup_table()
def process_ir_sensor():
    for sensor_id in Sensor_ids:
        sensor_data=int(Data[sensor_id-1][0])
        cloud_manager_1.get_ir_sensor_data(sensor_data,sensor_id)
        print(cloud_manager_1.process_ir_sensor_data()," at ir sensor",sensor_id)

def process_water_sensor():
    for sensor_id in Sensor_ids:
        sensor_data=int(Data[sensor_id-1][1])
        cloud_manager_1.get_water_sensor_data(sensor_data,sensor_id)
        print("sensor",sensor_id,"is",cloud_manager_1.process_water_sensor_data())



while True :
    if(os.path.exists(path) and os.path.exists(Mailpath)):
        break


    

while True :
    Data = [[0,0],[0,0],[0,0]]
    MailBody =[["x","y"]]
    newConnection = Connection(path)
    newConnection.read_csv_file(path)
    Data = newConnection.list_of_list
    print(Data)
    newConnection1 = Connection(Mailpath)
    newConnection1.read_csv_file(Mailpath)
    MailBody = newConnection1.list_of_list
    process_ir_sensor()
    process_water_sensor()
    time.sleep(Delay)
