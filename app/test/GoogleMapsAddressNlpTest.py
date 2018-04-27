import unittest
from .. import Utils
import os
from ..address_nlp_providers import google_maps_address_nlp
import yaml
import json

class GoogleMapsAddressNlpTest(unittest.TestCase):

    def setUp(self):
        pass
        
    def test_process_address_de(self):   
        result = google_maps_address_nlp.process_address("Günthersburgallee 98 Frankfurt HE 60389")
        self.assertEqual(result['street'],'Günthersburgallee')
        self.assertEqual(result['street_number'],'98')

    def test_process_address_fr(self):   
        result = google_maps_address_nlp.process_address("115 rue Ordener 75018 PARIS CEDEX 18")
        street = result['street']
        street_number = result['street_number']
        self.assertEqual(street,'Rue Ordener')
        self.assertEqual(street_number,'115')
       
#This will create a test suite and add test methods from the test case to execute
def test_suite():
    test_cases = ['test_process_address_de','test_process_address_fr']
    return unittest.TestSuite(map(GoogleMapsAddressNlpTest, test_cases))

if __name__ == '__main__':
    test_suite = test_suite()
    unittest.TextTestRunner(verbosity=2).run(test_suite)