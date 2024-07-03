from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("DataPreprocessing") \
    .config("spark.hadoop.fs.s3a.access.key", "YOUR_ACCESS_KEY") \
    .config("spark.hadoop.fs.s3a.secret.key", "YOUR_SECRET_KEY") \
    .config("spark.hadoop.fs.s3a.endpoint", "s3.amazonaws.com") \
    .getOrCreate()

df = spark.read.csv('s3a://my-ml-pipeline-bucket/data/file.csv', header=True, inferSchema=True)
processed_df = df.filter(df['column'] != 'value')  # Example preprocessing
processed_df.write.jdbc(url='jdbc:postgresql://localhost:5432/dbname', table='table_name', mode='overwrite')

