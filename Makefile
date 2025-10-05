IMAGE_NAME := observant
CONTAINER_NAME := observant-container

build:
	docker build --build-arg UID=$(shell id -u) --build-arg GID=$(shell id -g) -t $(IMAGE_NAME) .

run:
	docker run -u $(shell id -u):$(shell id -u) -e CERTORAKEY=$(CERTORAKEY) --rm -it -v $(shell pwd):/home/observant/shared:z --name $(CONTAINER_NAME) $(IMAGE_NAME)
