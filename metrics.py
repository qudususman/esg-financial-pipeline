from loader import clean_numeric

def calculate_esg_score(env: float, soc: float, gov: float) -> float:
return round(0.4 * env + 0.3 * soc + 0.3 * gov, 2)

def compute_carbon_intensity(emissions: float, revenue: float) -> float:
if revenue <= 0:
return 0.0
return round(emissions / revenue, 4)

def summarize_company(row: dict) -> dict:
revenue = clean_numeric(row.get("Revenue"))
emissions = clean_numeric(row.get("CarbonEmissions"))
esg = calculate_esg_score(
clean_numeric(row.get("EnvScore")),
clean_numeric(row.get("SocScore")),
clean_numeric(row.get("GovScore")),
)
return {
"company": row.get("Company", "Unknown"),
"industry": row.get("Industry", "General"),
"esg_score": esg,
"carbon_intensity": compute_carbon_intensity(emissions, revenue),
}
