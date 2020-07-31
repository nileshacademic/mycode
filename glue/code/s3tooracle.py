sudo wget -P /usr/lib/sqoop/lib/ http://www.datanucleus.org/downloads/maven2/oracle/ojdbc6/11.2.0.3/ojdbc6-11.2.0.3.jar
pyspark --jars /usr/lib/sqoop/lib/ojdbc6-11.2.0.3.jar
df = spark.read.parquet("s3://rndbucket/sqoopparquet1/XE/TEST/bef151b3-5115-4516-92e9-9e0e84d5f351.parquet")
df.write.format("jdbc").option("url", "jdbc:oracle:thin:@172.31.31.78:1521:XE").option("dbtable", "TEST").option("user", "xx").option("password", "xx").option("driver", "oracle.jdbc.OracleDriver").mode("append").save()

jdbcDF = spark.read.format("jdbc").option("url", "jdbc:oracle:thin:@172.31.31.78:1521:XE").option("dbtable", "TEST").option("user", "xx").option("password", "xx").option("driver", "oracle.jdbc.OracleDriver").load()

Glue

###
import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

## @params: [JOB_NAME]
args = getResolvedOptions(sys.argv, ['JOB_NAME'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)
df = spark.read.parquet("s3://rndbucket/sparkparquetoutput/")
df.write.format("jdbc").option("url", "jdbc:oracle:thin:@172.31.31.78:1521:XE").option("dbtable", "TEST").option("user", "xx").option("password", "xx").option("driver", "oracle.jdbc.OracleDriver").mode("append").save()
job.commit()
###

https://aws.amazon.com/blogs/big-data/how-to-access-and-analyze-on-premises-data-stores-using-aws-glue/
