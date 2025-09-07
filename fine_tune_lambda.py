import boto3
import json
import os


FINE_TUNED_MODEL_ARN = os.environ['FINE_TUNED_MODEL_ARN']
REGION = os.environ['REGION']


bedrock = boto3.client("bedrock-runtime", region_name=REGION)


def lambda_handler(event, context):
body = json.loads(event.get("body", "{}"))
prompt = body.get("prompt", "Generate weekly compliance report for Dept. A")


response = bedrock.invoke_model(
modelId=FINE_TUNED_MODEL_ARN,
contentType="application/json",
accept="application/json",
body=json.dumps({"inputText": prompt})
)


result_body = response.get("body")
if hasattr(result_body, "read"):
result = json.loads(result_body.read())
else:
result = json.loads(result_body)


return {"statusCode": 200, "body": json.dumps(result)}
