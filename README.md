
# Legal Document Intelligence Platform (Microservices Architecture)

This repository contains an educational microservices-based architecture for a **Legal Document Intelligence Platform**, built using **FastAPI**, **Celery**, **GraphQL**, **PostgreSQL**, **RabbitMQ**, and **Kubernetes on Azure**. It demonstrates how to ingest, process, analyze, and generate insights from legal documents at scale.

---

## Project Overview

The platform is designed as a collection of **loosely coupled microservices**, each responsible for a **distinct business capability**. It follows modern best practices in distributed system design, observability, DevOps, and AI integration.

---

## Microservices Breakdown

### 1. Auth & User Management Service

- **Tech:** FastAPI + PostgreSQL + JWT + Bcrypt
- **Features:**
  - User registration & login
  - Role-Based Access Control (RBAC)
  - JWT-based authentication
  - Secure password hashing (Bcrypt)
  - Rate limiting & secure cookie handling
  - Prometheus metrics + structured logs

---

### 2. Document Ingestion & Metadata Service

- **Tech:** FastAPI + PostgreSQL + Azure Blob Storage + Redis/RabbitMQ + Celery
- **Endpoints:**
  - `POST /documents/upload`
  - `GET /documents/{doc_id}`
- **Features:**
  - Upload large legal documents
  - Extract and store metadata (filename, size, upload date)
  - Store files in Azure Blob Storage
  - Trigger async processing pipeline via message queue

---

### 3. Document Processing Worker (Celery)

- **Tech:** Celery + Azure Blob Storage + Vector DB (pgvector/Milvus)
- **Celery Tasks:**
  - `extract_text_task`: OCR & text extraction
  - `chunk_document_task`: Chunk into context windows
  - `generate_embeddings_task`: Call ML model for embeddings
  - `store_embeddings_task`: Save chunks + vectors
  - `analyze_compliance_task`: Compliance risk detection via RAG/LLM
  - `generate_summary_task`: Generate summaries
  - `notification_task`: Notify users via email/in-app

- **Features:**
  - Scalable worker pool (Kubernetes)
  - Dead-letter queue & retry logic
  - Fully async, multi-stage processing pipeline

---

### 4. Reporting & Analytics Service

- **Tech:** FastAPI + PostgreSQL + GraphQL + Kafka (optional)
- **Endpoints:**
  - `GET /reports/compliance`
  - `POST /analytics/trends`
- **Features:**
  - Query historical document data
  - Generate compliance reports
  - GraphQL for flexible analytics queries
  - Connects to data warehouse or Kafka stream

---

### 5. Notification Service

- **Tech:** FastAPI + Celery + WebSockets
- **Features:**
  - Email notifications (via Celery)
  - Real-time in-app alerts (WebSocket support)
  - Triggered internally by other services

---

## Technologies Used(in future)

| Category               | Stack                                                                 |
|------------------------|-----------------------------------------------------------------------|
| API Framework          | FastAPI                                                              |
| Background Tasks       | Celery                                                               |
| Message Broker         | RabbitMQ                                                    |
| Database               | PostgreSQL + pgvector                                                |
| File Storage           | Azure Blob Storage                                                   |
| ML Integration         | LLM for RAG (e.g., Gemini/OpenAI), custom embedding service          |
| Real-Time Notifications| WebSockets                                                           |
| Observability          | OpenTelemetry, Prometheus, Grafana, Tempo, Loki                      |
| Containerization       | Docker                                                               |
| Orchestration          | Kubernetes (Azure AKS)                                               |
| CI/CD                  | GitHub Actions / Azure Pipelines                                     |
| Security               | JWT, OAuth2, RBAC, HTTPS, secure coding practices                    |
| IaC                    | Terraform or Bicep for Azure infrastructure                          |

---

## RAG Pipeline Overview (within Worker Service)

1. **Text Extraction** → `extract_text_task`
2. **Chunking** → `chunk_document_task`
3. **Embeddings** → `generate_embeddings_task`
4. **Storage** → `store_embeddings_task`
5. **Compliance/QA** → `analyze_compliance_task`
6. **Summarization** → `generate_summary_task`

---

## Testing Strategy

- **Unit Tests:** Core logic (e.g., auth, task functions)
- **Integration Tests:** API + DB + Blob + Celery
- **CI:** Enforces >90% test coverage using `pytest`, `coverage.py`, and CI workflows

---

> [!NOTE]
> Educational Goals:
> This project is ideal for learning:
> Clean microservice architecture with async pipelines
> Secure, scalable FastAPI APIs
> Production-ready Celery pipelines
> Vector search + RAG in a real-world system
> Observability with OpenTelemetry, Prometheus, and Grafana
> Azure-native deployment and IaC with Terraform
