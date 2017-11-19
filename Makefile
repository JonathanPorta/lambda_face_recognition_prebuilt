include ./ops/pip.mk

build: build_container
	docker cp build-container:/var/task/ ./build
	cd ./build && zip -r9 ../lambda_face_recognition_prebuilt/deps.zip *

build_container: clean_container
	docker build -t jonathanporta/lambda_face_recognition_prebuilt .
	docker run --name build-container jonathanporta/lambda_face_recognition_prebuilt:latest

clean: clean_container

clean_container:
	@-docker rm build-container

shell: build_container
	@-docker rm build-container
	docker run --rm -it jonathanporta/lambda_face_recognition_prebuilt:latest bash

package: pip_package

release: pip_release
