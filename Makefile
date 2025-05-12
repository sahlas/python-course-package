# Execute the "targets" in this file with `make <target>` e.g., `make test`.
#
# You can also run multiple in sequence, e.g. `make clean lint test serve-coverage-report`

clean:
	bash run.sh clean

help:
	bash run.sh help

install:
	bash run.sh install

generate-project:
	bash run.sh generate-project


# write a github action workflow to execute the test target
test:
	bash run.sh test
	# bash run.sh test --coverage
	# bash run.sh test --coverage --html
	# bash run.sh test --coverage --html --xml
	# bash run.sh test --coverage --html --xml --json
	# bash run.sh test --coverage --html --xml --json --junit
	# bash run.sh test --coverage --html --xml --json --junit --junit-xml


# run our linting tools

lint:
	bash run.sh lint
	# bash run.sh lint --fix
	# bash run.sh lint --fix --all
	# bash run.sh lint --fix --all --check
	# bash run.sh lint --fix --all --check --diff
	# bash run.sh lint --fix --all --check --diff --verbose
	# bash run.sh lint --fix --all --check --diff --verbose --quiet
	# bash run.sh lint --fix --all --check --diff --verbose --quiet --max-line-length=120

