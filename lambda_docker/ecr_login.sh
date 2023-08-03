#!/bin/bash
source ../.env
# echo ${AWS_ACCESS_KEY}
# Run the get-login-password command to authenticate the Docker CLI to your Amazon ECR registry.
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 071964951237.dkr.ecr.us-east-1.amazonaws.com

# Create a repository in Amazon ECR using the create-repository command.
aws ecr create-repository --repository-name s2b-lambda_01 --image-scanning-configuration scanOnPush=true --image-tag-mutability MUTABLE

# Extract repositoryUri using jq and assign to a variable
repositoryUri=$(echo "$output" | jq -r '.repository.repositoryUri')

# Print the repositoryUri
echo "Repository URI: $repositoryUri"
