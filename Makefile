SHELL := /bin/bash

.SHELLFLAGS = -e -o pipefail -c
.ONESHELL:

IMAGE_NAME=simple-app
CONTAINER_NAME=simple-app

.PHONY: build run rm

build:
	cd ./app
	docker build --build-arg DEPLOY_REF=$(DEPLOY_REF) -t $(IMAGE_NAME) .

run:
	docker run -d \
		--name $(CONTAINER_NAME) \
		-p 5000:5000 \
		$(IMAGE_NAME)

rm:
	docker rm -f $(CONTAINER_NAME) || true