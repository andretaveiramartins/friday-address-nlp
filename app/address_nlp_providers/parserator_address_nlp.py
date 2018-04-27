# Provider reference: https://github.com/datamade/usaddress

#Deprecated: Works well for US addresses and a few worldwide addresses but not too consistent
import usaddress

def process_address(address):
    
    address_tuple= usaddress.parse(address)
    #print (test[0][0])
    address_dict = dict((y, x) for x, y in address_tuple)
    print (address_dict)
    return {'street_name' : address_dict['SubaddressType'], 'street_number' : address_dict['SubaddressIdentifier']}

