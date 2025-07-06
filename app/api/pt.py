from fastapi import APIRouter
from app.models.pt_models import PTRequest, PTResponse
from app.services.pt_service import calculate_pt_score, get_min_max_for_all_components

router = APIRouter()

@router.post("/calculate")
def calculate(request: PTRequest):
    """
    Calculate PT scores for all components in a single request.
    """
    resp = calculate_pt_score(request)
    # Flatten the response for frontend compatibility
    out = {k: v.dict() for k, v in resp.component_scores.items()}
    out["total_score"] = resp.total_score
    if resp.message:
        out["message"] = resp.message
    return out

@router.get("/minmax")
def minmax(gender: str, age: int, component: str):
    """
    Get min/max values for a given component, gender, and age.
    """
    return get_min_max_for_all_components(gender, age, component)
