# Enterprise Knowledge Assistant

**Project:** RAG-Powered Q&A + Fine-Tuned Report Generator  
**Platform:** AWS Console  
**Services:** Amazon S3, Amazon Bedrock, OpenSearch Serverless, Lambda, API Gateway, Cognito  

---

## Overview

The Enterprise Knowledge Assistant allows employees to:

1. **Ask Questions about Internal Policies & Documents** – powered by **RAG (Retrieval-Augmented Generation)**.  
2. **Auto-Generate Structured Reports** – using **fine-tuned LLMs** for compliance summaries, weekly updates, and risk assessments.

This project demonstrates a complete workflow from **document storage** → **embedding** → **vector search** → **query response** → **structured report generation**.

---

## How It Works

### RAG Q&A Workflow

1. Upload internal documents (policies, SOPs, compliance manuals) to **Amazon S3**.  
2. Create a **Knowledge Base in AWS Bedrock**, linking the S3 bucket.  
3. Select an **embedding model** for the knowledge base.  
4. Bedrock automatically:
   - Chunks the documents.
   - Generates embeddings for each chunk.
   - Stores embeddings in **OpenSearch Serverless**.  
5. User queries (e.g., “What are onboarding requirements under ISO27001?”):
   - Relevant chunks are retrieved.
   - LLM generates answers with citations.

### Fine-Tuned Report Generation

1. Upload historical reports (weekly summaries, risk assessments, audits) as **JSONL files in S3**.  
2. Fine-tune an LLM in **AWS Bedrock** on these datasets.  
3. Users request a report (e.g., “Generate weekly compliance summary for Dept. A”).  
4. The fine-tuned LLM generates a **formatted, structured report** in the company’s style.

---

## Sample Files

### RAG Documents (S3 bucket: `enterprise-docs-rag`)

**`onboarding_policy.txt`**
**`data_retention_policy.txt`**


### Fine-Tuning Dataset (S3 bucket: `enterprise-finetune-reports`)

**`weekly_compliance_reports.jsonl`**

---

## Features

RAG-powered Enterprise Q&A with citations
Fine-tuned structured report generation
Separation of concerns: RAG vs fine-tuning
Enterprise-ready: saves time, ensures consistent reporting

---

## License

MIT License
