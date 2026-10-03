# LLM App CI/CD Pipeline

A small LLM app with unit tests, LLM evals, a Docker image, and a GitHub Actions pipeline.

## Run locally
```
pip install -r requirements.txt
pytest
python -m evals.run_evals
python -m app
```
Requires Ollama with `ollama pull qwen2.5:1.5b`.

## Pipeline
push / PR -> unit tests -> LLM evals -> Docker build
