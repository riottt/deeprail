generate:
	./scripts/generate

check:
	./scripts/check

test:
	python3 -m unittest discover -s tests -v

build:
	python3 -m build

docs:
	./scripts/build-docs

dist:
	./scripts/build-dist

all: generate check test build
