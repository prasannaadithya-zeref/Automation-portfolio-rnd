# 🌐 API Architecture & Lifecycle Guide

## 1. Types of APIs
Understanding the different architectural styles is crucial for testing.

### REST (Representational State Transfer)
- **Standard**: Most common. Uses HTTP methods (GET, POST, PUT, DELETE).
- **Format**: JSON or XML.
- **Stateless**: Server doesn't remember previous requests.
- **Example**: `GET /users/1`

### SOAP (Simple Object Access Protocol)
- **Standard**: Strict protocol, heavy, enterprise-focused.
- **Format**: XML only. Requires WSDL (Web Services Description Language).
- **State**: Can be stateful.
- **Example**: Banking transactions.

### GraphQL
- **Concept**: "Ask for exactly what you need". No over-fetching.
- **Method**: Single Endpoint (usually POST).
- **Format**: JSON-like query language.

---

## 2. API Lifecycle (Creation to Deployment)
How does an API get to production?

1.  **Design (Contract)**: Define Swagger/OpenAPI spec. "This API takes X and returns Y".
2.  **Development**: Developers build the backend (Python Flask, Java SpringBoot, Node.js).
3.  **Mocking**: QA creates Mocks (like in this portfolio) to test before Dev is ready.
4.  **Deployment**:
    *   **Containerize**: Wrap app in Docker.
    *   **Orchestrate**: Deploy to Kubernetes (K8s) or AWS ECS.
5.  **Gateway**: API Gateway (Kong, AWS API Gateway) sits in front to handle Auth & Rate Limiting.

---

## 3. Common HTTP Status Codes
*   **200**: OK (Success)
*   **201**: Created (Resource made)
*   **204**: No Content (Delete success)
*   **400**: Bad Request (Invalid JSON)
*   **401**: Unauthorized (No Token)
*   **403**: Forbidden (Token valid, but ID doesn't have permissions)
*   **404**: Not Found
*   **500**: Internal Server Error (Code crash)
*   **503**: Service Unavailable (Down)
