import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql import DataFrame, Row
import datetime
from awsglue import DynamicFrame
from pyspark.sql.types import StructType

sc = SparkContext.getOrCreate()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
userSchema = StructType().add("name", "string").add("age", "integer")
csvDF = spark \
    .readStream \
    .option("sep", ",").option("checkpointLocation", "s3://rndbucket/checkpoint10/") \
    .schema(userSchema) \
    .csv("s3://rndbucket/sparkstructuredstreaming/")

csvDF.writeStream \
  .format("csv").option("format","append").option("checkpointLocation","s3://rndbucket/checkpoint10/").option("path","s3://rndbucket/sparkstructuredstreamingout10/") \
  .trigger(once=True).outputMode("append") \
  .start()

spark.streams.awaitAnyTermination()
