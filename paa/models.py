from django.db import models
from django.contrib.auth import get_user_model


class Plan(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:  # pragma: no cover - simple representation
        return self.name


class Action(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:  # pragma: no cover
        return self.name


class ActionPlan(models.Model):
    plan = models.ForeignKey(
        Plan, on_delete=models.CASCADE, related_name="action_plans"
    )
    action = models.ForeignKey(
        Action, on_delete=models.CASCADE, related_name="action_plans"
    )
    owner = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, null=True, blank=True
    )

    class Meta:
        unique_together = ("plan", "action")

    def __str__(self) -> str:  # pragma: no cover
        return f"{self.plan} -> {self.action}"
