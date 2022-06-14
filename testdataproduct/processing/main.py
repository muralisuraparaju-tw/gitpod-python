from sparkutil import *
from constants import *
from storageutil import *
import sys

def main(argv):
    spark = get_spark()
    read_abfss(spark, CONTAINER_NAME, STORAGE_ACCOUNT_NAME, FILE_NAME)

# Flask end point
if __name__ == "__main__":
   main(sys.argv[1:])