from fastapi import FastAPI
from schema.user_input import InputData
from model.predict import predict_output, model, MODEL_VERSION
from fastapi.responses import JSONResponse
from schema.predict_response import PredictionResponse
app = FastAPI()


@app.get('/')
def home():
    return {
        'message': 'Insurance Premium Prediction API'
    }


@app.get('/health')
def health_check():
    return {
        'status': 'OK',
        'version': MODEL_VERSION,
        'model_loaded': model is not None

    }


@app.post("/predict", response_model=PredictionResponse)
def predict(data: InputData):
    user_input = {
        'bmi': data.bmi,
        'age_group': data.age_group,
        'lifestyle_risk': data.lifestyle_risk,
        'city_tier': data.city_tier,
        'income_lpa': data.income_lpa,
        'occupation': data.occupation
    }
    try:
        prediction = predict_output(user_input)

        return JSONResponse(
            status_code=200,
            content={
                'response': prediction
            }
        )
    except Exception as e:
        return JSONResponse(status_code=500, content=str(e))
