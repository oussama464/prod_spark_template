import importlib
import argparse
from pyspark.sql import SparkSession
#from parse import parse


def _parse_arguments():
    """Parse arguments provided by spark-submit command"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--job", required=True)
    return parser.parse_args()


def main():
    args = _parse_arguments()
    """ Main function executed by spark submit command"""
    configs_module = importlib.import_module(f"shared.config")
    configs = configs_module.get_configs("config.ini", "movies_app")
    spark = SparkSession.builder.appName(configs.get("app_name")).getOrCreate()

    job_module = importlib.import_module(f"jobs.{args.job}")
    job_module.run_job(spark, configs)


if __name__ == "__main__":
    main()
