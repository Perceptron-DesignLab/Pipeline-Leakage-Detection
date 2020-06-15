from pipeline_leakage_detection import *
import unittest
class test_water_sensor_data_collection(unittest.TestCase):
    
    def test_get_water_sensor_data(self):
        water_sensor=water_sensor_data_collection(0,1)
        expt_ans=0
        self.assertEqual(water_sensor.get_water_sensor_data(),expt_ans)

        water_sensor=water_sensor_data_collection(1024,1)
        expt_ans=1024
        self.assertEqual(water_sensor.get_water_sensor_data(),expt_ans)
    def test_get_delay(self):
        water_sensor=water_sensor_data_collection(0,1)
        expt_ans=30
        self.assertEqual(water_sensor.get_delay(),expt_ans)

        water_sensor=water_sensor_data_collection(450,1)
        expt_ans=5
        self.assertEqual(water_sensor.get_delay(),expt_ans)

class test_ir_sensor_data_collection(unittest.TestCase):
    
    def test_get_ir_sensor_data(self):
        ir_sensor=ir_sensor_data_collection(0,1)
        expt_ans=0
        self.assertEqual(ir_sensor.get_ir_sensor_data(),expt_ans)

        ir_sensor=ir_sensor_data_collection(1,1)
        expt_ans=1
        self.assertEqual(ir_sensor.get_ir_sensor_data(),expt_ans)

class test_wifi_manager(unittest.TestCase):
    def test_get_water_sensor_data(self):
        wifi_module=wifi_manager("192.168.0.1",1)
        wifi_module.get_water_sensor_data(1024)
        expt_ans=1024
        self.assertEqual(wifi_module.water_sensor_data,expt_ans)

    def test_get_ir_sensor_data(self):
        wifi_module=wifi_manager("192.168.0.1",1)
        wifi_module.get_ir_sensor_data(1)
        expt_ans=1
        self.assertEqual(wifi_module.ir_sensor_data,expt_ans)

if __name__ == '__main__':
    unittest.main()
