# FastAPI Project with Streamlit

A modern, fast (high-performance) web framework for building APIs with Python 3.6+ based on standard Python type hints, integrated with Streamlit for interactive data visualization and web apps.

## Features

- **Fast**: Very high performance, on par with NodeJS and Go
- **Fast to code**: Increase the speed to develop features by about 200% to 300%
- **Fewer bugs**: Reduce about 40% of human (developer) induced errors
- **Intuitive**: Great editor support with autocompletion everywhere
- **Easy**: Designed to be easy to use and learn
- **Short**: Minimize code duplication
- **Interactive**: Streamlit integration for beautiful web interfaces

## Installation

```bash
pip install fastapi uvicorn streamlit
```

## Quick Start

### FastAPI Backend

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}
```

### Streamlit Frontend

```python
import streamlit as st
import requests

st.title("FastAPI + Streamlit App")

# Get data from FastAPI
response = requests.get("http://127.0.0.1:8000/")
st.json(response.json())

# Interactive item query
item_id = st.number_input("Item ID", min_value=1, value=1)
if st.button("Get Item"):
    response = requests.get(f"http://127.0.0.1:8000/items/{item_id}")
    st.json(response.json())
```

## Running the Application

### Start FastAPI server:

```bash
uvicorn main:app --reload
```

### Start Streamlit app:

```bash
streamlit run streamlit_app.py
```

## Documentation

- Interactive API docs: `http://127.0.0.1:8000/docs`
- Alternative docs: `http://127.0.0.1:8000/redoc`
- Streamlit app: `http://localhost:8501`

# ✅ Project Update Summary – Model API Improvements

**🕒 Timeline:** `4:13 – 40:34`  
**📦 Commit Scope:** Modularization, validation, confidence scoring, route enhancements

---

## 📁 1. Created New Folder Structure

- Organized the project into modular folders for maintainability.
- Separated concerns: `model/`, `routes/`, `schemas/`, etc.

## 🛡️ 2. Added Field Validator for City Input

- Implemented `@field_validator` to normalize city input.
- Ensures consistent casing and formatting before model processing.

## 🌐 3. Added Routes

- `/` → Home route.
- `/health` → Health check route to monitor server status.

## 🧠 4. Embedded Model Versioning

- Added a model version string to prediction response.
- Useful for debugging and version control of deployed models.

## ⚙️ 5. Separated Core Logic

- Moved different responsibilities to their own files:
  - `pydantic_model.py` → Request model validation.
  - `city_tier.py` → Tier classification logic.
  - `predict.py` → Machine learning inference.

## 🚨 6. Added Try-Except Error Handling

- Wrapped inference code in try-catch blocks.
- Prevents API from crashing on bad inputs or internal errors.

## 📈 7. Confidence Score Integration

- Included `predict_proba()` output in API response (if available).
- Helps understand prediction certainty.

## 🧾 8. Introduced Response Model

- Used a Pydantic response schema for cleaner, documented API responses.

## ✅ 9. Final Testing and Confirmation

- Successfully tested all routes with valid/invalid inputs.
- Verified API responses and stability.

---
