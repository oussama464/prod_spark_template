import os
import shutil
import pandas as pd
import pandas.testing as pdt
from src.jobs import movies


class TestMoviesJob:
    def test_transform_data(self, spark_session):
        test_data = spark_session.createDataFrame(
            [(1, "Toy Story (1995)", "Adventure"),
             (160646, "Goat (2016)", "Drama")],
            ["movieId", "title", "genres"],
        )
        expected_data = spark_session.createDataFrame(
            [(1, "Toy Story", 1995), (160646, "Goat", 2016)],
            ["movieId", "title", "year"],
        ).toPandas()
        real_data = movies._transform_data(test_data).toPandas()
        # pdt.assert_frame_equal(real_data, expected_data, check_dtype=False)
        print(expected_data.head())
        print(real_data.head())
        pdt.assert_frame_equal(real_data, expected_data, check_dtype=False)
