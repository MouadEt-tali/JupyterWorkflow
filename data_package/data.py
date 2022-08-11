import os
from urllib.request import urlretrieve
import pandas as pd

URL = "https://data.seattle.gov/api/views/65db-xm6k/rows.csv?accessType=DOWNLOAD"

def get_fremont_data(filename='Fremont.csv',url=URL, force_download= False):
    """Download and cache Fremont data
       Parameters
       -----------
      filename : string 
       url : string
      Returns
       -----------
      data : dataframe
	"""
    if force_download or not os.path.exists(filename):
        urlretrieve(URL,filename)
    data = pd.read_csv(filename, index_col = "Date", parse_dates=['Date'])
    data.columns = ["Total","East","West"]
    return data