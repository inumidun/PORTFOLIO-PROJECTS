import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

args = getResolvedOptions(sys.argv, ["JOB_NAME"])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args["JOB_NAME"], args)

# Script generated for node Amazon S3
AmazonS3_node1701615393628 = glueContext.create_dynamic_frame.from_options(
    format_options={
        "quoteChar": '"',
        "withHeader": True,
        "separator": ",",
        "optimizePerformance": False,
    },
    connection_type="s3",
    format="csv",
    connection_options={
        "paths": ["s3://dev-de-on-youtube-raw/youtube/raw_statistics/"],
        "recurse": True,
    },
    transformation_ctx="AmazonS3_node1701615393628",
)

# Script generated for node Amazon S3
AmazonS3_node1701615692425 = glueContext.write_dynamic_frame.from_options(
    frame=AmazonS3_node1701615393628,
    connection_type="s3",
    format="glueparquet",
    connection_options={
        "path": "s3://dev-de-on-youtube-clean/youtube/raw_statistics/",
        "partitionKeys": [],
    },
    format_options={"compression": "snappy"},
    transformation_ctx="AmazonS3_node1701615692425",
)

job.commit()
