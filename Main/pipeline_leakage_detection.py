import csv
import os

path =  os.getcwd() + "/file.csv"
Mailpath = os.getcwd() + "/body.csv"
Data = [[0,0],[0,0]]
MailBody = [['Dear Sir,','It has come to attention to our monitoring system that a leakage has been detected at system present ','The type of leakage has been found to be ','Kindly bring your attention.','Thanks & Regards'],
            ['Dear Sir,','It has come to attention to our monitoring system that an obstacle has been detected at system present ','Kindly bring your attention.','Thanks & Regards']
            ]

class setup_manager:
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

class Connection:
    def __init__(self,list_of_list,path):
        self.list_of_list = list_of_list
        self.path = path
    def writing_data_to_csv_file(self):
        with open(self.path,"w") as f:
            writer = csv.writer(f)
            writer.writerows(self.list_of_list)


class water_sensor_data_collection:
    def __init__(self,water_data,ida):
        self.water_data=water_data
        self.delay = 30
        self.ida = ida

    def get_water_sensor_data(self):
        return self.water_data

    def get_delay(self):
        if(self.water_data > 500):
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

setup_manager=setup_manager()

def ir_sensor():
    sensor_id = int(input("Enter IR Sensor Id : "))
    sensor_data=int(input("Enter IR Sensor data : "))
    Data[sensor_id-1][0] = sensor_data
    ir_sensor_1=ir_sensor_data_collection(sensor_data,sensor_id)
    wifi_manager_1=wifi_manager("192.168.0.1",sensor_id)
    wifi_manager_1.get_ir_sensor_data(ir_sensor_1.ir_data)
    print("data recieved in wifi_module is ",wifi_manager_1.ir_sensor_data)
    

def water_sensor():
    sensor_id = int(input("Enter Water Sensor Id : " ))
    sensor_data=int(input("Enter Water Sensor Data : "))
    Data[sensor_id-1][1] = sensor_data
    water_sensor_1=water_sensor_data_collection(sensor_data,sensor_id)
    print("delay is ",water_sensor_1.get_delay()," minutes")
    wifi_manager_1=wifi_manager("192.168.0.1",1)
    wifi_manager_1.get_water_sensor_data(water_sensor_1.water_data)
    print("data recieved in wifi_module is ",wifi_manager_1.water_sensor_data)



switcher={
    1:ir_sensor,
    2:water_sensor,

}
flag = 0
while True :
    print("1-Ir_sensor\n2-Water_sensor\n0-Exit")
    argument=int(input())
    if argument==1 or argument==2 :
        func = switcher.get(argument)
        func()
    else :
        if flag == 0:
            newConnection1 = Connection(MailBody,Mailpath)
            newConnection1.writing_data_to_csv_file()
            flag = 1

        newConnection = Connection(Data,path)
        newConnection.writing_data_to_csv_file()
        break

