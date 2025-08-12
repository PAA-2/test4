"""Models for admin panel configuration."""

from django.db import models


class ConfigBase(models.Model):
    """Abstract base for configuration models.

    Each configuration stores arbitrary settings in a JSON field and tracks
    the last update timestamp. All configuration models inherit from this
    base.
    """

    settings = models.JSONField(default=dict, blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class PanelConfig(ConfigBase):
    """General panel settings."""

    class Meta:
        permissions = [
            ("super_admin", "Can manage admin panel"),
        ]


class BrandingConfig(ConfigBase):
    """Branding options for the site."""


class MenuConfig(ConfigBase):
    """Navigation menu configuration."""


class FlagConfig(ConfigBase):
    """Feature flag toggles."""


class SystemConfig(ConfigBase):
    """System wide settings."""


class ImportProfileConfig(ConfigBase):
    """Import profiles settings."""


class SyncConfig(ConfigBase):
    """Data synchronisation settings."""


class StorageConfig(ConfigBase):
    """Storage related settings."""


# The reports section uses templates only and does not require a model.

