#from lib.sparkutil import get_session
from pyspark.sql import SparkSession

STORAGE_ACCOUNT_NAME = "backstagepocdb"
STORAGE_ACCOUNT_KEY = "GUF8m5+SylVgb6W77vEXUcx9jTrypN2muHkpAn3izu02RGkdcsQORCdfZQrPmTyFT3Is3DWDdWFH+AStJJiXkw=="
CONTAINER_NAME = "hockey"

FILE_NAME = "abbrev.csv"
FULL_FILE_NAME = "wasbs://"+CONTAINER_NAME+"@"+STORAGE_ACCOUNT_NAME+".blob.core.windows.net/"+FILE_NAME
CSV_FILE_FORMAT = "csv"

#### Library functions -- START
def get_spark_session():
    spark = SparkSession.builder.appName("Test Spark App").getOrCreate()
    return spark

def init_adls():
    key = "fs.azure.account.key."+STORAGE_ACCOUNT_NAME+".blob.core.windows.net"
    spark = get_spark_session()
    spark.conf.set(key, STORAGE_ACCOUNT_KEY)

#### Library functions -- END

def read_csv_adls(file_name, file_format):
    spark = get_spark_session()
    df = spark.read.format(file_format)\
        .option('header', True)\
            .load(file_name)
    df.show()
    return df

def test_in_memory_spark():
    #spark = get_session()
    spark = get_spark_session()
    init_adls()
    df = spark.createDataFrame([(1, "value1"), (2, "value2")], ["id", "value"])
    df.write.csv("data/output.csv")
    df.show()
    return df

def test_adls():
    spark = SparkSession.builder.appName("Test Spark App").getOrCreate()
    init_adls()

def main():
    print("Hello")
    test_in_memory_spark()
    read_csv_adls(FULL_FILE_NAME, CSV_FILE_FORMAT)

main()