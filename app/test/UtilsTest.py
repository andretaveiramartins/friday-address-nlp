import unittest
from .. import Utils
import os
import yaml

class UtilsTest(unittest.TestCase):

    def setUp(self):
        pass

    def test_get_yml_fileName_only(self):
        try:
            config = Utils.load_yml_config(os.path.join("config.yml"))
        except yaml.YAMLError as exc:
            self.assertFalse
        self.assertTrue
        
        
    def test_get_yml_relative_path(self):
        try:
            config = Utils.load_yml_config(os.path.join("..", "samples" ,"config.yml"))
        except yaml.YAMLError as exc:
            self.assertFalse
        self.assertTrue
        

#This will create a test suite and add test methods from the test case to execute
def test_suite():
    test_cases = ['test_get_yml_fileName_only', 'test_get_yml_relative_path']
    return unittest.TestSuite(map(UtilsTest, test_cases))

if __name__ == '__main__':
    test_suite = test_suite()
    unittest.TextTestRunner(verbosity=2).run(test_suite)