BINARY_NAME=hbase_exporter

SRC=./

.PHONY: build
build:
	@echo "Building the application..."
	go build -o $(BINARY_NAME) $(SRC)
