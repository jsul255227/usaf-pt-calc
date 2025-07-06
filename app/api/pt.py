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
    # Add top-level keys for points for frontend
    out["cardio_points"] = resp.component_scores["cardio"].score
    out["upper_points"] = resp.component_scores["upper"].score
    out["core_points"] = resp.component_scores["core"].score
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
