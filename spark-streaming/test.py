from pyspark.sql import SparkSession
from pyspark.sql.types import *
from pyspark.sql.functions import from_json, col


if __name__ == '__main__':
    spark = SparkSession \
        .builder \
        .appName("Stream Coinapi") \
        .getOrCreate()
    spark.sparkContext.setLogLevel('WARN')

    df = spark \
        .readStream \
        .format("kafka") \
        .option("kafka.bootstrap.servers", "localhost:9092") \
        .option("subscribe", "assets") \
        .load()

    df = df.selectExpr("CAST(value AS STRING)")

    df_schema = StructType([
            StructField("id", StringType(), True),
            StructField("rank", StringType(), True),
            StructField("symbol", StringType(), True),
            StructField("name", StringType(), True),
            StructField("maxSupply", StringType(), True),
            StructField("marketCapUsd", StringType(), True),
            StructField('volumeUsd24Hr', StringType(), True),
            StructField("priceUsd", StringType(), True),
            StructField("changePercent24hr", StringType(), True),
            StructField('vwap24Hr', StringType(),True)]
            )
    
    assets_df = df.select(from_json(col('value'), df_schema).alias('data'))\
                .select('data.*')

    assets_df.writeStream \
    .outputMode('update')\
    .format("console")\
    .start()\
    .awaitTermination()

