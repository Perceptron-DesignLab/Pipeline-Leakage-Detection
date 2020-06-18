import csv
import os
import threading
import time
import asyncio

MidLevel=500
NormalDelay=30
ReducedDelay=5
path =  os.getcwd() + "/file.csv"
Mailpath = os.getcwd() + "/body.csv"

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
            f.close()

    def read_csv_file(self,path):
        self.list_of_list = []
        with open(path,newline='') as f:
            csvreader = csv.reader(f)
            for row in csvreader:
                self.list_of_list.append(row)
                temp = self.list_of_list[-1]
                if(len(temp)==0):
                    self.list_of_list.pop()

    


class water_sensor_data_collection:
    def __init__(self,water_data,ida):
        self.water_data=water_data
        self.delay = NormalDelay
        self.ida = ida

    def get_water_sensor_data(self):
        return self.water_data

    def get_delay(self):
        if(self.water_data > MidLevel):
            self.delay = ReducedDelay
        else :
            self.delay = NormalDelay

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
    def __init__(self,sensor_id):
        self.sensor_id=sensor_id

    def get_water_sensor_data(self,water_data):
        self.water_sensor_data=water_data
    def get_ir_sensor_data(self,ir_data):
        self.ir_sensor_data=ir_data

setup_manager=setup_manager()

def delay(interval):
    time.sleep(interval)

def ir_sensor(id_sensor):
    sensor_id = id_sensor
    f=0
    while f!=1:
        sensor_data=int(input("Enter IR Sensor data : "))
        if sensor_data==0 or sensor_data==1:
            f=1
        else:
            print("Invalid data")
    Data[sensor_id-1][0] = sensor_data
    ir_sensor_1=ir_sensor_data_collection(sensor_data,sensor_id)
    wifi_manager_1=wifi_manager(sensor_id)
    wifi_manager_1.get_ir_sensor_data(ir_sensor_1.ir_data)
    print("data recieved in wifi_module is ",wifi_manager_1.ir_sensor_data)
    newConnection = Connection(Data,path)
    newConnection.writing_data_to_csv_file()
    return sensor_data
    

def water_sensor(id_sensor):
    sensor_id = id_sensor
    f=0
    while f!=1:
        sensor_data=int(input("Enter Water Sensor data : "))
        if sensor_data>=0 and sensor_data<=1024:
            f=1
        else:
            print("Invalid data")
    Data[sensor_id-1][1] = sensor_data
    water_sensor_1=water_sensor_data_collection(sensor_data,sensor_id)
    print("delay is ",water_sensor_1.get_delay()," minutes")
    wifi_manager_1=wifi_manager(1)
    wifi_manager_1.get_water_sensor_data(water_sensor_1.water_data)
    print("data recieved in wifi_module is ",wifi_manager_1.water_sensor_data)
    newConnection = Connection(Data,path)
    newConnection.writing_data_to_csv_file()
    return sensor_data
    

def sensor(sensor_id,f):
    ir_data=ir_sensor(sensor_id)
    f=0
    water_data=water_sensor(sensor_id)
    if water_data>500:
        for i in range(0,5):
            f=1
            time.sleep(5)
            water_data=water_sensor(sensor_id)
            if water_data<500:
                f=0
                break
    return f





flag = 0
id_sensor = int(input("Enter Sensor Id : "))
while True :
    
    if(os.path.exists(path)):
        temp=[]
        newConnection = Connection(temp, path)
        newConnection.read_csv_file(path)
        Data = newConnection.list_of_list
    else:
        Data = [[0,0],[0,0],[0,0]]
        newConnection2 = Connection(Data,path)
        newConnection2.writing_data_to_csv_file()
        newConnection3 = Connection(MailBody,Mailpath)
        newConnection3.writing_data_to_csv_file()


    f=0
    f=sensor(id_sensor,f)
    if f==0:
        time.sleep(30)
    else:
        f=1


    
