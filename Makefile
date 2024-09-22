.PHONY: all push run download install

all: run

run:
	@mpremote run src/main.py

push:
	@echo "Pushing code to the board..."
	@mpremote cp src/secrets.py :secrets.py
	@mpremote cp src/main.py :main.py

download:
	@./scripts/dowload_micropython.sh

install:
	@./scripts/install_micropython.sh
