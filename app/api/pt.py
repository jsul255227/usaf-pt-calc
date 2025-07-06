from fastapi import APIRouter
from app.models.pt_models import PTRequest, PTResponse
from app.services.pt_service import calculate_pt_score, get_min_max_for_all_components

router = APIRouter()

@router.post("/calculate", response_model=PTResponse)
def calculate(request: PTRequest):
    """
    Calculate PT scores for all components in a single request.
    """
    return calculate_pt_score(request)

@router.get("/minmax")
def minmax(gender: str, age: int, component: str):
    """
    Get min/max values for a given component, gender, and age.
    """
    return get_min_max_for_all_components(gender, age, component)
