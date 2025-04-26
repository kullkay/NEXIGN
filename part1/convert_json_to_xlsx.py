import json
import pandas as pd
from openpyxl import load_workbook
from openpyxl.utils import get_column_letter

# Загружаем Trivy-отчёт
with open("portainer.json", "r") as f:
    data = json.load(f)

# Собираем уязвимости
vulns = []
for result in data.get("Results", []):
    for vuln in result.get("Vulnerabilities", []):
        vulns.append({
            "PkgName": vuln.get("PkgName"),
            "VulnerabilityID": vuln.get("VulnerabilityID"),  
            "PkgID": vuln.get("PkgID"),
            "Severity": vuln.get("Severity"),
        })

df = pd.DataFrame(vulns)

# Сортируем по VulnerabilityID
grouped_df = pd.DataFrame(vulns).sort_values(by=["PkgName", "VulnerabilityID"])

# Путь к файлу
filename = "portainer_vulns_grouped.xlsx"

# Сохраняем в Excel
grouped_df.to_excel(filename, index=False)

# Загружаем рабочую книгу для форматирования
wb = load_workbook(filename)
ws = wb.active

# Устанавливаем ширину столбцов по максимальной длине в каждой колонке
for col in ws.columns:
    max_length = 0
    column = col[0].column  # Номер колонки (1, 2, 3…)
    for cell in col:
        try:
            if cell.value:
                max_length = max(max_length, len(str(cell.value)))
        except:
            pass
    adjusted_width = max_length + 2
    ws.column_dimensions[get_column_letter(column)].width = adjusted_width

# Сохраняем результат
wb.save(filename)
print(f"✅ Уязвимости сохранены и отформатированы в {filename}")