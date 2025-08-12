"""Forms for admin panel configuration models."""

from django import forms

from . import models


class PanelConfigForm(forms.ModelForm):
    class Meta:
        model = models.PanelConfig
        fields = ["settings"]


class BrandingConfigForm(forms.ModelForm):
    class Meta:
        model = models.BrandingConfig
        fields = ["settings"]


class MenuConfigForm(forms.ModelForm):
    class Meta:
        model = models.MenuConfig
        fields = ["settings"]


class FlagConfigForm(forms.ModelForm):
    class Meta:
        model = models.FlagConfig
        fields = ["settings"]


class SystemConfigForm(forms.ModelForm):
    class Meta:
        model = models.SystemConfig
        fields = ["settings"]


class ImportProfileConfigForm(forms.ModelForm):
    class Meta:
        model = models.ImportProfileConfig
        fields = ["settings"]


class SyncConfigForm(forms.ModelForm):
    class Meta:
        model = models.SyncConfig
        fields = ["settings"]


class StorageConfigForm(forms.ModelForm):
    class Meta:
        model = models.StorageConfig
        fields = ["settings"]

