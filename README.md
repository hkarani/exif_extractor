Setting up the Project

1. Clone the repository
    git clone https://github.com/hkarani/exif_extractor.git

2. Build docker image
    docker build --platform linux/amd64 -t docker-image:test . 

3. Run the docker image
    sudo docker run --platform linux/amd64 -p 9000:8080 docker-image:test

Testing Locally
1. Open folder location on terminal

2. Create python vitual environment
    python3 -m venv myvenv

3. Activate your virtual environment
    source myvenv/bin/activate

4. Create test.py file and paste in code from test.py

5. Run script via terminal
    python3 test.py

How to stop application

1. Get container ID
    docker ps

2. Kill the docker file
    docker kill 3766c4ab331c


Deploying to AWS

1. Run the get-login-password command to authenticate the Docker CLI to your Amazon ECR registry.
Set the --region value to the AWS Region where you want to create the Amazon ECR repository.
Replace 111122223333 with AWS account ID.


    aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 111122223333.dkr.ecr.us-east-1.amazonaws.com

2. Create a repository in Amazon ECR using the create-repository command.
    aws ecr create-repository --repository-name hello-world --region us-east-1 --image-scanning-configuration scanOnPush=true --image-tag-mutability MUTABLE

    **make sure the region matches the first option you selected

    Success will yield you this:
    {
    "repository": {
        "repositoryArn": "arn:aws:ecr:us-east-1:111122223333:repository/hello-world",
        "registryId": "111122223333",
        "repositoryName": "hello-world",
        "repositoryUri": "111122223333.dkr.ecr.us-east-1.amazonaws.com/hello-world",
        "createdAt": "2023-03-09T10:39:01+00:00",
        "imageTagMutability": "MUTABLE",
        "imageScanningConfiguration": {
            "scanOnPush": true
        },
        "encryptionConfiguration": {
            "encryptionType": "AES256"
        }
        }
    }    

3. Copy the repositoryUri from the output in the previous step.

4. Run the docker tag command to tag your local image into your Amazon ECR repository as the latest version. In this command:

    -Replace docker-image:test with the name and tag of your Docker image.
    -Replace <ECRrepositoryUri> with the repositoryUri that you copied. Make sure to include :latest at the end of the URI.
        docker tag docker-image:test <ECRrepositoryUri>:latest
        docker tag docker-image:test 111122223333.dkr.ecr.us-east-1.amazonaws.com/hello-world:latest

5. Run the docker push to deploy your local image
        docker push 111122223333.dkr.ecr.us-east-1.amazonaws.com/hello-world:latest

6. Create an execution role for the function, if you don't already have one. You need the Amazon Resource Name (ARN) of the role in the next step.

7. Create the Lambda function. For ImageUri, specify the repository URI from earlier. Make sure to include :latest at the end of the URI.
        aws lambda create-function \
        --function-name hello-world \
        --package-type Image \
        --code ImageUri=111122223333.dkr.ecr.us-east-1.amazonaws.com/hello-world:latest \
        --role arn:aws:iam::111122223333:role/lambda-ex

8. Invoke your function when you need.

*** Remember to name your app appropriate during deployment if "Hello world doesn't meet your needs"

