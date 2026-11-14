from loader import load_esg_records
from metrics import summarize_company

def run_pipeline(filepath: str) -> list[dict]:
raw_rows = load_esg_records(filepath)
results = []
for row in raw_rows:
results.append(summarize_company(row))
return results

if __name__ == "__main__":
print("ESG Financial Pipeline ready.")

