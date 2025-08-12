import pytest
from openpyxl import Workbook
from paa.importers import import_plan_from_excel
from paa.models import Plan

pytestmark = pytest.mark.django_db


def test_import_plan(tmp_path):
    wb = Workbook()
    ws = wb.active
    ws.cell(row=11, column=1, value="Imported")
    file = tmp_path / "plan.xlsx"
    wb.save(file)
    plan = import_plan_from_excel(str(file))
    assert isinstance(plan, Plan)
    assert plan.name == "Imported"
