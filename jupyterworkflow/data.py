import os
from urllib.request import urlretrieve
import pandas as pd

Fremont_URL = 'https://data.seattle.gov/api/views/65db-xm6k/rows.csv?accessType=DOWNLOAD'

def get_fremont_data(filename='Fremont.csv', url=Fremont_URL, force_download=False):
    
    """Download and cache the fremont data

    Parameters
    ------------
    filename : string (optional)
        location to save the data
    url : string (optional)
        web location of the data
    force_download : bool (optional)
        if True, force redownload of data

    Returns
    ------------
    data : pandas.DataFrame
        the fremont bridge data
    """

    if force_download or not os.path.exists(filename):     #==>check exists file in working directory
        urlretrieve(url, filename)
        
    data = pd.read_csv('Fremont.csv', index_col='Date')
    try:
        data.index = pd.to_datetime(data.index, format='%m/%d/%Y %I:%M:%S %p')
    except TypeError:
        data.index = pd.to_datetime(data.index)

    data.columns = ['East', 'West']
    data['Total'] =data['West'] + data['East']
    return data
    

