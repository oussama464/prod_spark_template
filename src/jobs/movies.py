from pyspark.sql import functions as F


# read data
def _extract_data(spark, configs):
    raw_df = (
        spark.read.format("csv")
        .option("header", "true")
        .option("inferSchema", "true")
        .load(f"{configs.get('source_data_path')}/movies.csv")
    )
    return raw_df


# transform data
def _transform_data(raw_df):
    transformed_df = raw_df.select(
        F.col("movieId"),
        F.expr("substring(title,1,length(title)-6)").alias("title"),
        F.col("title").substr(-5, 4).alias("year"),
    )
    return transformed_df


# extract write data
def _load_data(transformed_df, configs):
    transformed_df.write.mode("overwrite").parquet(
        f"{configs.get('output_data_path')}/movies"
    )


def run_job(spark, configs):
    """run movies job"""
    _load_data(_transform_data(_extract_data(spark, configs)), configs)
