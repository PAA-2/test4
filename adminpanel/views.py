"""Views for the admin panel configuration."""

from django.contrib.auth.decorators import permission_required
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView, UpdateView

from . import forms, models


class SingleObjectUpdateView(UpdateView):
    """UpdateView operating on a single configuration instance."""

    def get_object(self, queryset=None):
        obj, _ = self.model.objects.get_or_create(pk=1)
        return obj


@method_decorator(permission_required("adminpanel.super_admin"), name="dispatch")
class PanelView(SingleObjectUpdateView):
    model = models.PanelConfig
    form_class = forms.PanelConfigForm
    template_name = "adminpanel/panel.html"
    success_url = reverse_lazy("adminpanel:panel")


@method_decorator(permission_required("adminpanel.super_admin"), name="dispatch")
class BrandingView(SingleObjectUpdateView):
    model = models.BrandingConfig
    form_class = forms.BrandingConfigForm
    template_name = "adminpanel/branding.html"
    success_url = reverse_lazy("adminpanel:branding")


@method_decorator(permission_required("adminpanel.super_admin"), name="dispatch")
class MenusView(SingleObjectUpdateView):
    model = models.MenuConfig
    form_class = forms.MenuConfigForm
    template_name = "adminpanel/menus.html"
    success_url = reverse_lazy("adminpanel:menus")


@method_decorator(permission_required("adminpanel.super_admin"), name="dispatch")
class FlagsView(SingleObjectUpdateView):
    model = models.FlagConfig
    form_class = forms.FlagConfigForm
    template_name = "adminpanel/flags.html"
    success_url = reverse_lazy("adminpanel:flags")


@method_decorator(permission_required("adminpanel.super_admin"), name="dispatch")
class SystemView(SingleObjectUpdateView):
    model = models.SystemConfig
    form_class = forms.SystemConfigForm
    template_name = "adminpanel/system.html"
    success_url = reverse_lazy("adminpanel:system")


@method_decorator(permission_required("adminpanel.super_admin"), name="dispatch")
class ImportProfilesView(SingleObjectUpdateView):
    model = models.ImportProfileConfig
    form_class = forms.ImportProfileConfigForm
    template_name = "adminpanel/import_profiles.html"
    success_url = reverse_lazy("adminpanel:import_profiles")


@method_decorator(permission_required("adminpanel.super_admin"), name="dispatch")
class SyncView(SingleObjectUpdateView):
    model = models.SyncConfig
    form_class = forms.SyncConfigForm
    template_name = "adminpanel/sync.html"
    success_url = reverse_lazy("adminpanel:sync")


@method_decorator(permission_required("adminpanel.super_admin"), name="dispatch")
class StorageView(SingleObjectUpdateView):
    model = models.StorageConfig
    form_class = forms.StorageConfigForm
    template_name = "adminpanel/storage.html"
    success_url = reverse_lazy("adminpanel:storage")


class ReportsView(TemplateView):
    """Display reports; no special permission required."""

    template_name = "adminpanel/reports.html"

