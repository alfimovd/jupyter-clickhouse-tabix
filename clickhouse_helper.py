import requests
import pandas as pd
from io import StringIO

USER = 'default'
PASS = ''

HOST = 'http://clickhouse:8123'

#request to clickhouse
def get_ch_data(query, host=HOST, connection_timeout = 1500, **kwargs):
    params = kwargs
    r = requests.post(host, params = params, auth=(USER, PASS), timeout = connection_timeout, data = query)
    if r.status_code == 200:
        return r.text
    else:
        raise ValueError(r.text)

#load data to pandas data frame
def get_clichouse_df(query, host=HOST, connection_timeout = 1500):
    data = get_ch_data(query, host, connection_timeout)
    df = pd.read_csv(StringIO(data), sep = '\t')
    return df