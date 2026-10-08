# LLM App CI/CD Pipeline

A small LLM application demonstrating **unit testing, LLM evaluation, Docker containerization, and GitHub Actions CI/CD automation**.

The project uses **Ollama + Qwen2.5 1.5B** locally and includes automated tests and LLM evaluation test cases.

---

## Project Flow

```text
Code Push / Pull Request
          ↓
     GitHub Actions
          ↓
      Unit Tests
       (Pytest)
          ↓
      LLM Evals
          ↓
    Quality Check
          ↓
      Docker Build
```

---

## Project Structure

```text
llm-app/
│
├── app/
│   ├── __init__.py
│   ├── __main__.py
│   └── llm_service.py
│
├── tests/
│   └── test_unit.py
│
├── evals/
│   ├── test_cases.json
│   └── run_evals.py
│
├── .github/
│   └── workflows/
│       └── ci.yml
│
├── Dockerfile
├── requirements.txt
├── pytest.ini
└── README.md
```

---

# Run Locally

## 1. Clone the repository

```bash
git clone <your-repository-url>
cd llm-app
```

## 2. Create a virtual environment

### Windows

```powershell
python -m venv venv
```

Activate it:

```powershell
.\venv\Scripts\Activate.ps1
```

You should see:

```text
(venv)
```

at the beginning of your terminal.

---

## 3. Install dependencies

```powershell
pip install -r requirements.txt
```

---

# 4. Install and Start Ollama

The application uses Ollama to run the local LLM.

Install Ollama and pull the required model:

```powershell
ollama pull qwen2.5:1.5b
```

Make sure Ollama is running before executing the LLM evaluation or application.

---

# 5. Run Unit Tests

Run:

```powershell
pytest
```

Example successful output:

```text
tests\test_unit.py ... [100%]

3 passed
```

This means the three predefined unit tests were discovered and executed successfully.

The tests verify:

* LLM response handling
* Prompt transmission
* JSON response parsing

The LLM API call is mocked during unit testing, so the tests do not require an actual LLM request.

---

# 6. Run LLM Evaluations

From the project root directory, run:

```powershell
python -m evals.run_evals
```

The evaluation script reads the predefined test cases from:

```text
evals/test_cases.json
```

and evaluates the application's LLM responses.

> Use `python -m evals.run_evals` instead of `python evals/run_evals.py` because running the file directly can cause Python import errors such as `ModuleNotFoundError: No module named 'app'`.

---

# 7. Run the Application

After the tests and evaluations pass:

```powershell
python -m app
```

The application uses the configured Ollama model to generate responses.

---

# Docker

Build the Docker image:

```powershell
docker build -t llm-app .
```

Run the container:

```powershell
docker run --rm llm-app
```

---
Quick Execution Guide

From the project root (llm-app):

# 1. Create virtual environment
python -m venv venv

# 2. Activate virtual environment
.\venv\Scripts\Activate.ps1

# 3. Install dependencies
pip install -r requirements.txt

# 4. Make sure Ollama is installed and the model is available
ollama pull qwen2.5:1.5b

# 5. Run unit tests
pytest

# 6. Run LLM evaluations
python -m evals.run_evals

# 7. Run the application
python -m app
# CI/CD Pipeline

The project includes a GitHub Actions workflow.

The pipeline is triggered when code is:

* Pushed to the repository
* Submitted through a Pull Request

The pipeline performs:

```text
Push / Pull Request
        ↓
Install Dependencies
        ↓
Run Unit Tests
        ↓
Run LLM Evaluations
        ↓
Build Docker Image
```

If a required stage fails, GitHub Actions reports the workflow as failed.

---

# Testing

The project contains predefined unit tests in:

```text
tests/test_unit.py
```

LLM evaluation test cases are maintained separately in:

```text
evals/test_cases.json
```

This separation allows the unit tests and LLM evaluation tests to be maintained independently.

---

# Quick Start

For an already configured environment:

```powershell
# Activate environment
.\venv\Scripts\Activate.ps1

# Run unit tests
pytest

# Run LLM evaluations
python -m evals.run_evals

# Run application
python -m app
```

---

# Technologies Used

* Python
* Pytest
* Ollama
* Qwen2.5 1.5B
* LLM Evaluation
* Docker
* GitHub Actions
* CI/CD
* JSON-based Test Cases
