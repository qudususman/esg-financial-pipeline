import csv
from pathlib import Path

def load_esg_records(filepath: str) -> list[dict]:
path = Path(filepath)
if not path.exists():
raise FileNotFoundError(f"Dataset not found: {filepath}")
records = []
with path.open("r", encoding="utf-8") as f:
reader = csv.DictReader(f)
for row in reader:
records.append(row)
return records

def clean_numeric(value: str, default: float = 0.0) -> float:
if value is None or str(value).strip() == "":
return default
return float(str(value).replace(",", "").strip())
