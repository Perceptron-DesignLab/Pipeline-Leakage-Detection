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
def ir_sensor_1():
    sensor_data=int(input())
    ir_sensor_1=ir_sensor_data_collection(sensor_data,1)
    wifi_manager_1=wifi_manager("192.168.0.1",1)
    wifi_manager_1.get_ir_sensor_data(ir_sensor_1.ir_data)
    print("data recieved in wifi_module is ",wifi_manager_1.ir_sensor_data)
    
def ir_sensor_2():
    sensor_data=int(input())
    ir_sensor_2=ir_sensor_data_collection(sensor_data,2)
    wifi_manager_2=wifi_manager("192.168.0.2",1)
    wifi_manager_2.get_ir_sensor_data(ir_sensor_2.ir_data)
    print("data recieved in wifi_module is ",wifi_manager_2.ir_sensor_data)

def water_sensor_1():
    sensor_data=int(input())
    water_sensor_1=water_sensor_data_collection(sensor_data,1)
    print("delay is ",water_sensor_1.get_delay()," minutes")
    wifi_manager_1=wifi_manager("192.168.0.1",1)
    wifi_manager_1.get_water_sensor_data(water_sensor_1.water_data)
    print("data recieved in wifi_module is ",wifi_manager_1.water_sensor_data)

def water_sensor_2():
    sensor_data=int(input())
    water_sensor_2=water_sensor_data_collection(sensor_data,2)
    print("delay is ",water_sensor_2.get_delay()," minutes")
    wifi_manager_2=wifi_manager("192.168.0.1",1)
    wifi_manager_2.get_water_sensor_data(water_sensor_2.water_data)
    print("data recieved in wifi_module is ",wifi_manager_2.water_sensor_data)

switcher={
    1:ir_sensor_1,
    2:ir_sensor_2,
    3:water_sensor_1,
    4:water_sensor_2,

}
while True :
    print("1-Ir_sensor_1\n2-Ir_sensor_2\n3-Water_sensor_1\n4-Water_sensor_2\n0-Exit")
    argument=int(input())
    if argument==1 or argument==2 or argument==3 or argument==4:
        func = switcher.get(argument)
        func()
    else :
        break

