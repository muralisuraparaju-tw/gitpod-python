from pyspark.sql import SparkSession
from constants import *

def get_spark():
    spark = SparkSession.builder.appName("Test Spark App").getOrCreate()
    print(">>>>Successfully created spark session")
    return spark

def set_abfss_params(spark, storage_account_name, directory_id, client_id, client_secret):
    spark.conf.set("fs.azure.account.auth.type."+storage_account_name+".dfs.core.windows.net", "OAuth")
    spark.conf.set("fs.azure.account.oauth.provider.type."+storage_account_name+".dfs.core.windows.net",  "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider")
    spark.conf.set("fs.azure.account.oauth2.client.id."+storage_account_name+".dfs.core.windows.net", client_id)
    spark.conf.set("fs.azure.account.oauth2.client.secret."+storage_account_name+".dfs.core.windows.net", client_secret)
    spark.conf.set("fs.azure.account.oauth2.client.endpoint."+storage_account_name+".dfs.core.windows.net", "https://login.microsoftonline.com/"+directory_id+"/oauth2/token")
    print(">>>>Set abfss params")

def set_default_abfss_params(spark):
    set_abfss_params(spark, STORAGE_ACCOUNT_NAME, DIRECTORY_ID, CLIENT_ID, CLIENT_SECRET)
    spark.conf.set("fs.azure.createRemoteFileSystemDuringInitialization", "false")