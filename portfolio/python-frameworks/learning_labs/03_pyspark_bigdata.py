"""
LEARNING LAB: Big Data Validation with PySpark
==============================================
When data exceeds memory (GBs or TBs), Pandas/Polars crash. 
We use Apache Spark (PySpark).

Concepts:
- SparkSession
- RDDs vs DataFrames
- Distributed Processing

NOTE: To run this, you need Java installed. This script includes a try-catch block 
to just print concepts if Spark Environment isn't ready.
"""

import sys

try:
    from pyspark.sql import SparkSession
    from pyspark.sql.functions import col, sum as _sum
    SPARK_AVAILABLE = True
except ImportError:
    SPARK_AVAILABLE = False
    print("[!] PySpark not installed or Java missing. Install with 'pip install pyspark'")

def run_spark_demo():
    if not SPARK_AVAILABLE:
        return

    # 1. Initialize Spark Session (The entry point)
    print("\n[Spark] Initializing Session (this takes a moment)...")
    spark = SparkSession.builder \
        .appName("PortfolioDataValidation") \
        .getOrCreate()
        # .master("local[*]") \ # Use all cores

    # 2. Create Data (simulating a CSV read)
    data = [("James", "Sales", 3000),
            ("Anna", "Sales", 4600),
            ("Robert", "Sales", 4100),
            ("Maria", "Finance", 3000)]
    columns = ["Employee Name", "Department", "Salary"]
    
    df = spark.createDataFrame(data=data, schema=columns)
    
    print("[Spark] Schema:")
    df.printSchema()

    # 3. Validation Transformation
    # "Show me total salary by department where salary > 3500"
    print("[Spark] Running Aggregation...")
    
    result_df = df.filter(col("Salary") > 3500) \
        .groupBy("Department") \
        .agg(_sum("Salary").alias("Total_Salary"))
    
    result_df.show()
    
    spark.stop()

if __name__ == "__main__":
    print("--- PySpark Big Data Validation ---")
    if SPARK_AVAILABLE:
        run_spark_demo()
    else:
        print("Skipping execution. Please install Java 8/11 and pyspark to run.")
