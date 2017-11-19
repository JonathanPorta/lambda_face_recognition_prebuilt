#lambda_face_recognition_prebuilt
A prebuilt set of the dependencies needed to run face_recognition in AWS Lambda.

## Usage
`pip install lambda_face_recognition_prebuilt`

## How it Works
The libs needed for face_recognition are built inside a Docker container that matches the environment in which AWS Lambda code is ran.

Since the dependencies for face_recognition exceed the source code size limit of AWS Lambda functions, we do some ridiculousness to make it work. We zip up the deps and then unzip them at runtime.

The unzipping of these deps at runtime will add overhead to your function's start time. So, please keep that in mind in deciding whether to use this package.
