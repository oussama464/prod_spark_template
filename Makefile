all:test build
test:
	cd tests && pytest
build:
	rm -rf ./dist && rm -rf ./src/libs/* && mkdir ./dist 
	pip install -r requirements.txt -t ./src/libs 
	cp ./src/main.py ./dist 
	cp ./src/config.ini ./dist 
	zip -r dist/jobs.zip ./src/jobs 
	zip -r dist/shared.zip ./src/shared 
	zip -r -D dist/libs.zip ./src/libs
setup_build:
	rm -rf dist build && python setup.py sdist bdist_wheel && unzip -l dist/*.whl && tar --list -f dist/*.tar.gz
build_devolop:
	pip install -e .
clean:
	rm -rf dist build
