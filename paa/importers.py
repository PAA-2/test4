import openpyxl
from .models import Plan


def import_plan_from_excel(path: str) -> Plan:
    """Import plan name from excel file reading row 11 column 1."""
    wb = openpyxl.load_workbook(path)
    ws = wb.active
    name = ws.cell(row=11, column=1).value
    return Plan.objects.create(name=name)
