import json
import boto3
import os
import urllib3

# Initialize AWS clients
bedrock = boto3.client('bedrock-runtime')
http = urllib3.PoolManager()

# Environment variables (set in Lambda configuration)
KB_ID = os.environ['KB_ID']  # Your Knowledge Base ID
FINE_TUNED_MODEL_ARN = os.environ['FINE_TUNED_MODEL_ARN']
SLACK_WEBHOOK_URL = os.environ.get('SLACK_WEBHOOK_URL')  # optional

def lambda_handler(event, context):
    """
    Lambda entry point for RAG Q&A and fine-tuned report generation
    event = {
        "type": "query" or "report",
        "text": "User input question or report request"
    }
    """
    request_type = event.get('type')
    user_input = event.get('text', '')

    if not user_input:
        return {"statusCode": 400, "body": "No input provided"}

    if request_type == "query":
        response = query_rag(user_input)
    elif request_type == "report":
        response = generate_report(user_input)
    else:
        return {"statusCode": 400, "body": "Invalid type. Must be 'query' or 'report'"}

    # Optional: Send to Slack
    if SLACK_WEBHOOK_URL:
        send_slack_message(response)

    return {"statusCode": 200, "body": response}

# -------------------------------
# RAG Knowledge Base Query
# -------------------------------
def query_rag(user_question):
    """
    Call Bedrock Knowledge Base to retrieve answer with citations
    """
    response = bedrock.retrieve_and_generate(
        input={"text": user_question},
        retrieveAndGenerateConfiguration={
            "knowledgeBaseConfiguration": {
                "knowledgeBaseId": KB_ID,
                "modelArn": FINE_TUNED_MODEL_ARN
            },
            "type": "KNOWLEDGE_BASE"
        }
    )
    answer = response.get('results', [{}])[0].get('outputText', '')
    return answer

# -------------------------------
# Fine-Tuned Report Generation
# -------------------------------
def generate_report(prompt_text):
    """
    Call Bedrock fine-tuned model to generate structured report
    """
    response = bedrock.invoke_model(
        body=json.dumps({"inputText": prompt_text}),
        modelId=FINE_TUNED_MODEL_ARN,
        contentType="application/json",
        accept="application/json"
    )
    result = json.loads(response['body'].read())
    report = result.get('outputText', '')
    return report

# -------------------------------
# Slack Notification
# -------------------------------
def send_slack_message(message_text):
    """
    Send the response to a Slack channel using Incoming Webhook
    """
    payload = {"text": message_text}
    http.request(
        "POST",
        SLACK_WEBHOOK_URL,
        body=json.dumps(payload),
        headers={"Content-Type": "application/json"}
    )
