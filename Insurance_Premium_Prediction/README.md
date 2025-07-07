# Insurance Premium Prediction API

A FastAPI-based machine learning service for predicting insurance premiums using scikit-learn.

## Quick Start with Docker

Pull and run the pre-built Docker image:

```bash
docker pull sijanpaudel14/insurance-premium-api
docker run -p 8000:8000 sijanpaudel14/insurance-premium-api
```

The API will be available at `http://localhost:8000`

## API Documentation

- **Interactive Docs**: `http://localhost:8000/docs`
- **ReDoc**: `http://localhost:8000/redoc`

## Local Development

1. Create virtual environment:

```bash
python -m venv fastapi_env
source fastapi_env/bin/activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the application:

```bash
uvicorn app:app --reload
```

## Tech Stack

- **FastAPI** - Web framework
- **Pydantic** - Data validation
- **scikit-learn** - Machine learning
- **pandas** - Data processing
- **Docker** - Containerization
