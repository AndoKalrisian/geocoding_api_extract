# geocoding-api-extract

This package makes it easy to connect to the [US GeoCoding api](https://geocoding.geo.census.gov/) and extract data from a large set of addresses.  It batches up the request for querying the api and returns the results in a Pandas DataFrame as a result.  The US geocoding api does accept batches but it does not work unless you have more address details like zipcode.  This script allows you to look up address details using only street address, city, and state.

# Install

```
pip install geocoding_api_extract
```

# Usage 

The following code will retrieve a DataFrame with the following columns: ['address', 'state', 'county', 'tract', 'cent_lat', 'cent_lon','us_zip'].

```
import geocoding_api_extract as geox

tmp_folder = "tmp"

addr_data = {'address': ['6021 CERVINUS RUN', "4008 VIVAS LN", "7612 CAYENNE LN"],
             'city': 'Austin',
             'state': 'TX'}

result = geox.extract_address_details(addr_data['address'], addr_data['city'], addr_data['state'],
                                      tmp_folder)

geox.remove_tmp_files('Austin', 'TX', 'tmp')
```

I have also included a larger sample to try this out in the 'sample_data' folder.
```
import pandas as pd

import geocoding_api_extract as geox

tmp_folder = "tmp"

df = pd.read_parquet('sample_data/addresses_sample.parquet.gzip')

addresses = df['address']
city = 'Austin'
state = 'TX'

result = geox.extract_address_details(addresses, city, state,
                                      tmp_folder)

geox.remove_tmp_files('Austin', 'TX', 'tmp')
```
