from pyspark.sql import SparkSession

def test_spark():
    spark = SparkSession.builder.appName("Test Spark App").getOrCreate()
    df = spark.createDataFrame([(1, "value1"), (2, "value2")], ["id", "value"])
    df.write.csv("output.csv")
    df.show()

def main():
    print("Hello")
    test_spark()

main()