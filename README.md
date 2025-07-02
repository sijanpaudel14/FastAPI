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