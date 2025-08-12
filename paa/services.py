from typing import List
from .models import Plan


def pdca(plan: Plan) -> List[str]:
    """Return the PDCA steps for a plan."""
    return [f"Plan:{plan.name}", "Do", "Check", "Act"]


def pdca_j(plan: Plan) -> List[str]:
    """Return PDCA cycle with an extra Justify step."""
    steps = pdca(plan)
    steps.append("Justify")
    return steps
