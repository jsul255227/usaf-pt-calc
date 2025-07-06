import importlib
from app.models.pt_models import PTRequest, PTResponse, PTComponentScore
from tables import *  # Import all tables for now (can optimize later)

# Helper: Map age to age group string
AGE_GROUPS = [
    ("under_25", range(0, 25)),
    ("25_29", range(25, 30)),
    ("30_34", range(30, 35)),
    ("35_39", range(35, 40)),
    ("40_44", range(40, 45)),
    ("45_49", range(45, 50)),
    ("50_54", range(50, 55)),
    ("55_59", range(55, 60)),
    ("over_60", range(60, 200)),
]

# Helper: Map component to table suffix
COMPONENT_SUFFIX = {
    "run": "RUN",
    "hamr": "HAMR",
    "pushups": "PUSHUPS",
    "hr_pushups": "HR_PUSHUPS",
    "situps": "SITUPS",
    "crunch": "CRUNCH",
    "plank": "PLANK",
}

COMPONENT_LIST = [
    "run", "hamr", "pushups", "hr_pushups", "situps", "crunch", "plank"
]

def get_age_group(age: int) -> str:
    for group, rng in AGE_GROUPS:
        if age in rng:
            return group
    raise ValueError(f"No age group for age {age}")

def get_table(gender: str, age: int, component: str):
    gender = gender.strip().lower()
    if gender not in ("male", "female"):
        raise ValueError("Gender must be 'male' or 'female'")
    gender_prefix = "MALE" if gender == "male" else "FEMALE"
    age_group = get_age_group(age)
    component = component.strip().lower()
    if component not in COMPONENT_SUFFIX:
        raise ValueError(f"Unknown component: {component}")
    suffix = COMPONENT_SUFFIX[component]
    # Build module and variable name
    module_name = f"tables.{gender_prefix.lower()}s_{age_group}"
    if age_group == "over_60":
        module_name = f"tables.{gender_prefix.lower()}s_over_60"
    elif age_group == "under_25":
        module_name = f"tables.{gender_prefix.lower()}s_under_25"
    var_name = f"{gender_prefix}_{age_group.upper()}_{suffix}"
    # Import module and get variable
    mod = importlib.import_module(module_name)
    table = getattr(mod, var_name)
    return table

def calculate_pt_score(request: PTRequest) -> PTResponse:
    component_scores = {}
    total = 0.0
    # Each category: cardio, upper, core
    categories = [
        ("cardio", request.cardio),
        ("upper", request.upper),
        ("core", request.core),
    ]
    for cat, comp_input in categories:
        component = comp_input.component
        value = comp_input.value
        try:
            table = get_table(request.gender, request.age, component)
        except Exception as e:
            component_scores[cat] = PTComponentScore(score=0, max_score=0, min_score=0, message=str(e))
            continue
        score = None
        max_score = max(row[2] for row in table)
        min_score = min(row[2] for row in table)
        min_allowed = min(row[0] for row in table)
        max_allowed = max(row[1] for row in table if row[1] != float('inf'))
        if component == "run":
            # Lower time is better
            if value > max_allowed:
                score = 0.0
            elif value < min_allowed:
                score = max_score
            else:
                for start, end, s in table:
                    if start <= value <= end:
                        score = s
                        break
        elif component == "plank":
            # Higher time is better, but time-based: above max = 20, below min = 0
            if value < min_allowed:
                score = 0.0
            elif value > max_allowed:
                score = max_score
            else:
                for start, end, s in table:
                    if start <= value <= end:
                        score = s
                        break
        else:
            # Rep-based: higher is better, above max = max points, below min = 0
            if value < min_allowed:
                score = 0.0
            elif value > max_allowed:
                score = max_score
            else:
                for start, end, s in table:
                    if start <= value <= end:
                        score = s
                        break
        component_scores[cat] = PTComponentScore(score=score, max_score=max_score, min_score=min_score)
        total += score
    return PTResponse(component_scores=component_scores, total_score=total)

def get_min_max_for_component(gender: str, age: int, component: str):
    table = get_table(gender, age, component)
    if component == "run":
        min_val = None
        max_val = max(row[1] for row in table if row[1] != float('inf'))
    elif component == "plank":
        min_val = min(row[0] for row in table)
        max_val = max(row[1] for row in table if row[1] != float('inf'))
    else:
        # For reps: min is the lowest finite end, max is the highest finite end
        finite_ends = [row[1] for row in table if row[1] != float('inf')]
        min_val = min(finite_ends) if finite_ends else None
        max_val = max(finite_ends) if finite_ends else None
    return {"min": min_val, "max": max_val}

def get_min_max_for_all_components(gender: str, age: int, component: str):
    """
    Return min/max for a single component (for dynamic frontend display).
    """
    try:
        table = get_table(gender, age, component)
    except Exception as e:
        return {"min": None, "max": None, "error": str(e)}
    min_val = float('inf')
    max_val = float('-inf')
    for start, end, _ in table:
        min_val = min(min_val, start)
        if end != float('inf'):
            max_val = max(max_val, end)
    return {"min": min_val, "max": max_val}
