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
        result = google_maps_address_nlp.process_address("Guenthersburgallee 98 Frankfurt HE 60389")
        #expected_result = {'street':result['street'],'street_number':result['street_number']}
        expected_result = {'street': 'Günthersburgallee', 'state': 'Hessen', 'city': 'Frankfurt am Main', 'county': 'Darmstadt', 'country': 'Germany', 'postal_code': '60389', 'neighborhood': None, 'sublocality': 'Innenstadt', 'housenumber': None, 'postal_town': None, 'subpremise': None, 'latitude': 50.1286077, 'longitude': 8.7006328, 'location_type': 'RANGE_INTERPOLATED', 'postal_code_suffix': None, 'street_number': '98', 'address': 'Guenthersburgallee 98 Frankfurt HE 60389'}
        self.assertEqual(result,expected_result)

    def test_process_address_fr(self):   
        result = google_maps_address_nlp.process_address("115 bis rue Ordener 75018 PARIS CEDEX 18")
        expected_result = {'street': 'Rue Ordener', 'state': 'Île-de-France', 'city': 'Paris', 'county': 'Paris', 'country': 'France', 'postal_code': '75018', 'neighborhood': None, 'sublocality': None, 'housenumber': None, 'postal_town': None, 'subpremise': None, 'latitude': 48.8925348, 'longitude': 2.3433625, 'location_type': 'ROOFTOP', 'postal_code_suffix': None, 'street_number': '115', 'address': '115 bis rue Ordener 75018 PARIS CEDEX 18'}
        self.assertEqual(result,expected_result)
       
#This will create a test suite and add test methods from the test case to execute
def test_suite():
    test_cases = ['test_process_address_de','test_process_address_fr']
    return unittest.TestSuite(map(GoogleMapsAddressNlpTest, test_cases))

if __name__ == '__main__':
    test_suite = test_suite()
    unittest.TextTestRunner(verbosity=2).run(test_suite)