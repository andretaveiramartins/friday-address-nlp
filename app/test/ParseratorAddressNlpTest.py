import unittest
from .. import Utils
import os
from ..address_nlp_providers import parserator_address_nlp
import yaml
import json

class ParseratorAddressNlpTest(unittest.TestCase):

    def setUp(self):
        pass
        
    def test_process_address_simple(self):   
        result = parserator_address_nlp.process_address("Günthersburgallee 98 Frankfurt HE 60389")
        expected_result = {'street_name': 'Günthersburgallee', 'street_number': '98'}
        self.assertEqual(result,expected_result)

    def test_process_address_complicated(self):   
        result = parserator_address_nlp.process_address("Auf der Vogelwiese 23 b")
        expected_result = {'street_name': 'Auf der Vogelwiese', 'street_number': '23 b'}
        self.assertEqual(result,expected_result)
    
    def test_process_address_other_countries(self):   
        result = parserator_address_nlp.process_address("200 Broadway Av")
        expected_result = {'street_name': 'Broadway Av', 'street_number': '200'}
        self.assertEqual(result,expected_result)
#This will create a test suite and add test methods from the test case to execute
def test_suite():
    test_cases = ['test_process_address_simple','test_process_address_complicated','test_process_address_other_countries']
    return unittest.TestSuite(map(ParseratorAddressNlpTest, test_cases))

if __name__ == '__main__':
    test_suite = test_suite()
    unittest.TextTestRunner(verbosity=2).run(test_suite)