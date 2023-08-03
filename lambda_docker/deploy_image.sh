#!/bin/bash
docker build -t burn_model --platform linux/amd64 . &&
docker tag burn_model:latest 867661782732.dkr.ecr.us-east-1.amazonaws.com/burn_model:latest &&
docker push 867661782732.dkr.ecr.us-east-1.amazonaws.com/burn_model:latest &&
aws lambda update-function-code --function-name oculo_burn_model --image-uri 867661782732.dkr.ecr.us-east-1.amazonaws.com/burn_model:latest
