import pytest
from django.contrib.auth.models import User
from guardian.shortcuts import assign_perm
from paa.models import Plan

pytestmark = pytest.mark.django_db


def test_object_permission():
    user = User.objects.create_user("user")
    plan = Plan.objects.create(name="Secure")
    assign_perm("change_plan", user, plan)
    assert user.has_perm("change_plan", plan)
