from pyspark.sql import SparkSession

spark = SparkSession.builder.appName(
    "HW2 Fashion Boutique Pricing Analysis"
).getOrCreate()

df = spark.read.option("header", True).csv(
    "independent_boutiques_dehradun.csv"
)

df.show(10)

df.createOrReplaceTempView("boutiques")

result = spark.sql("""
    SELECT Price_Range, COUNT(*) AS count
    FROM boutiques
    GROUP BY Price_Range
""")

result.show()

spark.stop()
