from pydantic import BaseModel, validator
from typing import Optional, Dict

VALID_COMPONENTS = {"run", "hamr", "pushups", "hr_pushups", "situps", "crunch", "plank"}

class PTComponentInput(BaseModel):
    value: float
    component: str  # e.g., 'run', 'hamr', 'pushups', etc.

    @validator('component')
    def component_must_be_valid(cls, v):
        if v not in VALID_COMPONENTS:
            raise ValueError(f"Invalid component: {v}")
        return v
    
    @validator('value')
    def value_must_be_positive(cls, v):
        if v < 0:
            raise ValueError("Value must be non-negative")
        return v

class PTRequest(BaseModel):
    gender: str  # 'male' or 'female'
    age: int
    # Each category (cardio, upper, core) has a selected component and value
    cardio: PTComponentInput
    upper: PTComponentInput
    core: PTComponentInput

    @validator('gender')
    def gender_must_be_valid(cls, v):
        if v not in {"male", "female"}:
            raise ValueError("Gender must be 'male' or 'female'")
        return v
    
    @validator('age')
    def age_must_be_valid(cls, v):
        if not (17 <= v <= 100):
            raise ValueError("Age must be between 17 and 100")
        return v

class PTComponentScore(BaseModel):
    score: float
    max_score: float
    min_score: float
    message: Optional[str] = None

class PTResponse(BaseModel):
    component_scores: Dict[str, PTComponentScore]
    total_score: float
    message: Optional[str] = None
