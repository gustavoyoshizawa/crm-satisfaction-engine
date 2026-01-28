from pathlib import Path
from extract import extract_excel
from transform import (
    apply_quality_rules,
    calculate_metrics,
    calculate_score,
    segment_customers,
    generate_summaries
)
from load import load_mysql

BASE_DIR = Path(__file__).resolve().parent.parent
path = BASE_DIR / "data/input/crm_interactions.xlsx"

df = extract_excel(path)
df = apply_quality_rules(df)

metrics = calculate_metrics(df)
metrics = calculate_score(metrics)
metrics = segment_customers(metrics)
metrics = generate_summaries(metrics)

load_mysql(metrics)
