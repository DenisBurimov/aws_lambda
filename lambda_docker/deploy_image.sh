#!/bin/bash
docker build -t lambda_01 --platform linux/amd64 . &&
docker tag lambda_01:latest 071964951237.dkr.ecr.us-east-1.amazonaws.com/s2b-lambda_01:latest &&
docker push 071964951237.dkr.ecr.us-east-1.amazonaws.com/s2b-lambda_01:latest &&
aws lambda update-function-code --function-name oculo_burn_model --image-uri 071964951237.dkr.ecr.us-east-1.amazonaws.com/s2b-lambda_01:latest
