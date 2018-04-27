import unittest
from .. import Utils
import os
from ..address_nlp_providers import custom_address_nlp
import yaml
import json

class CustomAddressNlpTest(unittest.TestCase):

    def setUp(self):
        self.test_data=None
        try:
            with open(os.path.join("samples" ,"address-nlp-test-data.json")) as file_stream:
                self.test_data = json.load(file_stream)
        except Exception as exc:
            print (exc)

    def test_process_address_mismatch_processed_source_address(self):
        """
        This method tests when the inputed source address differs from google output address
        """   
        for test_record in self.test_data:
            nlp_result = custom_address_nlp.process_address(test_record['address'])
            self.assertEqual(test_record['expected_result'],nlp_result)
            

    def test_process_address_not_found(self):
        """
        This method tests when google could not identify the address and parse it
        """ 
        error_message = {'error_message': 'We could extract the street number or street name from the informed address. This address will be manually analyzed.'}
        self.assertEqual(custom_address_nlp.process_address("SQS 316 Bloco E apto 105, Brasilia, DF, Brazil"),error_message)

#This will create a test suite and add test methods from the test case to execute
def test_suite():
    test_cases = ['test_process_address_mismatch_processed_source_address','test_process_address_not_found']
    return unittest.TestSuite(map(CustomAddressNlpTest, test_cases))

if __name__ == '__main__':
    test_suite = test_suite()
    unittest.TextTestRunner(verbosity=2).run(test_suite)