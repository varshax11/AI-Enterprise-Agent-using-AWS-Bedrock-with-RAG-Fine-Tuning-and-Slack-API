# Enterprise Knowledge Assistant

---

## Overview
The Enterprise Knowledge Assistant is an AI-powered system that helps employees:
1. Ask questions about internal policies, SOPs, and compliance documents (RAG-powered).
2. Generate structured reports, summaries, and risk assessments using a fine-tuned LLM.
3. Post outputs or notifications to Slack channels.


This project integrates AWS Bedrock, Amazon S3, OpenSearch Serverless, and AWS Lambda.

---

## Architecture / Flow
1. Document Storage – Internal documents and reports are stored in Amazon S3.
2. Knowledge Base – AWS Bedrock chunks, embeds, and stores documents in OpenSearch Serverless for retrieval.
3. Fine-Tuned Model – Historical reports are used to fine-tune a Bedrock LLM (Nova Pro).
4. AWS Lambda Functions – Handle retrieval, report generation, and Slack notifications.
5. Bedrock Agent – Orchestrates user requests and invokes the appropriate Lambda action group.

---

## Prerequisites
- AWS account with Bedrock access.
- S3 buckets:
- `enterprise-docs-rag` → internal documents.
- `enterprise-finetune-reports` → fine-tuning datasets.
- IAM roles with required permissions for Bedrock, S3, and CloudWatch.
- Slack workspace & bot token for Slack integration

## Sample Files

### RAG Documents (S3 bucket: `enterprise-docs-rag`)

**`onboarding_policy.txt`**

### Fine-Tuning Dataset (S3 bucket: `enterprise-finetune-reports`)

**`weekly_compliance_reports.jsonl`**

---

## Features

AI Agent that decides which tool to use when user gives a prompt
RAG-powered Enterprise Q&A with citations
Fine-tuned structured report generation
Slack notification creation by the AI agent

---

## License

MIT License
