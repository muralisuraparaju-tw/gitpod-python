from sparkutil import *
from constants import *

def read_abfss(spark, container_name, storage_account_name, file):
    set_default_abfss_params(spark)
    path = "abfss://"+container_name+"@"+storage_account_name+".dfs.core.windows.net/"+file
    print("Path:"+path)
    #TODO: Check jars
    spark.read.format("csv").load(path).show()
    