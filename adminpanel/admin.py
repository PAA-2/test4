"""Admin registrations for admin panel models."""

from django.contrib import admin

from . import models


@admin.register(
    models.PanelConfig,
    models.BrandingConfig,
    models.MenuConfig,
    models.FlagConfig,
    models.SystemConfig,
    models.ImportProfileConfig,
    models.SyncConfig,
    models.StorageConfig,
)
class ConfigAdmin(admin.ModelAdmin):
    list_display = ("id", "updated_at")

