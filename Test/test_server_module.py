from server_module import cloud_manager
import unittest

class test_cloud_manager(unittest.TestCase) :
    def test_process_water_sensor_data(self) :
        cloud_manager_1=cloud_manager()
        cloud_manager_1.create_lookup_table()
        cloud_manager_1.get_water_sensor_data(560,1)
        self.assertEqual(cloud_manager_1.process_water_sensor_data(),"Fully Submerged")

    def test_process_ir_sensor_data(self) :
        cloud_manager_1=cloud_manager()
        cloud_manager_1.create_lookup_table()
        cloud_manager_1.get_ir_sensor_data(1,1)
        self.assertEqual(cloud_manager_1.process_ir_sensor_data(),"obstacles present")
    
if __name__ == '__main__':
    unittest.main()