from pydantic import BaseModel, Field
from typing import Dict


class PredictionResponse(BaseModel):
    """
    Pydantic model for the prediction response.
    """
    predicted_category: str = Field(
        ...,
        description="The category predicted by the model.",
        example="High"
    ),
    confidence: float = Field(
        ...,
        description="Confidence level of the prediction, ranging from 0 to 1.",
        ge=0, le=1,
        example=0.85
    )
    prediction: Dict[str, float] = Field(
        ...,
        description="Prediction results with probabilities for each class."
    )
    class_probabilities: Dict[str, float] = Field(
        ...,
        description="Probabilities for each class in the prediction.",
        example={
            "Low": 0.1,
            "Medium": 0.2,
            "High": 0.7
        }
    )

    class Config:
        json_schema_extra = {
            "example": {
                "predicted_category": "High",
                "confidence": 0.85,
                "prediction": {
                    "Low": 0.1,
                    "Medium": 0.2,
                    "High": 0.7
                },
                "class_probabilities": {
                    "Low": 0.1,
                    "Medium": 0.2,
                    "High": 0.7
                }
            }
        }
