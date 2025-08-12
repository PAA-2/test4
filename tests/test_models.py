import pytest
from paa.models import Plan, Action, ActionPlan

pytestmark = pytest.mark.django_db


def test_actionplan_str():
    plan = Plan.objects.create(name="P")
    action = Action.objects.create(name="A")
    ap = ActionPlan.objects.create(plan=plan, action=action)
    assert str(ap) == "P -> A"
