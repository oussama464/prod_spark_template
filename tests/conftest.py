from pytest import fixture
from pyspark.sql import SparkSession


@fixture(scope="session")
def spark_session():
    spark = SparkSession.builder.appName("testing_movies_etl").getOrCreate()
    yield spark
    spark.stop()
