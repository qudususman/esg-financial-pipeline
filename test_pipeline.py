import unittest
from metrics import calculate_esg_score, compute_carbon_intensity, summarize_company

class TestESGPipeline(unittest.TestCase):
def test_esg_score(self):
self.assertEqual(calculate_esg_score(80, 70, 90), 79.0)

def test_carbon_intensity_zero_revenue(self):
self.assertEqual(compute_carbon_intensity(500, 0), 0.0)

def test_summarize_company(self):
sample = {
"Company": "Acme Corp",
"Industry": "Energy",
"Revenue": "1000",
"CarbonEmissions": "250",
"EnvScore": "60",
"SocScore": "70",
"GovScore": "80",
}
out = summarize_company(sample)
self.assertEqual(out["esg_score"], 69.0)
self.assertEqual(out["carbon_intensity"], 0.25)

if __name__ == "__main__":
unittest.main()
