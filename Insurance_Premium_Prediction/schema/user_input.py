from pydantic import BaseModel, Field, computed_field, field_validator
from typing import List, Optional, Literal, Annotated
from config.city_tier import tier_1_cities,tier_2_cities

# pydantic model for input data and validate incoming data

class InputData(BaseModel):
    age: Annotated[int, Field(..., ge=0, le=120,
                              description="Age of the person")]
    weight: Annotated[float,
                      Field(..., ge=0,  description="Weight of the person in kg")]
    height: Annotated[float,
                      Field(..., ge=0, le=2.5, description="Height of the person in cm")]
    income_lpa: Annotated[float,
                          Field(..., ge=0, description="Income in lakhs per annum")]
    smoker: Annotated[bool,
                      Field(..., description="Smoking status of the person")]
    city: Annotated[str,
                    Field(..., description="City of residence")]
    occupation: Annotated[Literal['retired', 'student', 'freelancer', 'government_job', 'business_owner', 'private_job', 'unemployed'],
                          Field(..., description="Occupation of the person")]

    @computed_field
    @property
    def bmi(self) -> float:
        return self.weight / (self.height ** 2)

    @computed_field
    @property
    def lifestyle_risk(self) -> str:
        if self.smoker and self.bmi > 30:
            return "high"
        elif self.smoker or self.bmi > 27:
            return "medium"
        else:
            return "low"

    @computed_field
    @property
    def age_group(self) -> str:
        if self.age < 18:
            return "young"
        elif 18 <= self.age < 45:
            return "adult"
        elif 45 <= self.age < 60:
            return "middle-aged"
        else:
            return "senior"

    @computed_field
    @property
    def city_tier(self) -> int:
        if self.city in tier_1_cities:
            return 1
        elif self.city in tier_2_cities:
            return 2
        else:
            return 3
        
    @field_validator('city')
    @classmethod
    def normalize_city(cls,v:str) -> str:
        v = v.strip().title()
        return v
