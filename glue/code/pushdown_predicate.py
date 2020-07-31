import sys
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.transforms import *
glueContext = GlueContext(SparkContext.getOrCreate())
persons_DyF = glueContext.create_dynamic_frame.from_catalog(database="parquettest", table_name="nileshparquet", push_down_predicate = "activity_day='2020-06-21'")
persons_DyF = glueContext.create_dynamic_frame.from_catalog(database="parquettest", table_name="nileshparquet")
persons_DyF.show()
