build:
	python3 -m build

clean:
	rm -rf dist/ *.egg-info

doc:
	pdoc3 .

ci:
	python -m pytest tests/

run:
	uvicorn sentinelnet:app --reload

test:
	python -m pytest tests/

lint:
	python -m flake8 sentinelnet/

bench:
	locust -f benchmarks/>
