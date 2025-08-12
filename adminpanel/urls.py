"""URL patterns for the admin panel app."""

from django.urls import path

from . import views


app_name = "adminpanel"

urlpatterns = [
    path("panel/", views.PanelView.as_view(), name="panel"),
    path("branding/", views.BrandingView.as_view(), name="branding"),
    path("menus/", views.MenusView.as_view(), name="menus"),
    path("flags/", views.FlagsView.as_view(), name="flags"),
    path("system/", views.SystemView.as_view(), name="system"),
    path("import-profiles/", views.ImportProfilesView.as_view(), name="import_profiles"),
    path("sync/", views.SyncView.as_view(), name="sync"),
    path("storage/", views.StorageView.as_view(), name="storage"),
    path("reports/", views.ReportsView.as_view(), name="reports"),
]

