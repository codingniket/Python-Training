import pandas as pd

data = pd.read_json("customers.json")

normalized = pd.json_normalize(data["customers"])

print("Normalized Data:\n", normalized.head())