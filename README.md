# ProductHub API

RESTful API for product and inventory management, built with Python and FastAPI, tested with Postman, and managed using Scrum.

## Project Overview

ProductHub is a backend development project designed to practice REST API development, automated API testing, Git/GitHub workflows, and agile software development methodologies.

The project also serves as a hands-on QA portfolio, demonstrating API validation, test automation, and software testing practices.

## Tech Stack

- **Python** — Backend programming language
- **FastAPI** — REST API framework
- **Uvicorn** — ASGI server
- **Postman** — API testing and automated assertions
- **Git & GitHub** — Version control and pull requests
- **Jira (Scrum)** — Sprint planning and task tracking

**Planned:** SQLite for database integration.

## Project Status

**Sprint 0 — Project Setup and API Testing**

Completed:
- GitHub repository initialization
- Python virtual environment configuration
- FastAPI application setup
- Postman collection creation
- Health check endpoint implementation
- Automated health check tests

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/renataam11/producthub-api.git
cd producthub-api
```

### 2. Create and activate a virtual environment

Windows (Git Bash):

```bash
python -m venv .venv
source .venv/Scripts/activate
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

## Running the API

Start the development server:

```bash
python -m uvicorn main:app --reload
```

The API will be available at:

`http://127.0.0.1:8000`

Interactive API documentation:

`http://127.0.0.1:8000/docs`

## Available Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Returns the ProductHub welcome message |
| GET | `/health` | Returns the API health status |

### GET /

Expected response:

```json
{
  "message": "Welcome to ProductHub API"
}
```

### GET /health

Expected response:

```json
{
  "status": "healthy"
}
```

Expected HTTP status: `200 OK`

## API Testing with Postman

The repository includes a Postman collection in the `postman/` directory.

### Running the tests

1. Start the FastAPI development server.
2. Open Postman.
3. Import the JSON collection from the `postman/` directory.
4. Set the `host` variable to `http://127.0.0.1:8000`.
5. Open the health check request.
6. Click **Send**.
7. Review the results in **Test Results**.

### Automated Health Check Tests

The health check request validates:

1. The HTTP status code is `200`.
2. The response is valid JSON.
3. The `status` field equals `"healthy"`.

Expected result: **3 passed, 0 failed**.

A controlled negative assertion was also performed during development to confirm that the tests detect unexpected response values.

## Features (Planned)

- Product CRUD operations
- Inventory management
- SQLite database integration
- API validation and error handling
- Additional positive and negative API test cases
- Expanded automated API testing

## Development Workflow

The project follows a Scrum-based workflow using Jira.

Each development task is implemented in a dedicated Git branch, committed, pushed to GitHub, reviewed through a pull request, and merged into `main`.

## Sprint 0 Summary

Sprint 0 established the initial development and testing environment for ProductHub API.

The main deliverables were a working FastAPI application, a documented Postman collection, a health check endpoint, and automated response validations.

These foundations will support future product management features and additional QA testing scenarios.
