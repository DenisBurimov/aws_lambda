import requests
import json
import boto3
from botocore.auth import SigV4Auth
from botocore.awsrequest import AWSRequest
from botocore.credentials import Credentials

aws_access_key = 'AKIARBQLSALC2EJA2FNT'
aws_secret_key = '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'
region = 'us-east-1'
function_name = 'S2B_0108_01'

# function_url = f'https://lambda.{region}.amazonaws.com/2015-03-31/functions/{function_name}/invocations'
function_url = "https://t6unghsab7klqrwl26yk3bnury0nwvke.lambda-url.us-east-1.on.aws/"
endpoint = f'lambda.{region}.amazonaws.com'

# Sample payload to send to the Lambda function (adjust according to your function's input)
payload = {
    'key2': 'value2'
}


def sign_request(method, url, data):
    credentials = Credentials(aws_access_key, aws_secret_key)

    request = AWSRequest(
        method=method,
        url=url,
        data=data.encode('utf-8') if data is not None else None,
        headers={
            'Content-Type': 'application/json',
            'X-Amz-Invocation-Type': 'RequestResponse',
            'X-Amz-Log-Type': 'None'
        }
    )

    SigV4Auth(credentials, 'lambda', region).add_auth(request)

    return request


data = json.dumps(payload)
signed_request = sign_request('POST', function_url, data)

response = requests.post(
    function_url,
    data=data,
    headers=signed_request.headers
)

if response.status_code == 200:
    result = json.loads(response.text)
    print(json.dumps(result, indent=2))
else:
    print(f"Error: {response.status_code} - {response.text}")
