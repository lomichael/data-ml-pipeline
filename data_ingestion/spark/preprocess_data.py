from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("DataPreprocessing").getOrCreate()

df = spark.read.json("hdfs://localhost:9000/user/hadoopuser/input/datafile")
df = df.select("desired_column")  # Example preprocessing
df.write.csv("hdfs://localhost:9000/user/hadoopuser/output/preprocessed_data")

