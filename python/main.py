import sys
from pyspark.sql import SparkSession,SQLContext

spark = SparkSession.builder.appName("PythonScalaUDF").getOrCreate()
spark.range(1, 1000000).createOrReplaceTempView("test")

def call_python_udf_sql():
  from my_udf.functions import square, isprime
  print("\nCalling Python UDF with SQL")
  spark.udf.register("squareWithPython", square)
  spark.udf.register("isprime_py", isprime)
  spark.sql("select id, squareWithPython(id) as square_sql, isprime_py(id) as isprime_n from test").show()

def call_python_udf_df():
  print("Calling Python UDF with DataFrame")
  from pyspark.sql.functions import udf
  from my_udf.functions import square, isprime
  square_udf = udf(square)
  isprime_udf = udf(isprime)
  # or more type-safe
  # from pyspark.sql.types import LongType
  # square_udf = udf(square, LongType())
  df = spark.table("test")
  df.select("id", square_udf("id").alias("square_df"), isprime_udf("id").alias("isprime_n")).show()

def call_scala_udf_sql():
  print("Calling Scala UDF with SQL")
  sqlContext = SQLContext(spark.sparkContext)
  spark._jvm.com.databricks.solutions.udf.Functions.registerFunc(sqlContext._jsqlContext,"cube")
  spark._jvm.com.databricks.solutions.udf.Functions.registerFunc2(sqlContext._jsqlContext, "isprime")
  spark.sql("select id, cube(id) as cube_sql_scala, isprime(id) as isprime_n from test").show()

if __name__ == "__main__":
  call_python_udf_sql()
  call_python_udf_df()
  call_scala_udf_sql()
