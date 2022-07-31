all:test build
test:
	cd tests && pytest
build:
	rm -rf ./dist && rm -rf libs/* && mkdir ./dist 
	pip install -r requirements.txt -t ./libs 
	cp ./main.py ./dist 
	cp ./config.ini ./dist 
	zip -r dist/jobs.zip jobs 
	zip -r dist/shared.zip shared 
	zip -r -D dist/libs.zip libs
setup_build:
	rm -rf dist build && python setup.py sdist bdist_wheel && unzip -l dist/*.whl && tar --list -f dist/*.tar.gz
build_devolop:
	pip install -e .
clean:
	rm -rf dist build
