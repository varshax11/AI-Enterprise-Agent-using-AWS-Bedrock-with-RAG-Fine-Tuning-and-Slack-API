import json
import os
import requests


SLACK_TOKEN = os.environ['SLACK_TOKEN']
CHANNEL_ID = os.environ['CHANNEL_ID']


def lambda_handler(event, context):
body = json.loads(event.get("body", "{}"))
message = body.get("message", "No message provided")


url = "https://slack.com/api/chat.postMessage"
headers = {
"Content-Type": "application/json",
"Authorization": f"Bearer {SLACK_TOKEN}"
}
payload = {
"channel": CHANNEL_ID,
"text": message
}


response = requests.post(url, headers=headers, data=json.dumps(payload))


return {"statusCode": response.status_code, "body": response.text}
