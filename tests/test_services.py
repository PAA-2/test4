import pytest
from paa.models import Plan
from paa.services import pdca, pdca_j

pytestmark = pytest.mark.django_db


def test_pdca_steps():
    plan = Plan.objects.create(name="Plan")
    steps = pdca(plan)
    assert steps == ["Plan:Plan", "Do", "Check", "Act"]


def test_pdca_j_adds_justify():
    plan = Plan.objects.create(name="Plan")
    assert pdca_j(plan)[-1] == "Justify"
