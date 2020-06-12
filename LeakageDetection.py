
#imports 
import random
#from threading import Thread
import threading
import time
import smtplib
#import ray


class Setup_manager:
    def pin_mode(self, water_sensor_pin, ir_sensor_pin):
        self.water_sensor_pin = water_sensor_pin
        self.ir_sensor_pin = ir_sensor_pin
        print("Pins Callibrated Successfully !!")

    def get_delay(self, flag, delay):
        self.delay = delay
        if(delay == 30):
            self.flag = True
        else:
            self.flag = False

        print("Default delay set to ", self.delay, " seconds !!")


class water_sensor_data_collection:

    def __init__(self,water_data,ida):
        self.water_data=water_data
        self.delay = 30
        self.ida = ida

    def get_water_sensor_data(self):
        return self.water_data

    def get_delay(self):
        if(self.water_data > 400):
            self.delay = 5
        else :
            self.delay = 30

        return self.delay

    def get_id(self):
        return self.ida

class ir_sensor_data_collection:

    def __init__(self,ir_data,ida):
        self.ir_data=ir_data
        self.ida = ida

    def get_ir_sensor_data(self):
        return self.ir_data

    def get_id(self):
        return self.ida

class wifi_manager():
    def __init__(self,ip_address,sensor_id):
        self.ip_address=ip_address
        self.sensor_id=sensor_id

    def get_water_sensor_data(self,water_data):
        self.water_sensor_data=water_data
    def get_ir_sensor_data(self,ir_data):
        self.ir_sensor_data=ir_data

def delay(interval):
    time.sleep(interval)


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


def sensor_1(water_sensor):
    while True :
        wifi_managers[water_sensor.get_id()].get_water_sensor_data(water_sensor.get_water_sensor_data())
        cloud_manager.get_water_sensor_data(wifi_managers[water_sensor.get_id()].water_sensor_data,water_sensor.get_id())
        message=cloud_manager.process_water_sensor_data()
        print("WATER SENSOR ID : ", water_sensor.get_id()," READING : ",water_sensor.get_water_sensor_data(), " DELAY : ", water_sensor.get_delay()," message : ",message,"\n","--------------------------------------------------------")
        delay(water_sensor.get_delay())
        water_sensor.water_data = random.choice(water_sensor_reading_values)

def irsensor(ir_sensor):
    while True:
        wifi_managers[ir_sensor.get_id()].get_ir_sensor_data(ir_sensor.get_ir_sensor_data())
        print()
        cloud_manager.get_ir_sensor_data(wifi_managers[ir_sensor.get_id()].ir_sensor_data,ir_sensor.get_id())
        message=cloud_manager.process_ir_sensor_data()
        print("IR SENSOR ID : ", ir_sensor.get_id()," READING : ",ir_sensor.get_ir_sensor_data(), " DELAY : 30 message : ",message,"\n","------------------------------------------------------- ")
        delay(30)
        ir_sensor.ir_data = random.choice(ir_sensor_reading_values)

setup_manager = Setup_manager()
setup_manager.pin_mode(1,2)
setup_manager. get_delay(0,30)

wifi_managers=[]
wifi_managers.append(wifi_manager("192.168.0.0",0))
wifi_managers.append(wifi_manager("192.168.0.1",1))
wifi_managers.append(wifi_manager("192.168.0.2",2))
wifi_managers.append(wifi_manager("192.168.0.3",3))
wifi_managers.append(wifi_manager("192.168.0.4",4))


cloud_manager=cloud_manager()
cloud_manager.create_lookup_table()
#Creating Biased Random number generators to simulate real life inputs
water_sensor_reading_values = [0 for i in range(0,500)] + random.sample([j for j in range(1,500)],25) + random.sample([k for k in range(600,1025)],25)
ir_sensor_reading_values = [0 for i in range(0,100)] + [1 for j in range(0,10)]
water_sensor_reading_values = random.sample(water_sensor_reading_values, len(water_sensor_reading_values))
ir_sensor_reading_values = random.sample(ir_sensor_reading_values, len(ir_sensor_reading_values))

ir_sensor_0 = ir_sensor_data_collection(random.choice(ir_sensor_reading_values),0)
ir_sensor_1 = ir_sensor_data_collection(random.choice(ir_sensor_reading_values),1)
ir_sensor_2 = ir_sensor_data_collection(random.choice(ir_sensor_reading_values),2)
ir_sensor_3 = ir_sensor_data_collection(random.choice(ir_sensor_reading_values),3)
ir_sensor_4 = ir_sensor_data_collection(random.choice(ir_sensor_reading_values),4)

water_sensor_0 = water_sensor_data_collection(random.choice(water_sensor_reading_values),0)
water_sensor_1 = water_sensor_data_collection(random.choice(water_sensor_reading_values),1)
water_sensor_2 = water_sensor_data_collection(random.choice(water_sensor_reading_values),2)
water_sensor_3 = water_sensor_data_collection(random.choice(water_sensor_reading_values),3)
water_sensor_4 = water_sensor_data_collection(random.choice(water_sensor_reading_values),4)

t1 = threading.Thread(target=sensor_1, args = (water_sensor_0,), name='t1')
t2 = threading.Thread(target=sensor_1, args = (water_sensor_1,), name='t2')
t3 = threading.Thread(target=sensor_1, args = (water_sensor_2,), name='t3')
t4 = threading.Thread(target=sensor_1, args = (water_sensor_3,), name='t4')
t5 = threading.Thread(target=sensor_1, args = (water_sensor_4,), name='t5')

t6 = threading.Thread(target=irsensor, args = (ir_sensor_0,), name='t6') 
t7 = threading.Thread(target=irsensor, args = (ir_sensor_1,), name='t7')
t8 = threading.Thread(target=irsensor, args = (ir_sensor_2,), name='t8')
t9 = threading.Thread(target=irsensor, args = (ir_sensor_3,), name='t9')
t10 =threading.Thread(target=irsensor, args = (ir_sensor_4,), name='t10') 

#starting threads 

t1.start() 
t2.start()
t3.start()
t4.start()
t5.start()

t6.start() 
t7.start()
t8.start()
t9.start()
t10.start()

