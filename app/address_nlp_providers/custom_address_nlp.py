"""This module provides extra functionality on to of google Geocoding API. It tries to execute the google maps processor
and in case we identify the address wasn't processed correctly them we perform a manual resolution of the address. Google might
not resolve the address in case of a malformed address or in case the address doesn't exist or can't be matched in Google."""

from . import google_maps_address_nlp


def process_address(address):
    address_resolved =  google_maps_address_nlp.process_address(address)
    # When google can't process a message it returns on the payload only the address that was informed without street_number
    if 'street_number' in address_resolved.keys() and address_resolved['street'] is not None:
        address_without_street_number = None
        if address_resolved['street_number'] is not None:
            address_without_street_number = address.replace(_extract_street_number_from_adress(address),"").rstrip().lstrip().replace("   "," ").replace(",","")
            # TODO: Remove street address and trailing numbers
        return {'street':address_without_street_number,'street_number':address_resolved['street_number']}
    else:
        # TODO: Manual remediation strategy for Addresses not found should be in place for a real system
        return {'error_message':'We could extract the street number or street name from the informed address. This address will be manually analyzed.'}

def _extract_street_number_from_adress(address):
    """
    This function extracts the street number from the address and possible characters that are part of it
    """
    address_list = address.replace(",","").split(" ")
    
    