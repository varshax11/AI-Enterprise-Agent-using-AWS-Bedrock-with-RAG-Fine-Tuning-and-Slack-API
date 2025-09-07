import boto3
import json
import os


KB_ID = os.environ['KB_ID']
LLM_MODEL_ARN = os.environ['LLM_MODEL_ARN']
REGION = os.environ['REGION']


kb_rt = boto3.client("bedrock-runtime", region_name=REGION)


def lambda_handler(event, context):
body = json.loads(event.get("body", "{}"))
user_query = body.get("query", "What are onboarding requirements?")


response = kb_rt.retrieve_and_generate(
input={"text": user_query},
retrieveAndGenerateConfiguration={
"knowledgeBaseConfiguration": {
"knowledgeBaseId": KB_ID,
"modelArn": LLM_MODEL_ARN
},
"type": "KNOWLEDGE_BASE"
}
)


result = response.get("body")
if hasattr(result, "read"):
result = json.loads(result.read())
else:
result = json.loads(result)


return {"statusCode": 200, "body": json.dumps(result)}
