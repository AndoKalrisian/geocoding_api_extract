
import pandas as pd
from pandas.core.frame import DataFrame
import pytest

import geocoding_api_extract as geox

@pytest.fixture
def addr_data():
    return {'address': ['6021 CERVINUS RUN', "4008 VIVAS LN", "7612 CAYENNE LN"],
            'city': 'Austin',
            'state': 'TX'}
    

def test_extract_address_details_dataframe(addr_data):
    tmp_folder = "tmp"
    result = geox.extract_address_details(addr_data['address'], addr_data['city'], addr_data['state'],
                                          tmp_folder)
    
    # Assert
    assert type(result) == DataFrame
    
    
def test_extract_address_details_columns(addr_data):
    tmp_folder = "tmp"
    result = geox.extract_address_details(addr_data['address'], addr_data['city'], addr_data['state'],
                                          tmp_folder)

    # Assert
    assert result.columns.to_list() == ['address', 'state', 'county', 'tract', 'cent_lat', 'cent_lon',
                                        'us_zip']
    

def test_extract_address_details_data_01(addr_data):
    tmp_folder = "tmp"
    result = geox.extract_address_details(addr_data['address'], addr_data['city'], addr_data['state'],
                                          tmp_folder)

    # Assert
    assert result['tract'].to_list() == ['001914', '001914', '002312']


def test_extract_address_details_data_tmp_folder(addr_data):
    tmp_folder = "ZS:dkljftmp"
    result = geox.extract_address_details(addr_data['address'], addr_data['city'], addr_data['state'],
                                          tmp_folder)

    # Assert
    assert type(result) == DataFrame
    

def test_extract_address_details_data_addresses(addr_data):
    tmp_folder = "tmp"
    result = geox.extract_address_details(12, addr_data['city'], addr_data['state'],
                                          tmp_folder)

    # Assert
    assert type(result) == DataFrame
    

def test_extract_address_details_data_clean_result(addr_data):
    tmp_folder = "tmp"
    result = geox.extract_address_details(addr_data['address'], addr_data['city'], addr_data['state'],
                                          tmp_folder, clean_result=False)

    # Assert
    assert type(result) == DataFrame
    

def test_extract_address_details_data_reset(addr_data):
    tmp_folder = "tmp"
    result = geox.extract_address_details(addr_data['address'], addr_data['city'], addr_data['state'],
                                          tmp_folder, reset=True)

    # Assert
    assert type(result) == DataFrame
    
