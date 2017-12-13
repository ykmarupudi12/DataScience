#!pip install thrift==0.9.3
#!pip install thrift_sasl
#!pip install impyla


import os
from pandas_highcharts.display import display_charts


# Specify IMPALA_HOST as an environment variable in your project settings
IMPALA_HOST = os.getenv('IMPALA_HOST', 'datacomdlas-dn0.australiasoutheast.cloudapp.azure.com')

import pandas
from impala.dbapi import connect
from impala.util import as_pandas

# Connect to Impala using Impyla
#
# * If you have not already established your Kerberos credentials in CDSW do so before running this script.
# * Remove auth_mechanism and use_ssl parameters on non-secure clusters.
conn = connect(host=IMPALA_HOST,
               port=21050)
#                             use_ssl=True)

# Get the available tables
cursor = conn.cursor()
cursor.execute('SHOW TABLES')

# Pretty output using Pandas
tables = as_pandas(cursor)
tables