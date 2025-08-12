from django.contrib import admin
from guardian.admin import GuardedModelAdmin
from .models import Plan, Action, ActionPlan


@admin.register(Plan)
class PlanAdmin(GuardedModelAdmin):
    pass


@admin.register(Action)
class ActionAdmin(GuardedModelAdmin):
    pass


@admin.register(ActionPlan)
class ActionPlanAdmin(GuardedModelAdmin):
    pass
