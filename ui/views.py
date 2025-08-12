from django.shortcuts import render


def dashboard(request):
    return render(request, "ui/dashboard.html")


def actions_view(request):
    return render(request, "ui/actions.html")


def kanban_view(request):
    return render(request, "ui/kanban.html")


def action_detail(request, pk):
    return render(request, "ui/action_detail.html", {"pk": pk})
