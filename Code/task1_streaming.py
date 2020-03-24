from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.sql import SQLContext
from pyspark.sql.types import *
from pyspark.sql import Row

def importCSV():
    spark.read.format('csv').options(header='true', inferSchema='true').load('zipcodes.csv')

if __name__ == "__main__":
    importCSV()