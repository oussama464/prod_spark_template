
## packaging pyspark for spark submitt 
### project folder structure 
* jobs: contains the jobs to run 
* shared: contains shared modules for the job 
* libs contains external libs and dependecies
* main.py our main program to submitt 


```
.
├── dist
│   ├── config.ini
│   ├── jobs.zip
│   ├── libs.zip
│   ├── main.py
│   └── shared.zip
├── Makefile
├── README.md
├── requirements.txt
├── setup.py
├── src
│   ├── config.ini
│   ├── data
│   ├── jobs
│   ├── libs
│   ├── main.py
│   └── shared
├── tests
│   ├── conftest.py
│   ├── jobs
│   └── pytest.ini

```
## spark submitt command 

```bash
cd dist && spark-submit --master yarn --py-files jobs.zip,shared.zip --files config.ini main.py  --job movies
```
in main.py the jobs to run are imported dynamically using import lib package 

```py

 job_module = importlib.import_module(f"jobs.{args.job}")
 job_module.run_job(spark, configs)

```

## tests 
to be able to run tests we build an src package using setup.py and pip install it in venv in develop mode ie (pip install -e .)

### final notes 
*  all commands to build this package are in a `Makefile`
* see also : [youtube](https://www.youtube.com/watch?v=Bp0XvA3wIXw&t=1370s) and [repo](https://github.com/pchrabka/PySpark-PyData)