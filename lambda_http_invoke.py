import os
import requests
import json
from botocore.auth import SigV4Auth
from botocore.awsrequest import AWSRequest
from botocore.credentials import Credentials
from dotenv import load_dotenv

load_dotenv()

aws_access_key = os.getenv("AWS_ACCESS_KEY")
aws_secret_key = os.getenv("AWS_SECRET_KEY")
region = os.getenv("AWS_REGION")
function_name = os.getenv("LAMBDA_NAME")

function_url = "https://t6unghsab7klqrwl26yk3bnury0nwvke.lambda-url.us-east-1.on.aws/"
endpoint = f"lambda.{region}.amazonaws.com"

payload = {"key2": "value2"}


def sign_request(method, url, data):
    credentials = Credentials(aws_access_key, aws_secret_key)

    request = AWSRequest(
        method=method,
        url=url,
        data=data.encode("utf-8") if data is not None else None,
        headers={
            "Content-Type": "application/json",
            "X-Amz-Invocation-Type": "RequestResponse",
            "X-Amz-Log-Type": "None",
        },
    )

    SigV4Auth(credentials, "lambda", region).add_auth(request)

    return request


data = json.dumps(payload)
signed_request = sign_request("POST", function_url, data)

response = requests.post(function_url, data=data, headers=signed_request.headers)

if response.status_code == 200:
    result = json.loads(response.text)
    print(json.dumps(result, indent=2))
else:
    print(f"Error: {response.status_code} - {response.text}")
